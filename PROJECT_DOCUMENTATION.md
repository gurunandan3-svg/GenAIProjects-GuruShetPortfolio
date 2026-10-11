# Guru Shet Portfolio Project

## Project overview

This project is a locally runnable, single-page portfolio built with Streamlit. It presents Guru Shet's enterprise technology and program leadership experience through a professional introduction, career timeline, areas of strength, and four project case studies.

The documentation describes the current implementation. The available folder does not contain earlier draft snapshots or commit history, so the development sequence below is reconstructed from the current code and README. It should not be read as a precise record of dated edits.

## Problem statement

A resume and a LinkedIn profile are useful records, but they do not always make the scale, complexity, and outcomes of technical program work easy to scan. The portfolio addresses this by giving a visitor a concise overview first, then letting them open selected projects for more context.

The experience is designed to help a prospective employer or colleague quickly understand:

- Guru's professional focus and areas of expertise.
- The progression of his career and the organizations represented.
- The challenge, role, work, and outcomes associated with selected programs.
- The scale of those programs through concrete scope markers, such as countries, integrations, records, and systems.

## How the project developed

### 1. Initial draft: establish a clear portfolio structure

The draft established the core content and navigation model: a landing page with a professional headline and project timeline, with each timeline item opening a case study. The repository README describes this draft structure. The current Streamlit implementation retains it.

### 2. Refine the landing page for quick scanning

The landing page now groups information into distinct sections:

- A hero area with the professional headline, summary, experience facts, and email and LinkedIn links.
- A project timeline with four selectable projects.
- A career path section covering Uber, KBACE/Cognizant, and Oracle.
- An areas-of-strength section covering platforms, data and integration, and delivery leadership.

This gives visitors an overview before asking them to read a full case study.

### 3. Expand project entries into case studies

Each project is represented by structured content in the `PROJECTS` mapping in `main.py`. The four entries cover Uber, Thermo Fisher Scientific (PPD), Xerox, and Sensata Technologies. A case study contains the period, role, project title, summary, scope markers, challenge, role detail, selected work, and outcomes.

This format makes the project pages consistent and lets visitors compare different examples of program leadership.

### 4. Add visual identity and responsive layout

Custom CSS in `main.py` supplies the portfolio's typography, colors, timeline, cards, spacing, and mobile layout. The Streamlit theme in `.streamlit/config.toml` provides matching base colors. Company SVG logos are stored in `static/logos/` and shown on case study pages.

### 5. Make the app straightforward to run

The project declares Python and package requirements in `pyproject.toml`, locks dependency versions in `uv.lock`, and includes a local run command in the README. Static file serving is enabled in the Streamlit configuration.

## Step-by-step: what happens in the app

1. Streamlit starts `main.py` and applies the page title, wide layout, and collapsed sidebar settings.
2. The app defines the four case studies and their content in `PROJECTS`.
3. Shared CSS and the site navigation are rendered.
4. The app checks the URL query parameter named `project`.
5. If a known project ID is present, the app renders that case study, including its logo, scope, challenge, role, selected work, and outcomes. The back link returns to the portfolio landing page.
6. If no project ID is present, the app renders the landing page, timeline, career path, and areas of strength.
7. Project timeline links open their case studies in a new browser tab.

## Main files

| File or folder | Purpose |
| --- | --- |
| `main.py` | Streamlit app, project content, page rendering, and CSS styling. |
| `.streamlit/config.toml` | Streamlit theme and static file serving configuration. |
| `pyproject.toml` | Project metadata, Python version requirement, and dependencies. |
| `uv.lock` | Locked dependency resolution for reproducible setup with `uv`. |
| `static/logos/` | Logo files served by the running app. |
| `assets/logos/` | Logo source copies and notes on attribution. |
| `README.md` | Short setup and local run instructions. |

## Run locally

From the `GuruShetPortfolio` directory, use:

```powershell
uv sync
uv run streamlit run main.py
```

Then open `http://localhost:8501` if Streamlit does not open a browser automatically. An alternative is `streamlit run main.py` in a Python environment where the project dependencies are installed.

The project currently specifies Python `>=3.14` in `pyproject.toml`.

## Current scope and follow-up review

The repository describes this as a local draft that has not been published. Before publishing, review the public contact details and LinkedIn link, verify all project wording and metrics, and decide whether to add project links, screenshots, or other artifacts. The logo notes in `assets/logos/README.md` identify their sources and remind users to review applicable terms for use beyond a personal career portfolio.
