# Awesome Multimodal Agents

[English](README.md) · [简体中文](README.zh-CN.md)

多模态与视觉 Agent 论文汇总，首批 **15 篇**。涵盖规划、工具调用、证据核验、强化学习与多智能体协作。

每篇论文的 Framework 列直接展示作者原图，点击可查看完整 PNG。元数据核对日期：2026-10-06。会议状态以来源为准，预印本标注 arXiv。

## Contents

- [综述与研究路线](#surveys)
- [多模态搜索与检索 Agent](#multimodal-search-and-retrieval)
- [图像处理与复原 Agent](#image-processing-and-restoration)
- [生物医学视觉 Agent](#biomedical-visual-agents)
- [视频理解与多智能体系统](#video-understanding-and-multi-agent-systems)
- [音频与工具集成推理](#audio-and-tool-integrated-reasoning)

<a id="surveys"></a>
## 综述与研究路线

| Conference / Journal | Method | Title | Resources | Framework |
| :--- | :--- | :--- | :--- | :---: |
| **ACL 2026** | Survey | A Survey of Large Language Model-Based Search Agents | [Paper](https://aclanthology.org/2026.acl-long.374/) | <a href="assets/frameworks/llm-search-agents-survey.png"><img src="assets/frameworks/llm-search-agents-survey.png" width="360" alt="Survey Figure 2"></a><br><sub>Original paper figure: Figure 2 · <a href="https://aclanthology.org/2026.acl-long.374.pdf#page=3">Source: official PDF</a><br>Credit: Yunjia Xi et al.. © Paper authors/publisher. All rights remain with the original owner. · <a href="https://creativecommons.org/licenses/by/4.0/">License</a></sub> |

<a id="multimodal-search-and-retrieval"></a>
## 多模态搜索与检索 Agent

| Conference / Journal | Method | Title | Resources | Framework |
| :--- | :--- | :--- | :--- | :---: |
| **arXiv 2026** | DeepImageSearch | DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories | [Paper](https://arxiv.org/abs/2602.10809) | <a href="assets/frameworks/deep-image-search.png"><img src="assets/frameworks/deep-image-search.png" width="360" alt="DeepImageSearch Figure 3"></a><br><sub>Original paper figure: Figure 3 · <a href="https://arxiv.org/pdf/2602.10809v2#page=5">Source: official PDF</a><br>Credit: Chenlong Deng et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **ICML 2026** | Fix Before Search | Fix Before Search: Benchmarking Agentic Visual Query Pre-processing in Multimodal RAG | [Paper](https://proceedings.mlr.press/v306/zeng26w.html) · [Code](https://github.com/phycholosogy/VQQP_Bench) | <a href="assets/frameworks/fix-before-search.png"><img src="assets/frameworks/fix-before-search.png" width="360" alt="Fix Before Search Figure 1"></a><br><sub>Original paper figure: Figure 1 · <a href="https://raw.githubusercontent.com/mlresearch/v306/main/assets/zeng26w/zeng26w.pdf#page=1">Source: official PDF</a><br>Credit: Shenglai Zeng et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **ICLR 2026** | MC-Search | MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains | [Paper](https://arxiv.org/abs/2603.00873) · [Code](https://mc-search-project.github.io/) | <a href="assets/frameworks/mc-search.png"><img src="assets/frameworks/mc-search.png" width="360" alt="MC-Search Figure 2"></a><br><sub>Original paper figure: Figure 2 · <a href="https://arxiv.org/pdf/2603.00873v1#page=3">Source: official PDF</a><br>Credit: Xuying Ning et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **ICLR 2026** | MMSearch-Plus | MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents | [Paper](https://arxiv.org/abs/2508.21475) · [Code](https://github.com/mmsearch-plus/MMSearch-Plus) | <a href="assets/frameworks/mmsearch-plus.png"><img src="assets/frameworks/mmsearch-plus.png" width="360" alt="MMSearch-Plus Figure 1"></a><br><sub>Original paper figure: Figure 1 · <a href="https://arxiv.org/pdf/2508.21475v3#page=2">Source: official PDF</a><br>Credit: Xijia Tao et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **arXiv 2026** | Agentic Planning | Reason Before You Retrieve: Agentic Planning for Multi-modal RAG | [Paper](https://arxiv.org/abs/2607.22643) | <a href="assets/frameworks/reason-before-retrieve.png"><img src="assets/frameworks/reason-before-retrieve.png" width="360" alt="Agentic Planning Figure 1"></a><br><sub>Original paper figure: Figure 1 · <a href="https://arxiv.org/pdf/2607.22643v1#page=2">Source: official PDF</a><br>Credit: Tianyu Yang et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **arXiv 2026** | V-Retrver | V-Retrver: Evidence-Driven Agentic Reasoning for Universal Multimodal Retrieval | [Paper](https://arxiv.org/abs/2602.06034) · [Code](https://github.com/chendy25/V-Retrver) | <a href="assets/frameworks/v-retrver.png"><img src="assets/frameworks/v-retrver.png" width="360" alt="V-Retrver Figure 2"></a><br><sub>Original paper figure: Figure 2 · <a href="https://arxiv.org/pdf/2602.06034v4#page=4">Source: official PDF</a><br>Credit: Dongyang Chen et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **arXiv 2026** | VLD-RAG | VLD-RAG: Agentic Vision-Language RAG for Long, Visually Rich Multi-Page Documents | [Paper](https://arxiv.org/abs/2607.24748) | <a href="assets/frameworks/vld-rag.png"><img src="assets/frameworks/vld-rag.png" width="360" alt="VLD-RAG Figure 1"></a><br><sub>Original paper figure: Figure 1 · <a href="https://arxiv.org/pdf/2607.24748v1#page=2">Source: official PDF</a><br>Credit: Seonok Kim. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **arXiv 2026** | WeAgent-MMSearch | WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents | [Paper](https://arxiv.org/abs/2608.28062) | <a href="assets/frameworks/weagent-mmsearch.png"><img src="assets/frameworks/weagent-mmsearch.png" width="360" alt="WeAgent-MMSearch Figure 3"></a><br><sub>Original paper figure: Figure 3 · <a href="https://arxiv.org/pdf/2608.28062v2#page=5">Source: official PDF</a><br>Credit: Zongkai Liu et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |
| **MAGMaR at SIGIR 2025** | CollEX | CollEX: A Multimodal Agentic RAG System Enabling Interactive Exploration of Scientific Collections | [Paper](https://aclanthology.org/2025.magmar-1.2/) | <a href="assets/frameworks/collex.png"><img src="assets/frameworks/collex.png" width="360" alt="CollEX Figure 4"></a><br><sub>Original paper figure: Figure 4 · <a href="https://aclanthology.org/2025.magmar-1.2.pdf#page=3">Source: official PDF</a><br>Credit: Florian Schneider et al.. © Paper authors/publisher. All rights remain with the original owner. · <a href="https://creativecommons.org/licenses/by/4.0/">License</a></sub> |
| **EMNLP 2025** | ViDoRAG | ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents | [Paper](https://aclanthology.org/2025.emnlp-main.464/) · [Code](https://github.com/Alibaba-NLP/ViDoRAG) | <a href="assets/frameworks/vidorag.png"><img src="assets/frameworks/vidorag.png" width="360" alt="ViDoRAG Figure 3"></a><br><sub>Original paper figure: Figure 3 · <a href="https://aclanthology.org/2025.emnlp-main.464.pdf#page=5">Source: official PDF</a><br>Credit: Qiuchen Wang et al.. © Paper authors/publisher. All rights remain with the original owner. · <a href="https://creativecommons.org/licenses/by/4.0/">License</a></sub> |

<a id="image-processing-and-restoration"></a>
## 图像处理与复原 Agent

| Conference / Journal | Method | Title | Resources | Framework |
| :--- | :--- | :--- | :--- | :---: |
| **CVPR 2026** | Dynamic Multi-Expert Fusion | Beyond Sequential Tools: A Unified VLM Agent System for Photographic Post-Processing via Dynamic Multi-Expert Fusion | [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.pdf) | <a href="assets/frameworks/beyond-sequential-tools.png"><img src="assets/frameworks/beyond-sequential-tools.png" width="360" alt="Dynamic Multi-Expert Fusion Figure 1"></a><br><sub>Original paper figure: Figure 1 · <a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.pdf#page=3">Source: official PDF</a><br>Credit: Honglin Xiong et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |

<a id="biomedical-visual-agents"></a>
## 生物医学视觉 Agent

| Conference / Journal | Method | Title | Resources | Framework |
| :--- | :--- | :--- | :--- | :---: |
| **CVPR 2026** | IBISAgent | IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation | [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_IBISAgent_Reinforcing_Pixel-Level_Visual_Reasoning_in_MLLMs_for_Universal_Biomedical_CVPR_2026_paper.pdf) · [Code](https://github.com/Yankai96/IBISAgent) | <a href="assets/frameworks/ibisagent.png"><img src="assets/frameworks/ibisagent.png" width="360" alt="IBISAgent Figure 2"></a><br><sub>Original paper figure: Figure 2 · <a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_IBISAgent_Reinforcing_Pixel-Level_Visual_Reasoning_in_MLLMs_for_Universal_Biomedical_CVPR_2026_paper.pdf#page=4">Source: official PDF</a><br>Credit: Yankai Jiang et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |

<a id="video-understanding-and-multi-agent-systems"></a>
## 视频理解与多智能体系统

| Conference / Journal | Method | Title | Resources | Framework |
| :--- | :--- | :--- | :--- | :---: |
| **CVPR 2026** | Symphony | Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding | [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_Symphony_A_Cognitively-Inspired_Multi-Agent_System_for_Long-Video_Understanding_CVPR_2026_paper.pdf) · [Code](https://github.com/Haiyang0226/Symphony) | <a href="assets/frameworks/symphony.png"><img src="assets/frameworks/symphony.png" width="360" alt="Symphony Figure 2"></a><br><sub>Original paper figure: Figure 2 · <a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_Symphony_A_Cognitively-Inspired_Multi-Agent_System_for_Long-Video_Understanding_CVPR_2026_paper.pdf#page=3">Source: official PDF</a><br>Credit: Haiyang Yan et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |

<a id="audio-and-tool-integrated-reasoning"></a>
## 音频与工具集成推理

| Conference / Journal | Method | Title | Resources | Framework |
| :--- | :--- | :--- | :--- | :---: |
| **arXiv 2026** | ToolDF | TOOLDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection | [Paper](https://arxiv.org/pdf/2609.03620v1) · [Code](https://github.com/rlataewoo/tooldf) | <a href="assets/frameworks/tooldf.png"><img src="assets/frameworks/tooldf.png" width="360" alt="ToolDF Figure 1"></a><br><sub>Original paper figure: Figure 1 · <a href="https://arxiv.org/pdf/2609.03620v1#page=3">Source: official PDF</a><br>Credit: Taewoo Kim et al.. © Paper authors/publisher. All rights remain with the original owner.</sub> |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review and reproducible cropping workflow. Add paper metadata to `data/papers.json`; keep original PDFs and previews in ignored `.figure-work/`.

Figure selection: end-to-end framework → architecture → pipeline → method overview. Surveys may use an original taxonomy or overview. Crop page whitespace only; preserve labels, legends, arrows, and subfigure markers.

## Acknowledgments and rights

Layout inspired by [Awesome Aerial-Ground Object Re-Identification](https://github.com/Reflection0427/Awesome-Aerial-Ground-Object-Re-Identification). Search-agent entries and reviewed figure metadata are shared with [Awesome Multimodal Agentic Retrieval](https://github.com/Reflection0427/Awesome-Multimodal-Agentic-Retrieval).

Repository code is MIT licensed. Paper figures remain under their original authors' or publishers' terms; the repository license does not relicense those figures. Rights holders may request removal or replacement with an official link via an Issue.
