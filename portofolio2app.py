import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Karina Dyah Paramitha - Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Styling ---
# CSS Anda sudah sangat bagus, saya hanya melakukan sedikit penyesuaian
# dan menghapus background-image.
st.markdown("""
<style>
    /* General body font and scroll behavior */
    html {
        scroll-behavior: smooth;
    }
    body {
        font-family: 'Inter', sans-serif;
        color: #374151; /* text-gray-800 */
    }

    /* Hide Streamlit's default header and hamburger menu */
    .stApp > header {
        display: none;
    }

    /* Main content block adjustment */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 1200px;
        margin: auto;
    }

    /* Hero Section Styling */
    .hero-container {
        min-height: 90vh; /* Adjusted height */
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        text-align: center;
        background: linear-gradient(to bottom right, #eff6ff, #e0f2fe); /* Clean gradient background */
        border-radius: 1rem; /* Rounded corners */
        margin-bottom: 4rem; /* Space below hero section */
    }
    .hero-content {
        max-width: 48rem;
    }
    .profile-image {
        width: 10rem;
        height: 10rem;
        border-radius: 50%;
        margin: 0 auto 1.5rem auto;
        object-fit: cover;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        border: 4px solid white;
    }
    h1 {
        font-size: 3.75rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 1rem;
    }
    h2 {
        font-size: 1.875rem;
        color: #2563eb;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }
    
    /* Section Headers */
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        color: #111827;
        margin-top: 3rem;
        margin-bottom: 3rem;
    }

    /* Cards for Skills, Projects, and Contact */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border: 1px solid #e5e7eb; /* Add border to Streamlit containers */
        border-radius: 0.75rem;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 1rem;
    }
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"]:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }

    /* Project card specifics */
    .project-card h3 {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .project-card .tools-impact {
        font-size: 0.875rem;
        color: #4b5563;
    }
    .project-card .tools-impact span {
        font-weight: 600;
        color: #2563eb;
    }
    
    /* Contact Icon Styling */
    .contact-item-card i {
        font-size: 2.5rem;
        color: #3b82f6;
        margin-bottom: 0.75rem;
    }

    /* Footer Styling */
    .footer {
        background-color: #1f2937;
        color: white;
        text-align: center;
        padding: 2rem 1rem;
        margin-top: 4rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
with st.container():
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<div class='hero-content'>", unsafe_allow_html=True)
    
    st.image(
        "https://github.com/karinaskuy/PORTOFOLIO/blob/main/WhatsApp%20Image%202025-04-11%20at%2022.52.41.jpeg?raw=true",
        width=160,
        use_column_width=False
    )
    # Inject custom CSS class for profile image styling if needed
    st.markdown("<style>.stImage > img { border-radius: 50%; border: 4px solid white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }</style>", unsafe_allow_html=True)

    st.title("Karina Dyah Paramitha")
    st.subheader("Film Maker & Media Intelligence Analyst")
    st.markdown("_\"Turning stories into meaningful visuals.\"_")
    st.write("""
    Media Production student with interests in writing, photography, and video production. 
    Actively exploring media as a means of impactful storytelling. 
    I hope to continue learning and contributing to the Indonesian creative industry, especially film.
    """)
    st.link_button("Check My Projects", "#projects", use_container_width=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)


# --- Core Skills Section ---
st.markdown("<h2 class='section-title' id='skills'>Skills</h2>", unsafe_allow_html=True)

skills_data = {
    "Visual & Editing": [
        "Capcut", "DaVinci Resolve", "Wondershare Filmora", "Canva", 
        "Picsart", "Adobe Illustrator", "Adobe Photoshop", "Adobe Premiere Pro"
    ],
    "Writing & Storytelling": [
        "Copywriting", "Scriptwriting", "Narasi Visual"
    ],
    "Web & Media Tools": [
        "HTML/CSS dasar", "Figma", "Streamlit"
    ]
}

skill_cols = st.columns(3)
for i, (category, skills) in enumerate(skills_data.items()):
    with skill_cols[i]:
        with st.container(border=True):
            st.markdown(f"**{category}**")
            # Create a markdown list from the python list
            skills_md = "\n".join([f"- {skill}" for skill in skills])
            st.markdown(skills_md)


# --- Featured Projects Section ---
st.markdown("<h2 class='section-title' id='projects'>Projects</h2>", unsafe_allow_html=True)

projects_data = [
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210301.png?raw=true",
        "title": "AI-Powered Media Insights",
        "summary": "Elevating Content Strategy with Data.",
        "tools": "Streamlit, Plotly, Gemini, GitHub",
        "impact": "Mengubah data mentah menjadi insight yang bisa ditindaklanjuti.",
        "demo_link": "https://intelmedia3.streamlit.app/",
        "github_link": "https://github.com/karinaskuy/intelmedia"
    },
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210145.png?raw=true",
        "title": "Suara Kanal Timur",
        "summary": "Film dokumenter tentang Dea, seorang streamer TikTok di sekitar Banjir Kanal Timur.",
        "tools": "Kamera, Teamwork Produksi",
        "impact": "Sebagai Camera Person dalam tugas Produksi Film Dokumenter.",
        "demo_link": "https://drive.google.com/file/d/1WP0UK-DHdIn9UBnVm12FrU-a4p49Uz0e/view",
        "github_link": None
    },
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210332.png?raw=true",
        "title": "Masyarakat Cerdas Sadar Arsip",
        "summary": "Dokumentasi program pengabdian masyarakat di Pulau Untung Jawa.",
        "tools": "Kamera, Adobe Premiere Pro",
        "impact": "Bertugas sebagai Creative Media & PIC.",
        "demo_link": "https://youtu.be/cVCKa10bGYU?si=13rZ8tnOB8SAICmn",
        "github_link": None
    },
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20205949.png?raw=true",
        "title": "Analisis Video Iklan Gojek",
        "summary": "Analisis campaign Gojek menggunakan AI untuk mengevaluasi visual dan pesan.",
        "tools": "Gemini, ChatGPT, Google AI Studio",
        "impact": "Memperdalam pemahaman strategi branding digital dengan AI.",
        "demo_link": "https://www.canva.com/design/DAGi-r7RAy4/YW_4_iyj9o9tNx9tSTwVrw/edit",
        "github_link": None
    },
]

# Display projects in a grid
cols_per_row = 2
for i in range(0, len(projects_data), cols_per_row):
    project_row_cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(projects_data):
            project = projects_data[i + j]
            with project_row_cols[j]:
                # GANTI: Menggunakan st.container(border=True) untuk card yang lebih bersih
                with st.container(border=True):
                    # FIX: Menggunakan use_container_width=True
                    st.image(project["img"], use_container_width=True)
                    st.subheader(project['title'])
                    st.write(project['summary'])
                    st.markdown(f"**Tools:** {project['tools']}")
                    st.markdown(f"**Dampak:** {project['impact']}")

                    # Buttons in columns for alignment
                    btn_cols = st.columns(2)
                    if project["demo_link"]:
                        btn_cols[0].link_button("Demo Live", project["demo_link"], use_container_width=True)
                    if project["github_link"]:
                        btn_cols[1].link_button("GitHub", project["github_link"], use_container_width=True, type="secondary")


# --- Contact Me Section ---
st.markdown("<h2 class='section-title' id='contact'>Hubungi Saya</h2>", unsafe_allow_html=True)
st.info("Tertarik untuk berkolaborasi atau ingin mengetahui lebih lanjut? Jangan ragu untuk menghubungi saya.", icon="✉️")

contact_info = [
    {"icon": "fa-envelope", "text": "Email", "link": "mailto:karinadyah125@gmail.com"},
    {"icon": "fa-linkedin", "text": "LinkedIn", "link": "https://www.linkedin.com/in/karina-dyah-paramitha-b706b4288/"},
    {"icon": "fa-github", "text": "GitHub", "link": "https://github.com/karinaskuy"}
]

contact_cols = st.columns(3)
for i, contact in enumerate(contact_info):
    with contact_cols[i]:
        with st.container(border=True):
            st.markdown(f"<div style='text-align: center;'><a href='{contact['link']}' target='_blank' style='text-decoration: none; color: inherit;'><i class='fas {contact['icon']}' style='font-size: 2.5rem; color: #3b82f6;'></i><p style='font-weight: 600; margin-top: 0.5rem;'>{contact['text']}</p></a></div>", unsafe_allow_html=True)


# --- Footer ---
st.markdown("---")
st.markdown("<div class='footer'><p>© 2025 Karina Dyah Paramitha. All rights reserved.</p></div>", unsafe_allow_html=True)
