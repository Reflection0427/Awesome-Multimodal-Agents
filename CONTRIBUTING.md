# Maintaining the paper collection

1. Add a record to `data/papers.json` with a stable ID, exact title, authors, method, verified venue, category, and resource links. Use arXiv when a conference acceptance is unconfirmed.
2. Read the official PDF and select the complete end-to-end framework, architecture, pipeline, or method overview. Surveys may use taxonomy/overview figures.
3. Record the pinned official PDF URL, SHA-256, one-based PDF page, Figure label, figure kind, and crop coordinates `[x0, y0, x1, y1]` in PDF points (origin at top-left). Record a license URL only when verified.
4. Run `python scripts/extract_figure.py --paper-id PAPER_ID`. To supply a legally obtained PDF when its official host is temporarily inaccessible, put it in `.figure-work/pdfs/PAPER_ID.pdf`; the same SHA-256 check applies.
5. Open the PNG and compare it with the PDF. Keep complete arrows, legends, labels, and subfigure markers. Remove surrounding page whitespace; do not redraw, recolor, remove watermarks, or add content.
6. Run `python scripts/generate_readme.py`, then `python scripts/generate_readme.py --check`. Commit metadata, PNG, and both README files together in a PR.

Setup: `python -m pip install -r requirements.txt`.

Temporary PDFs and previews belong in ignored `.figure-work/`. Formal entries need exactly one readable original PNG and complete provenance. The Validate workflow checks metadata, image dimensions, inventory, and README synchronization; human PDF review is also required.

Initial scope includes multimodal search, image restoration, biomedical visual reasoning, video understanding, audio reasoning, and tool-using agents. Further categories may be added when reviewed papers justify them.
