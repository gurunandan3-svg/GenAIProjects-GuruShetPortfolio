"""Guru Shet's career portfolio. Run with: uv run streamlit run main.py"""

import streamlit as st


st.set_page_config(
    page_title="Guru Shet | Technical Program Leader",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PROJECTS = {
    "uber-core-hr": {
        "client": "Uber",
        "logo": "uber.svg",
        "period": "2024 — Present",
        "role": "Staff Technical Program Manager · Enterprise Platforms",
        "title": "Global Core HR Platform & Data Hub",
        "summary": "Core HR platform delivery and multi-country data transformation across 65+ countries and 80 entities.",
        "scope": ["65+ countries", "80 entities", "100+ integrations"],
        "challenge": "Coordinate a global HR technology portfolio with connected data, integration, release, security, and testing workstreams. Teams needed consistent access to enterprise data and a more predictable way to prepare environments for release.",
        "role_detail": "Own end-to-end delivery for the Core HR technology portfolio. Translate business priorities into roadmaps, architecture decisions, integrated plans, dependencies, release strategy, and acceptance criteria. Coordinate engineering, product, process, and data teams across global workstreams.",
        "work": [
            "Led the build of an operational data hub to standardize data access across enterprise systems and support reusable integration patterns.",
            "Directed a multi-country ETL and data transformation program using GCP and BigQuery for staging, validation, and reconciliation.",
            "Coordinated definition of PRDs and ERDs for 100+ integrations, and reviewed data flows, APIs, service dependencies, and downstream impacts.",
            "Defined an environment-management and production-to-test cloning strategy; planned SIT, UAT, regression, deployment sequencing, and cutover readiness.",
            "Established the agile delivery cadence across three engineering teams, including sprint planning, capacity planning, and backlog prioritization.",
            "Automated sprint summaries from Jira with Claude to surface completed, in-progress, and delayed work for leadership.",
        ],
        "outcomes": [
            "New integration setup moved from days to minutes through the operational data hub.",
            "Production-to-test cloning and environment release time decreased by 50%.",
            "Automated sprint summaries save 3+ hours each week and provide faster delivery-risk visibility.",
        ],
    },
    "thermo-fisher": {
        "client": "Thermo Fisher Scientific (PPD)",
        "logo": "thermo-fisher.svg",
        "period": "2017 — 2024",
        "role": "Technical Program Manager / Integration Lead",
        "title": "Lawson to Oracle Cloud Transformation",
        "summary": "Global HCM and ERP transformation spanning integration architecture, data conversion, testing, cutover, and release readiness.",
        "scope": ["200+ interfaces", "30,000+ worker records", "70+ legacy systems retired"],
        "challenge": "Move a global HR and ERP landscape from Lawson to Oracle Cloud while maintaining reliable connections to payroll, benefits, compensation, absence, time and labor, ERP, identity, security, and downstream systems.",
        "role_detail": "Owned technical program delivery and integration leadership. Aligned architecture roadmaps, milestones, testing, cutover, and release readiness across onsite-offshore teams and multiple business and technology workstreams.",
        "work": [
            "Designed integration and conversion architecture supporting more than 200 interfaces.",
            "Directed ETL for migration and validation of 30,000+ worker records into Oracle HCM Cloud and ERP Cloud.",
            "Managed API, file-based, identity, security, data, and testing dependencies across Core HR, Payroll, Benefits, Compensation, Absence, OTL, ERP, and downstream systems.",
            "Established reusable integration patterns, delivery standards, and design-review governance adopted across workstreams.",
            "Coordinated SIT, UAT, regression testing, defect prioritization, deployment sequencing, and cutover runbooks.",
        ],
        "outcomes": [
            "Retired 70+ legacy systems and interfaces.",
            "Created reusable integration patterns and technical delivery standards across the program.",
            "Supported global launch readiness across HCM and ERP workstreams.",
        ],
    },
    "xerox": {
        "client": "Xerox Corporation",
        "logo": "xerox.svg",
        "period": "2014 — 2017",
        "role": "Technical Manager",
        "title": "Global Oracle HCM Cloud Program",
        "summary": "Conversion and integration architecture for a global Oracle HCM Cloud program with complex downstream dependencies.",
        "scope": ["200+ integrations", "Multi-country delivery", "Cloud + downstream systems"],
        "challenge": "Deliver a global HCM Cloud program while connecting local and downstream systems through varied integration patterns, identity requirements, and data movement constraints.",
        "role_detail": "Led conversion and integration architecture, technical standards, and cross-platform coordination for cloud and downstream systems.",
        "work": [
            "Designed integration patterns using REST and SOAP web services, SFTP, HCM Extracts, and HDL.",
            "Coordinated single sign-on enablement and cross-platform technical dependencies.",
            "Established technical standards for integrations and data conversion across the program.",
        ],
        "outcomes": [
            "Delivered 200+ complex integrations for a global HCM Cloud program.",
            "Created repeatable technical standards for cloud and downstream system delivery.",
        ],
    },
    "sensata": {
        "client": "Sensata Technologies",
        "logo": "sensata.svg",
        "period": "2013 — 2014",
        "role": "Oracle E-Business Suite Technical Lead",
        "title": "Oracle EBS R12 Delivery & Integration Redesign",
        "summary": "Oracle EBS R12 technical delivery, environment strategy, and service-oriented integration redesign.",
        "scope": ["15-person team", "Oracle EBS R12", "Onsite-offshore delivery"],
        "challenge": "Deliver Oracle EBS R12 technical work with dependable performance and environments while replacing older interface patterns with more maintainable integrations.",
        "role_detail": "Owned technical delivery planning, hardware sizing, performance testing, and environment strategy. Led a 15-person onsite-offshore team through implementation and integration work.",
        "work": [
            "Led Oracle EBS R12 implementation planning and technical delivery.",
            "Planned hardware sizing, performance testing, and environment strategy.",
            "Redesigned legacy interfaces into service-oriented integrations.",
        ],
        "outcomes": [
            "Introduced service-oriented patterns to replace legacy interfaces.",
            "Coordinated a 15-person onsite-offshore team across technical workstreams.",
        ],
    },
}

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root { --ink:#172b3a; --muted:#5d6d78; --line:#d9e1e5; --accent:#137c71; --wash:#f4f7f5; --paper:#ffffff; }
    html, body, [class*="css"] { font-family:'Manrope',sans-serif; }
    .stApp { background:#fbfcfa; color:var(--ink); }
    h1, h2, .stMarkdown h1, .stMarkdown h2 { color:#0b1f33 !important; -webkit-text-fill-color:#0b1f33 !important; opacity:1 !important; }
    [data-testid="stHeader"] { background:rgba(251,252,250,.95); }
    .block-container { max-width:1200px; padding-top:1.35rem; padding-bottom:4rem; }
    a { color:var(--accent) !important; }
    .site-nav { display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line); padding:4px 0 17px; margin-bottom:38px; }
    .site-nav .wordmark { font-size:.94rem; font-weight:800; letter-spacing:-.04em; color:#0b1f33 !important; -webkit-text-fill-color:#0b1f33 !important; opacity:1 !important; }
    .site-nav .wordmark span { color:#00594f !important; -webkit-text-fill-color:#00594f !important; }
    .nav-meta { color:var(--muted); font: .68rem 'DM Mono',monospace; letter-spacing:.06em; }
    .eyebrow, .section-label { color:var(--accent); font: .68rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.13em; }
    .hero-title { font-size:clamp(2.75rem,5vw,4.7rem); font-weight:700; letter-spacing:-.075em; line-height:1.02; color:#0b1f33 !important; -webkit-text-fill-color:#0b1f33 !important; opacity:1 !important; margin:.7rem 0 1.25rem; }
    .hero-title em { color:#00594f !important; -webkit-text-fill-color:#00594f !important; font-style:normal; }
    .headline { color:#334959; font-size:1.05rem; line-height:1.7; font-weight:600; max-width:580px; }
    .hero-copy { color:var(--muted); font-size:.95rem; line-height:1.8; max-width:550px; margin-top:18px; }
    .hero-facts { display:flex; flex-wrap:wrap; gap:8px; margin-top:23px; }
    .fact { color:#415664; border:1px solid var(--line); background:#fff; border-radius:999px; padding:7px 11px; font: .65rem 'DM Mono',monospace; }
    .cta-row { display:flex; flex-wrap:wrap; gap:15px; margin-top:25px; font-size:.86rem; font-weight:700; }
    .timeline-panel { background:var(--wash); border:1px solid var(--line); border-radius:8px; padding:22px 24px 8px; }
    .timeline-heading { display:flex; justify-content:space-between; align-items:baseline; gap:12px; margin-bottom:4px; }
    .timeline-heading h2 { margin:0; color:var(--ink); font-size:1.22rem; letter-spacing:-.04em; }
    .timeline-heading span { color:var(--muted); font: .62rem 'DM Mono',monospace; }
    .project-row { position:relative; padding:18px 0 19px 23px; border-left:1px solid #b5c8c4; border-bottom:1px solid var(--line); }
    .project-row:last-child { border-bottom:0; }
    .project-row:before { content:''; position:absolute; left:-5px; top:23px; width:9px; height:9px; border-radius:50%; background:var(--accent); box-shadow:0 0 0 4px var(--wash); }
    .project-period { color:var(--accent); font: .62rem 'DM Mono',monospace; letter-spacing:.04em; margin-bottom:6px; }
    .project-row a { color:var(--ink) !important; text-decoration:none; font-weight:700; font-size:.9rem; letter-spacing:-.02em; }
    .project-row a:hover { color:var(--accent) !important; text-decoration:underline; }
    .project-client { color:var(--muted); font-size:.74rem; margin-top:3px; }
    .project-desc { color:#526571; font-size:.77rem; line-height:1.6; margin-top:6px; }
    .open-hint { color:var(--accent); font-size:.68rem; font-weight:700; margin-top:7px; }
    .section { margin-top:74px; }
    .section h2 { color:#0b1f33 !important; -webkit-text-fill-color:#0b1f33 !important; font-size:1.85rem; letter-spacing:-.055em; margin:.5rem 0 1rem; }
    .path-list { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; }
    .path-card { background:#fff; border:1px solid var(--line); border-radius:6px; padding:17px 18px; min-height:100px; }
    .path-card b { color:var(--ink); font-size:.83rem; }
    .path-card span { display:block; color:var(--muted); font-size:.73rem; margin-top:7px; line-height:1.5; }
    .detail-top { display:flex; justify-content:space-between; gap:22px; align-items:center; background:var(--wash); border:1px solid var(--line); border-radius:8px; padding:22px 25px; margin-bottom:30px; }
    .detail-logo { width:210px; height:70px; object-fit:contain; background:white; padding:11px 16px; border:1px solid var(--line); border-radius:5px; }
    .detail-title { color:#0b1f33 !important; -webkit-text-fill-color:#0b1f33 !important; font-size:clamp(2.2rem,5vw,3.8rem); line-height:1.04; letter-spacing:-.07em; margin:.55rem 0 .7rem; }
    .detail-summary { color:var(--muted); font-size:1rem; line-height:1.7; max-width:800px; }
    .detail-meta { color:var(--accent); font: .68rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.06em; }
    .scope-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin:26px 0 34px; }
    .scope-item { background:#fff; border:1px solid var(--line); border-radius:6px; padding:16px; color:var(--ink); font-weight:700; font-size:.87rem; }
    .detail-section { margin:30px 0; }
    .detail-section h2 { color:var(--ink); font-size:1.25rem; letter-spacing:-.04em; margin:0 0 10px; }
    .detail-section p, .detail-section li { color:#526571; font-size:.9rem; line-height:1.8; }
    .detail-section ul { padding-left:20px; }
    .outcome { border-left:3px solid var(--accent); padding:2px 0 2px 14px; margin:12px 0; color:var(--ink); font-size:.9rem; line-height:1.65; }
    .backlink { display:inline-block; margin-bottom:20px; font-size:.82rem; font-weight:700; text-decoration:none; }
    .footer { border-top:1px solid var(--line); margin-top:72px; padding-top:17px; color:#81909a; font: .65rem 'DM Mono',monospace; }
    @media(max-width:850px){ .path-list{grid-template-columns:1fr 1fr} }
    @media(max-width:650px){ .block-container{padding-left:1.1rem;padding-right:1.1rem} .site-nav{margin-bottom:26px} .nav-meta{display:none} .timeline-panel{padding:19px 17px 6px} .path-list,.scope-grid{grid-template-columns:1fr} .detail-top{align-items:flex-start; flex-direction:column} .detail-logo{width:170px;height:56px} }
    </style>
    """,
    unsafe_allow_html=True,
)


def logo_src(filename: str) -> str:
    return f"/app/static/logos/{filename}"


def site_nav() -> None:
    brand, location = st.columns([1, 1], vertical_alignment="center")
    with brand:
        st.markdown("### GURU SHET / PORTFOLIO")
    with location:
        st.caption("APEX, NORTH CAROLINA  ·  ENTERPRISE PROGRAM LEADERSHIP")
    st.divider()


def show_project(project_id: str) -> None:
    project = PROJECTS.get(project_id)
    if project is None:
        st.error("That project could not be found.")
        st.markdown('<a class="backlink" href="?">← Back to portfolio</a>', unsafe_allow_html=True)
        return

    logo = logo_src(project["logo"])
    st.markdown('<a class="backlink" href="?">← Back to portfolio</a>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="detail-top"><div><div class="section-label">PROJECT CASE STUDY</div>'
        f'<h1 class="detail-title">{project["title"]}</h1>'
        f'<div class="detail-meta">{project["period"]} &nbsp; · &nbsp; {project["role"]}</div>'
        f'<p class="detail-summary">{project["summary"]}</p></div>'
        f'<img class="detail-logo" src="{logo}" alt="{project["client"]} logo"></div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="scope-grid">' + "".join(f'<div class="scope-item">{item}</div>' for item in project["scope"]) + "</div>", unsafe_allow_html=True)
    st.markdown(f'<div class="detail-section"><h2>The challenge</h2><p>{project["challenge"]}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="detail-section"><h2>My role</h2><p>{project["role_detail"]}</p></div>', unsafe_allow_html=True)
    work_items = "".join(f"<li>{item}</li>" for item in project["work"])
    st.markdown(f'<div class="detail-section"><h2>Selected work</h2><ul>{work_items}</ul></div>', unsafe_allow_html=True)
    outcomes = "".join(f'<div class="outcome">{item}</div>' for item in project["outcomes"])
    st.markdown(f'<div class="detail-section"><h2>Outcomes</h2>{outcomes}</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">GURU SHET &nbsp; · &nbsp; PROJECT CASE STUDY</div>', unsafe_allow_html=True)


site_nav()
selected_project = st.query_params.get("project")

if selected_project:
    show_project(selected_project)
else:
    left, right = st.columns([1.02, 0.98], gap="large", vertical_alignment="top")
    with left:
        st.markdown('<div class="eyebrow">STAFF TECHNICAL PROGRAM MANAGER · ENTERPRISE PLATFORMS</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title" style="color:#0b1f33 !important;-webkit-text-fill-color:#0b1f33 !important;">Turning complex<br>systems into<br><em style="color:#00594f !important;-webkit-text-fill-color:#00594f !important;">clear outcomes.</em></h1>', unsafe_allow_html=True)
        st.markdown('<div class="headline">HR & ERP platforms · Oracle Cloud · Enterprise integration · Data transformation · Global delivery</div>', unsafe_allow_html=True)
        st.markdown('<p class="hero-copy">I lead global enterprise platform, data, and integration programs from architecture through production launch. With 21 years across Oracle Cloud, Workday, and ERP transformations, I connect technical depth with clear decisions, aligned teams, and measurable results.</p>', unsafe_allow_html=True)
        st.markdown('<div class="hero-facts"><span class="fact">21 YEARS IN ENTERPRISE TECHNOLOGY</span><span class="fact">65+ COUNTRIES</span><span class="fact">GLOBAL PROGRAM DELIVERY</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="cta-row"><a href="mailto:gurunandan3@gmail.com">Email Guru ↗</a><a href="https://www.linkedin.com/in/guru-shet/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div>', unsafe_allow_html=True)
    with right:
        rows = []
        for project_id, project in PROJECTS.items():
            rows.append(
                f'<div class="project-row"><div class="project-period">{project["period"]}</div>'
                f'<a href="?project={project_id}" target="_blank" rel="noopener noreferrer">{project["title"]} ↗</a>'
                f'<div class="project-client">{project["client"]} &nbsp; · &nbsp; {project["role"]}</div>'
                f'<div class="project-desc">{project["summary"]}</div>'
                '<div class="open-hint">Open case study in a new tab</div></div>'
            )
        st.markdown(
            '<div class="timeline-panel"><div class="timeline-heading"><h2>Project timeline</h2>'
            '<span>SELECT A PROJECT ↗</span></div>' + "".join(rows) + "</div>",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section"><div class="section-label">CAREER PATH</div><h2>Experience across platforms and scale.</h2></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="path-list">'
        '<div class="path-card"><b>Uber</b><span>Staff Technical Program Manager · Enterprise Platforms · 2024–Present</span></div>'
        '<div class="path-card"><b>KBACE, a Cognizant company</b><span>Associate Director, Technical Program Management · 2007–2024</span></div>'
        '<div class="path-card"><b>Oracle</b><span>Staff Consultant · Bangalore, India · 2005–2007</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="section"><div class="section-label">AREAS OF STRENGTH</div><h2>Technical depth. Program-wide view.</h2></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="path-list">'
        '<div class="path-card"><b>Platforms</b><span>Oracle Cloud HCM & ERP · Workday · Oracle EBS · OIC</span></div>'
        '<div class="path-card"><b>Data & integration</b><span>GCP · BigQuery · Snowflake · ETL · SQL · REST/SOAP APIs</span></div>'
        '<div class="path-card"><b>Delivery leadership</b><span>Roadmaps · OKRs · Agile · RAID · SIT/UAT · Cutover · Release strategy</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="footer">GURU SHET &nbsp; · &nbsp; MCGINTIRE SCHOOL OF COMMERCE, UVA · EXECUTIVE BUSINESS MANAGEMENT &nbsp; · &nbsp; VTU, B.E. ELECTRONICS & COMMUNICATION</div>', unsafe_allow_html=True)
