import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Karina Dyah Paramitha - Portfolio",
    page_icon="✨",
    layout="wide", # Use wide layout for better use of space
    initial_sidebar_state="collapsed" # Hide sidebar by default
)

# --- Custom CSS for basic styling (mimicking Tailwind where possible) ---
# This uses st.markdown with unsafe_allow_html=True to inject custom CSS.
# It helps to achieve a look similar to the original HTML with Tailwind.
st.markdown("""
<style>
    /* General body font and scroll behavior */
    html {
        scroll-behavior: smooth; /* Smooth scrolling for navigation links */
    }
    body {
        font-family: 'Inter', sans-serif;
        color: #374151; /* text-gray-800 */
        background-color: #ffffff; /* bg-white */
    }

    /* Custom scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1; /* Soft gray */
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8; /* Darker gray on hover */
    }

    /* Streamlit's main content block adjustment */
    .stApp > header {
        display: none; /* Hide Streamlit's default header */
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 1200px; /* Max width similar to HTML's max-w-6xl */
        margin-left: auto;
        margin-right: auto;
    }

    /* Hero Section Styling */
    .hero-container {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem; /* p-4 */
        text-align: center;
        background: linear-gradient(to bottom right, #eff6ff, #e0f2fe); /* from-blue-50 to-blue-100 */
        background-image: url('https://github.com/karinaskuy/PORTOFOLIO/blob/main/916b4bd44f429ba9d69e3976d778ae2d.jpg'); /* Placeholder background */
        background-size: cover;
        background-position: center;
    }
    .hero-content {
        background-color: rgba(255, 255, 255, 0.9); /* bg-white bg-opacity-90 */
        padding: 2.5rem; /* p-10 */
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1); /* shadow-2xl */
        max-width: 48rem; /* max-w-4xl */
        margin: auto;
    }
    .profile-image {
        width: 10rem; /* md:w-40 */
        height: 10rem; /* md:h-40 */
        border-radius: 9999px; /* rounded-full */
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1.5rem; /* mb-6 */
        object-fit: cover;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-lg */
        border: 4px solid #bfdbfe; /* border-blue-200 */
    }
    .hero-title {
        font-size: 3.75rem; /* text-6xl */
        font-weight: 700; /* font-bold */
        color: #111827; /* text-gray-900 */
        margin-bottom: 1rem; /* mb-4 */
        letter-spacing: -0.025em; /* tracking-tight */
    }
    .hero-subtitle {
        font-size: 1.875rem; /* text-3xl */
        color: #2563eb; /* text-blue-600 */
        font-weight: 600; /* font-semibold */
        margin-bottom: 0.75rem; /* mb-3 */
    }
    .hero-slogan {
        font-size: 1.25rem; /* text-xl */
        color: #4b5563; /* text-gray-700 */
        margin-bottom: 1.5rem; /* mb-6 */
        line-height: 1.625; /* leading-relaxed */
    }
    .hero-intro {
        font-size: 1.125rem; /* text-lg */
        color: #4b5563; /* text-gray-600 */
        margin-bottom: 2rem; /* mb-8 */
        max-width: 42rem; /* max-w-2xl */
        margin-left: auto;
        margin-right: auto;
    }
    .stLinkButton > a {
        display: inline-block;
        background-color: #2563eb; /* bg-blue-600 */
        color: white;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 9999px; /* rounded-full */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-lg */
        transition: all 0.3s ease-in-out;
        text-decoration: none;
    }
    .stLinkButton > a:hover {
        background-color: #1d4ed8; /* hover:bg-blue-700 */
        transform: scale(1.05); /* hover:scale-105 */
    }

    /* Section Headers */
    .section-title {
        font-size: 2.25rem; /* text-4xl */
        font-weight: 700; /* font-bold */
        text-align: center;
        color: #111827; /* text-gray-900 */
        margin-bottom: 3rem; /* mb-12 */
    }

    /* Skills Section Styling */
    .skills-section {
        padding-top: 4rem; /* py-16 */
        padding-bottom: 4rem; /* py-16 */
        background-color: #f9fafb; /* bg-gray-50 */
    }
    .skill-card {
        background-color: white;
        padding: 1.5rem; /* p-6 */
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-lg */
        border: 1px solid #bfdbfe; /* border-blue-100 */
        margin-bottom: 1.5rem; /* for responsiveness */
    }
    .skill-card h3 {
        font-size: 1.5rem; /* text-2xl */
        font-weight: 600; /* font-semibold */
        color: #1d4ed8; /* text-blue-700 */
        margin-bottom: 1rem; /* mb-4 */
        display: flex;
        align-items: center;
    }
    .skill-card i {
        color: #3b82f6; /* text-blue-500 */
        margin-right: 0.75rem; /* mr-3 */
    }
    .skill-card ul {
        list-style: disc;
        padding-left: 1.25rem; /* list-inside */
        color: #4b5563; /* text-gray-700 */
    }
    .skill-card li {
        margin-bottom: 0.5rem;
    }

    /* Projects Section Styling */
    .projects-section {
        padding-top: 4rem;
        padding-bottom: 4rem;
        background-color: #eff6ff; /* bg-blue-50 */
    }
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        margin-bottom: 1.5rem; /* For spacing between cards */
    }
    .project-card:hover {
        transform: scale(1.02); /* Slightly reduced scale for Streamlit responsiveness */
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }
    .project-card img {
        width: 100%;
        height: 12rem; /* h-48 */
        object-fit: cover;
        border-radius: 0.5rem; /* rounded-lg */
        margin-bottom: 1rem; /* mb-4 */
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06); /* shadow */
    }
    .project-card h3 {
        font-size: 1.5rem; /* text-2xl */
        font-weight: 600;
        color: #111827; /* text-gray-900 */
        margin-bottom: 0.5rem; /* mb-2 */
    }
    .project-card p {
        color: #4b5563; /* text-gray-700 */
        font-size: 0.875rem; /* text-sm */
        margin-bottom: 0.75rem; /* mb-3 */
    }
    .project-card .tools-impact span {
        font-weight: 500; /* font-medium */
        color: #2563eb; /* text-blue-600 */
    }
    .project-buttons a {
        display: inline-flex; /* flex items-center */
        align-items: center;
        gap: 0.5rem; /* space-x-2 */
        font-size: 0.875rem; /* text-sm */
        padding: 0.5rem 1rem; /* py-2 px-4 */
        border-radius: 9999px; /* rounded-full */
        transition: background-color 0.2s ease;
        text-decoration: none;
    }
    .project-buttons .demo-live {
        background-color: #3b82f6; /* bg-blue-500 */
        color: white;
    }
    .project-buttons .demo-live:hover {
        background-color: #2563eb; /* hover:bg-blue-600 */
    }
    .project-buttons .github {
        background-color: #4b5563; /* bg-gray-700 */
        color: white;
    }
    .project-buttons .github:hover {
        background-color: #1f2937; /* hover:bg-gray-800 */
    }

    /* Contact Section Styling */
    .contact-section {
        padding-top: 4rem;
        padding-bottom: 4rem;
        background-color: #f3f4f6; /* bg-gray-100 */
    }
    .contact-intro {
        font-size: 1.125rem; /* text-lg */
        color: #4b5563; /* text-gray-700 */
        margin-bottom: 2rem; /* mb-8 */
        max-width: 42rem; /* max-w-2xl */
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }
    .contact-item-card {
        background-color: white;
        padding: 1rem; /* p-4 */
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-md */
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .contact-item-card a {
        color: #2563eb; /* text-blue-600 */
        transition: color 0.3s ease;
        text-decoration: none;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .contact-item-card a:hover {
        color: #1e40af; /* hover:text-blue-800 */
    }
    .contact-item-card i {
        font-size: 3rem; /* text-5xl */
        margin-bottom: 0.75rem; /* mb-3 */
    }
    .contact-item-card span {
        font-size: 1.25rem; /* text-xl */
        font-weight: 500; /* font-medium */
        display: block;
    }

    /* Footer Styling */
    .footer {
        background-color: #1f2937; /* bg-gray-800 */
        color: white;
        text-align: center;
        padding: 1.5rem 1rem; /* py-6 px-4 */
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
# Use st.container for a div-like structure for the hero section background
with st.container():
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<div class='hero-content'>", unsafe_allow_html=True)

    # Profile Image
    st.markdown(
        f"<img src='https://github.com/karinaskuy/PORTOFOLIO/blob/main/WhatsApp%20Image%202025-04-11%20at%2022.52.41.jpeg?raw=true' "
        f"alt='Karina Dyah Paramitha' class='profile-image'>",
        unsafe_allow_html=True
    )

    # Name and Role
    st.markdown("<h1 class='hero-title'>Karina Dyah Paramitha</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='hero-subtitle'>Film Maker & Media Intelligence Analyst</h2>", unsafe_allow_html=True)

    # Slogan and Introduction
    st.markdown("<p class='hero-slogan'>\"Turning stories into meaningful visuals.\"</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='hero-intro'>
        Media Production student with interests in writing, photography, and video production. Actively exploring media as a means of impactful storytelling. I hope to continue learning and contributing to the Indonesian creative industry, especially film.
    </p>
    """, unsafe_allow_html=True)

    # CTA Button
    # Use st.link_button for simplicity and Streamlit's native styling
    st.link_button("Check My Project", url="#projects")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Core Skills Section ---
