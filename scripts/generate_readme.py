#!/usr/bin/env python3
"""Generate the five-column Agent paper index from reviewed metadata."""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from extract_figure import validate_image

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [
    "Surveys", "Multimodal Search and Retrieval", "Image Processing and Restoration",
    "Biomedical Visual Agents", "Video Understanding and Multi-Agent Systems",
    "Audio and Tool-Integrated Reasoning",
]
ZH = {
    "Surveys": "综述与研究路线",
    "Multimodal Search and Retrieval": "多模态搜索与检索 Agent",
    "Image Processing and Restoration": "图像处理与复原 Agent",
    "Biomedical Visual Agents": "生物医学视觉 Agent",
    "Video Understanding and Multi-Agent Systems": "视频理解与多智能体系统",
    "Audio and Tool-Integrated Reasoning": "音频与工具集成推理",
}
HOSTS = {"arxiv.org", "aclanthology.org", "openaccess.thecvf.com", "raw.githubusercontent.com"}
KINDS = {"framework", "architecture", "pipeline", "overview", "taxonomy", "benchmark", "dataset"}


def load_papers():
    papers = json.loads((ROOT / "data/papers.json").read_text())
    seen = set()
    for p in papers:
        if p["id"] in seen:
            raise ValueError(f"duplicate paper: {p['id']}")
        seen.add(p["id"])
        if not p["authors"] or p["section"] not in SECTIONS or not p["method"]:
            raise ValueError(f"incomplete paper: {p['id']}")
        f = p["figure"]
        if f["path"] != f"assets/frameworks/{p['id']}.png":
            raise ValueError(f"wrong image path: {p['id']}")
        url = urlparse(f["source_pdf_url"])
        if url.scheme != "https" or url.hostname not in HOSTS:
            raise ValueError(f"unapproved PDF source: {p['id']}")
        if url.hostname == "arxiv.org" and not re.search(r"v\d+$", url.path):
            raise ValueError(f"arXiv PDF must pin a version: {p['id']}")
        if not re.fullmatch(r"[0-9a-f]{64}", f["source_pdf_sha256"]):
            raise ValueError(f"invalid PDF hash: {p['id']}")
        if not re.fullmatch(r"Figure \d+", f["figure_label"]) or f["figure_kind"] not in KINDS:
            raise ValueError(f"invalid Figure label/kind: {p['id']}")
        if not isinstance(f["page"], int) or f["page"] < 1:
            raise ValueError(f"invalid page: {p['id']}")
        x0, y0, x1, y1 = f["crop_pt"]
        if not 0 <= x0 < x1 or not 0 <= y0 < y1:
            raise ValueError(f"invalid crop: {p['id']}")
        validate_image(ROOT / f["path"])
    expected = {ROOT / p["figure"]["path"] for p in papers}
    if set((ROOT / "assets/frameworks").glob("*.png")) != expected:
        raise ValueError("PNG inventory does not match paper metadata")
    return papers


def cell(value):
    return html.escape(str(value)).replace("|", "&#124;").replace("\n", " ")


def render(papers, chinese=False):
    title = "Awesome Multimodal Agents"
    lines = [f"# {title}", "", "[English](README.md) · [简体中文](README.zh-CN.md)", ""]
    if chinese:
        lines += [f"多模态与视觉 Agent 论文汇总，首批 **{len(papers)} 篇**。涵盖规划、工具调用、证据核验、强化学习与多智能体协作。", "", "每篇论文的 Framework 列直接展示作者原图，点击可查看完整 PNG。元数据核对日期：2026-10-06。会议状态以来源为准，预印本标注 arXiv。"]
    else:
        lines += [f"A curated collection of **{len(papers)} papers** on multimodal and visual agents: planning, tool use, evidence verification, reinforcement learning, and multi-agent collaboration.", "", "Each Framework cell displays an author-original figure. Click the thumbnail for the full PNG. Metadata reviewed on 2026-10-06; preprints are labeled arXiv."]
    lines += ["", "## Contents", ""]
    for s in SECTIONS:
        label = ZH[s] if chinese else s
        anchor = s.lower().replace(" ", "-")
        lines.append(f"- [{label}](#{anchor})")
    for s in SECTIONS:
        label = ZH[s] if chinese else s
        lines += ["", f'<a id="{s.lower().replace(" ", "-")}"></a>', f"## {label}", "", "| Conference / Journal | Method | Title | Resources | Framework |", "| :--- | :--- | :--- | :--- | :---: |"]
        for p in sorted((x for x in papers if x["section"] == s), key=lambda x: (-x["year"], x["title"])):
            f = p["figure"]
            resources = f'[Paper]({p["paper_url"]})'
            if p.get("code_url"):
                resources += f' · [Code]({p["code_url"]})'
            author = cell(p["authors"][0]) + (" et al." if len(p["authors"]) > 1 else "")
            figure = f'<a href="{f["path"]}"><img src="{f["path"]}" width="360" alt="{cell(p["method"])} {f["figure_label"]}"></a><br><sub>Original paper figure: {f["figure_label"]} · <a href="{f["source_pdf_url"]}#page={f["page"]}">Source: official PDF</a><br>Credit: {author}. © Paper authors/publisher. All rights remain with the original owner.'
            if f.get("license_url"):
                figure += f' · <a href="{f["license_url"]}">License</a>'
            figure += "</sub>"
            lines.append(f'| **{cell(p["venue"])}** | {cell(p["method"])} | {cell(p["title"])} | {resources} | {figure} |')
    lines += ["", "## Contributing", "", "See [CONTRIBUTING.md](CONTRIBUTING.md) for the review and reproducible cropping workflow. Add paper metadata to `data/papers.json`; keep original PDFs and previews in ignored `.figure-work/`.", "", "Figure selection: end-to-end framework → architecture → pipeline → method overview. Surveys may use an original taxonomy or overview. Crop page whitespace only; preserve labels, legends, arrows, and subfigure markers.", "", "## Acknowledgments and rights", "", "Layout inspired by [Awesome Aerial-Ground Object Re-Identification](https://github.com/Reflection0427/Awesome-Aerial-Ground-Object-Re-Identification). Search-agent entries and reviewed figure metadata are shared with [Awesome Multimodal Agentic Retrieval](https://github.com/Reflection0427/Awesome-Multimodal-Agentic-Retrieval).", "", "Repository code is MIT licensed. Paper figures remain under their original authors' or publishers' terms; the repository license does not relicense those figures. Rights holders may request removal or replacement with an official link via an Issue.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    papers = load_papers()
    for name, chinese in [("README.md", False), ("README.zh-CN.md", True)]:
        path = ROOT / name
        result = render(papers, chinese)
        if args.check:
            if not path.exists() or path.read_text() != result:
                raise SystemExit(f"stale {name}; run python scripts/generate_readme.py")
        else:
            path.write_text(result)
    print(f"Validated {len(papers)} papers and original PNGs")


if __name__ == "__main__":
    main()
