<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karina Dyah Paramitha - Portfolio</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts - Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <!-- AOS Library for scroll animations -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            scroll-behavior: smooth; /* Smooth scrolling for navigation */
        }
        /* Custom scrollbar for a cleaner look */
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
        .hero-bg {
            background-image: url('https://placehold.co/1920x1080/E0F2F7/334155?text=Background+Image'); /* Placeholder background */
            background-size: cover;
            background-position: center;
        }
    </style>
</head>
<body class="text-gray-800 bg-white">

    <!-- Hero Section -->
    <section id="hero" class="hero-bg min-h-screen flex items-center justify-center p-4 md:p-8 text-center bg-gradient-to-br from-blue-50 to-blue-100">
        <div class="max-w-4xl mx-auto bg-white bg-opacity-90 p-6 md:p-10 rounded-xl shadow-2xl" data-aos="fade-up">
            <!-- Profile Image Added Here -->
            <img src="https://content-storage-upload.googleapis.com/28d392b5-4191-41fa-b67e-d7f248691497" alt="Karina Dyah Paramitha" class="w-32 h-32 md:w-40 md:h-40 rounded-full mx-auto mb-6 object-cover shadow-lg border-4 border-blue-200">

            <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-4 tracking-tight">Karina Dyah Paramitha</h1>
            <h2 class="text-xl md:text-3xl text-blue-600 font-semibold mb-3">Film Maker & Media Intelligence Analyst</h2>
            <p class="text-md md:text-lg text-gray-600 mb-8 max-w-2xl mx-auto">
                Media Production student with interests in writing, photography, and video production. Actively exploring media as a means of impactful storytelling. I hope to continue learning and contributing to the Indonesian creative industry, especially film.
            </p>
            <a href="#projects" class="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-full shadow-lg transition duration-300 ease-in-out transform hover:scale-105">
                Check My Project
            </a>
        </div>
    </section>

    <!-- Core Skills Section -->
    <section id="skills" class="py-16 px-4 md:px-8 bg-gray-50">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl md:text-4xl font-bold text-center text-gray-900 mb-12" data-aos="fade-down">Skills</h2>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Visual & Editing -->
                <div class="bg-white p-6 rounded-xl shadow-lg border border-blue-100" data-aos="fade-right" data-aos-delay="100">
                    <h3 class="text-2xl font-semibold text-blue-700 mb-4 flex items-center">
                        <i class="fas fa-eye text-blue-500 mr-3"></i> Visual & Editing
                    </h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2">
                        <li>Capcut</li>
                        <li>DaVinci Resolve</li>
                        <li>Wondershare Filmora</li>
                        <li>Canva</li>
                        <li>Picsart</li>
                        <li>Adobe Illustrator</li>
                        <li>Adobe Photoshop</li>
                        <li>Adobe Premiere Pro</li>
                    </ul>
                </div>

                <!-- Writing & Storytelling -->
                <div class="bg-white p-6 rounded-xl shadow-lg border border-blue-100" data-aos="fade-up" data-aos-delay="200">
                    <h3 class="text-2xl font-semibold text-blue-700 mb-4 flex items-center">
                        <i class="fas fa-book-open text-blue-500 mr-3"></i> Writing & Storytelling
                    </h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2">
                        <li>Copywriting</li>
                        <li>Scriptwriting</li>
                        <li>Narasi Visual</li>
                    </ul>
                </div>

                <!-- Web & Media Tools -->
                <div class="bg-white p-6 rounded-xl shadow-lg border border-blue-100" data-aos="fade-left" data-aos-delay="300">
                    <h3 class="text-2xl font-semibold text-blue-700 mb-4 flex items-center">
                        <i class="fas fa-tools text-blue-500 mr-3"></i> Web & Media Tools
                    </h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2">
                        <li>HTML/CSS dasar</li>
                        <li>Figma</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Featured Projects Section -->
    <section id="projects" class="py-16 px-4 md:px-8 bg-blue-50">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl md:text-4xl font-bold text-center text-gray-900 mb-12" data-aos="fade-down">PROJECTS</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
                <!-- Project 1: AI-Powered Media Insights -->
                <div class="bg-white p-6 rounded-xl shadow-lg transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-xl" data-aos="fade-zoom-in" data-aos-delay="100">
                    <img src="https://placehold.co/600x400/E0F2F7/334155?text=AI+Media+Insights" alt="AI-Powered Media Insights" class="w-full h-48 object-cover rounded-lg mb-4 shadow">
                    <h3 class="text-2xl font-semibold text-gray-900 mb-2">AI-Powered Media Insights</h3>
                    <p class="text-gray-700 mb-3 text-sm">Elevating Content Strategy with Data</p>
                    <p class="text-gray-600 text-sm mb-3">
                        <span class="font-medium text-blue-600">Tools:</span> Streamlit, Plotly, Gemini, ChatGPT, GitHub, Streamlit Community Cloud
                    </p>
                    <p class="text-gray-600 text-sm mb-4">
                        <span class="font-medium text-blue-600">Tujuan:</span> Mengubah data mentah menjadi insight yang bisa ditindaklanjuti,