st.markdown("<section class='skills-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' id='skills'>Skills</h2>", unsafe_allow_html=True)

skill_cols = st.columns(3) # Create 3 columns for skill categories

skills_data = {
    "Visual & Editing": [
        "Capcut", "DaVinci Resolve", "Wondershare Filmora",
        "Canva", "Picsart", "Adobe Illustrator",
        "Adobe Photoshop", "Adobe Premiere Pro"
    ],
    "Writing & Storytelling": [
        "Copywriting", "Scriptwriting", "Narasi Visual"
    ],
    "Web & Media Tools": [
        "HTML/CSS dasar", "Figma"
    ]
}

for i, (category, skills) in enumerate(skills_data.items()):
    with skill_cols[i]: # Place each skill card in its column
        st.markdown(f"<div class='skill-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3><i class='fas {('fa-eye' if category == 'Visual & Editing' else 'fa-book-open' if category == 'Writing & Storytelling' else 'fa-tools')}'></i> {category}</h3>", unsafe_allow_html=True)
        st.markdown("<ul>", unsafe_allow_html=True)
        for skill in skills:
            st.markdown(f"<li>{skill}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</section>", unsafe_allow_html=True)


# --- Featured Projects Section ---
st.markdown("<section class='projects-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' id='projects'>PROJECTS</h2>", unsafe_allow_html=True)

