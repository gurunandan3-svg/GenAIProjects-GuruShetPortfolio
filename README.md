# Guru Shet — Portfolio draft

A Streamlit portfolio built from the supplied resume and public LinkedIn profile details. The landing page puts the professional headline on the left and a clickable project timeline on the right. Each case study opens in a new tab and includes the client logo, project context, role, scope, selected work, and outcomes.

The landing page keeps the headline on the left and puts four project case studies in a clickable timeline on the right. Each case study opens in a new tab and includes the client logo, project context, role, scope, selected work, and outcomes.

Company logo sources are recorded in `assets/logos/README.md`. Runtime logo copies are served from `static/logos/`.

## Run locally

From this folder, install the project dependencies and start Streamlit:

```powershell
uv sync
uv run streamlit run main.py
```

Or, with a Python environment that has Streamlit installed:

```powershell
streamlit run main.py
```

Streamlit opens the draft in your browser, usually at `http://localhost:8501`.

## Content to review

- Confirm that the contact details and LinkedIn link should be public.
- Review the selected project descriptions and metrics against your preferred wording.
- Add any project links, screenshots, or artifacts you want prospective employers to see.
- This is a local draft; it has not been published.