yang secara langsung mempengaruhi strategi konten, optimasi kampanye, dan
keputusan produksi
                    </p>
                    <div class="flex flex-wrap gap-3">
                        <a href="https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210301.png" alt="AI-Powered Media Insights" class="inline-block bg-blue-500 hover:bg-blue-600 text-white text-sm py-2 px-4 rounded-full transition duration-200">
                            <i class="fas fa-play-circle mr-2"></i> Demo Live
                        </a>
                        <a href="https://github.com/karinaskuy/intelmedia" target="_blank" class="inline-block bg-gray-700 hover:bg-gray-800 text-white text-sm py-2 px-4 rounded-full transition duration-200">
                            <i class="fab fa-github mr-2"></i> GitHub
                        </a>
                    </div>
                </div>

                <!-- Project 2: Suara Kanal Timur -->
                <div class="bg-white p-6 rounded-xl shadow-lg transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-xl" data-aos="fade-zoom-in" data-aos-delay="200">
                    <img src="https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210145.png" alt="Suara Kanal Timur" class="w-full h-48 object-cover rounded-lg mb-4 shadow">
                    <h3 class="text-2xl font-semibold text-gray-900 mb-2">Suara Kanal Timur</h3>
                    <p class="text-gray-700 mb-3 text-sm">Film dokumenter tentang Dea, seorang streamer TikTok yang hidup di sekitar Banjir Kanal Timur.</p>
                    <p class="text-gray-600 text-sm mb-3"><span class="font-medium text-blue-600">Tools:</span> Kamera, teamwork produksi</p>
                    <p class="text-gray-600 text-sm mb-4"><span class="font-medium text-blue-600">Role:</span> sebagai camera person di proyek tugas mata kuliah Produksi Film Dokumenter.</p>
                    <div class="flex flex-wrap gap-3">
                        <a href="https://drive.google.com/file/d/1WP0UK-DHdIn9UBnVm12FrU-a4p49Uz0e/view" target="_blank" class="bg-blue-500 hover:bg-blue-600 text-white text-sm py-2 px-4 rounded-full">Tonton Video</a>
                    </div>
                </div>

                <!-- Project 3: Masyarakat Cerdas Sadar Arsip -->
                <div class="bg-white p-6 rounded-xl shadow-lg transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-xl" data-aos="fade-zoom-in" data-aos-delay="300">
                    <img src="https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20210332.png" alt="Masyarakat Cerdas Sadar Arsip" class="w-full h-48 object-cover rounded-lg mb-4 shadow">
                    <h3 class="text-2xl font-semibold text-gray-900 mb-2">Masyarakat Cerdas Sadar Arsip</h3>
                    <p class="text-gray-700 mb-3 text-sm">Dokumentasi program pengabdian masyarakat yang mengedukasi pentingnya kearsipan keluarga di Pulau Untung Jawa.</p>
                    <p class="text-gray-600 text-sm mb-3"><span class="font-medium text-blue-600">Tools:</span> Kamera, Adobe Premiere Pro</p>
                    <p class="text-gray-600 text-sm mb-4"><span class="font-medium text-blue-600">Role:</span> Creative Media & PIC </p>
                    <div class="flex flex-wrap gap-3">
                        <a href="https://youtu.be/cVCKa10bGYU?si=13rZ8tnOB8SAICmn" target="_blank" class="bg-blue-500 hover:bg-blue-600 text-white text-sm py-2 px-4 rounded-full">Tonton Video</a>
                    </div>
                </div>

                <!-- Project 4: Analisis Video Iklan Gojek -->
                <div class="bg-white p-6 rounded-xl shadow-lg transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-xl" data-aos="fade-zoom-in" data-aos-delay="400">
                    <img src="https://github.com/karinaskuy/PORTOFOLIO/blob/main/Screenshot%202025-06-08%20205949.png" alt="Analisis Iklan Gojek" class="w-full h-48 object-cover rounded-lg mb-4 shadow">
                    <h3 class="text-2xl font-semibold text-gray-900 mb-2">Analisis Video Iklan Gojek</h3>
                    <p class="text-gray-700 mb-3 text-sm">Analisis mendalam terhadap 3 video campaign Gojek menggunakan AI tools untuk mengevaluasi visual, audio, dan efektivitas pesan.</p>
                    <p class="text-gray-600 text-sm mb-3"><span class="font-medium text-blue-600">Tools:</span> Gemini, ChatGPT, Google AI Studio</p>
                    <p class="text-gray-600 text-sm mb-4"><span class="font-medium text-blue-600">Dampak:</span> Disusun dalam presentasi kelompok dan memperdalam pemahaman strategi branding digital dengan AI.</p>
                    <div class="flex flex-wrap gap-3">
                        <a href="https://www.canva.com/design/DAGi-r7RAy4/YW_4_iyj9o9tNx9tSTwVrw/edit" target="_blank" class="bg-blue-500 hover:bg-blue-600 text-white text-sm py-2 px-4 rounded-full">Lihat Presentasi</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Me Section -->
    <section id="contact" class="py-16 px-4 md:px-8 bg-gray-100">
        <div class="max-w-4xl mx-auto text-center">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-12" data-aos="fade-down">Hubungi Saya</h2>
            <p class="text-lg text-gray-700 mb-8 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="100">
                Tertarik untuk berkolaborasi atau ingin mengetahui lebih lanjut? Jangan ragu untuk menghubungi saya melalui kontak di bawah ini.
            </p>

            <div class="flex flex-col md:flex-row justify-center items-center gap-8 md:gap-12">
                <!-- Email -->
                <div class="flex flex-col items-center p-4 rounded-xl bg-white shadow-md w-full md:w-auto" data-aos="fade-right" data-aos-delay="200">
                    <a href="mailto:karinadyah125@gmail.com" class="text-blue-600 hover:text-blue-800 transition duration-300">
                        <i class="fas fa-envelope text-5xl mb-3"></i>
                        <span class="block text-xl font-medium">karinadyah125@gmail.com</span>
                    </a>
                </div>

                <!-- LinkedIn -->
                <div class="flex flex-col items-center p-4 rounded-xl bg-white shadow-md w-full md:w-auto" data-aos="fade-up" data-aos-delay="300">
                    <a href="https://www.linkedin.com/in/karina-dyah-paramitha-b706b4288/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank" class="text-blue-600 hover:text-blue-800 transition duration-300">
                        <i class="fab fa-linkedin text-5xl mb-3"></i>
                        <span class="block text-xl font-medium">LinkedIn</span>
                    </a>
                </div>

                <!-- GitHub -->
                <div class="flex flex-col items-center p-4 rounded-xl bg-white shadow-md w-full md:w-auto" data-aos="fade-left" data-aos-delay="400">
                    <a href="https://github.com/karinaskuy" target="_blank" class="text-blue-600 hover:text-blue-800 transition duration-300">
                        <i class="fab fa-github text-5xl mb-3"></i>
                        <span class="block text-xl font-medium">GitHub</span>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-6 px-4">
        <p>&copy; 2025 Karina Dyah Paramitha. All rights reserved.</p>
    </footer>

    <!-- AOS Initialization -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 1000,
            once: true,
            mirror: false,
        });
    </script>
</body>
</html>