projects_data = [
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210301.png?raw=true",
        "title": "AI-Powered Media Insights",
        "summary": "Elevating Content Strategy with Data",
        "tools": "Streamlit, Plotly, Gemini, ChatGPT, GitHub, Streamlit Community Cloud",
        "impact": "Mengubah data mentah menjadi insight yang bisa ditindaklanjuti, yang secara langsung mempengaruhi strategi konten, optimasi kampanye, dan keputusan produksi",
        "demo_link": "https://intelmedia3.streamlit.app/",
        "github_link": "https://github.com/karinaskuy/intelmedia"
    },
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210145.png?raw=true",
        "title": "Suara Kanal Timur",
        "summary": "Film dokumenter tentang Dea, seorang streamer TikTok yang hidup di sekitar Banjir Kanal Timur.",
        "tools": "Kamera, teamwork produksi",
        "impact": "Sebagai camera person di proyek tugas mata kuliah Produksi Film Dokumenter.",
        "demo_link": "https://drive.google.com/file/d/1WP0UK-DHdIn9UBnVm12FrU-a4p49Uz0e/view",
        "github_link": None
    },
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210332.png?raw=true",
        "title": "Masyarakat Cerdas Sadar Arsip",
        "summary": "Dokumentasi program pengabdian masyarakat yang mengedukasi pentingnya kearsipan keluarga di Pulau Untung Jawa.",
        "tools": "Kamera, Adobe Premiere Pro",
        "impact": "Creative Media & PIC",
        "demo_link": "https://youtu.be/cVCKa10bGYU?si=13rZ8tnOB8SAICmn",
        "github_link": None
    },
    {
        "img": "https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20205949.png?raw=true",
        "title": "Analisis Video Iklan Gojek",
        "summary": "Analisis mendalam terhadap 3 video campaign Gojek menggunakan AI tools untuk mengevaluasi visual, audio, dan efektivitas pesan.",
        "tools": "Gemini, ChatGPT, Google AI Studio",
        "impact": "Disusun dalam presentasi kelompok dan memperdalam pemahaman strategi branding digital dengan AI.",
        "demo_link": "https://www.canva.com/design/DAGi-r7RAy4/YW_4_iyj9o9tNx9tSTwVrw/edit",
        "github_link": None
    },
]

# Display projects in a grid using Streamlit columns
cols_per_row = 2
for i in range(0, len(projects_data), cols_per_row):
    project_row_cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(projects_data): # Ensure we don't go out of bounds
            project = projects_data[i + j]
            with project_row_cols[j]:
                st.markdown(f"<div class='project-card'>", unsafe_allow_html=True)
                st.image(project["img"], caption="", use_column_width=True) # Streamlit handles image display
                st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p>{project['summary']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='tools-impact'><span>Tools:</span> {project['tools']}</p>", unsafe_allow_html=True)
                if project["impact"]: # Only show impact if it exists
                    st.markdown(f"<p class='tools-impact'><span>Dampak:</span> {project['impact']}</p>", unsafe_allow_html=True)

                # Buttons for Demo Live and GitHub
                st.markdown("<div class='project-buttons' style='display: flex; gap: 0.75rem; flex-wrap: wrap;'>", unsafe_allow_html=True)
                if project["demo_link"]:
                    st.markdown(f"<a href='{project['demo_link']}' target='_blank' class='demo-live'><i class='fas fa-play-circle'></i> Demo Live</a>", unsafe_allow_html=True)
                if project["github_link"]:
                    st.markdown(f"<a href='{project['github_link']}' target='_blank' class='github'><i class='fab fa-github'></i> GitHub</a>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</section>", unsafe_allow_html=True)

# --- Contact Me Section ---
st.markdown("<section class='contact-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' id='contact'>Hubungi Saya</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='contact-intro'>
    Tertarik untuk berkolaborasi atau ingin mengetahui lebih lanjut? Jangan ragu untuk menghubungi saya melalui kontak di bawah ini.
</p>
""", unsafe_allow_html=True)

contact_cols = st.columns(3) # Create 3 columns for contact info

contact_info = [
    {"icon": "fas fa-envelope", "text": "karinadyah125@gmail.com", "link": "mailto:karinadyah125@gmail.com"},
    {"icon": "fab fa-linkedin", "text": "LinkedIn", "link": "https://www.linkedin.com/in/karina-dyah-paramitha-b706b4288/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"},
    {"icon": "fab fa-github", "text": "GitHub", "link": "https://github.com/karinaskuy"}
]

for i, contact in enumerate(contact_info):
    with contact_cols[i]:
        st.markdown(f"<div class='contact-item-card'>", unsafe_allow_html=True)
        st.markdown(f"<a href='{contact['link']}' target='_blank'><i class='{contact['icon']}'></i><span>{contact['text']}</span></a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</section>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown("<p>&copy; 2025 Karina Dyah Paramitha. All rights reserved.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
