KarirMind

judul di cv : Large Language Model–Powered Career Analytics Framework

Build. Fix. Price. Land. — The Complete AI Career Acceleration System

1. Membuat sebuah system yg bisa merekomendasikan pekerjaan apa saja yg cocok berdasarkan CV sang user
    - User mengupload file PDF yg berisi CV nya, lalu sistem akan berpikir untuk merekomendasikan pekerjaan-pekerjaan yg paling cocok untuk sang user.
    - sistem dibangun menggunakan Model Gemini

2. Membangun sebuah sistem yang dapat melakukan audit dan kritik mendalam terhadap CV sang user menggunakan Gemini Model
    - User mengupload CV yg bisa berbentuk [.pdf .txt .docx .jpg .png .jpeg .webp]
    - Sistem membaca isi CV tersebut dan melakukan evaluasi secara menyeluruh (section-by-section dan bullet-by-bullet).
    - Sistem mengidentifikasi kelemahan seperti kalimat yang vague, tidak terukur, kurang jelas, atau tidak berdampak.
    - Sistem memberikan rekomendasi perbaikan yang actionable dan diklasifikasikan berdasarkan tingkat keparahan (HIGH, MEDIUM, LOW).
    - Output dihasilkan dalam format terstruktur menggunakan schema Pydantic agar konsisten dan mudah diproses lebih lanjut.
    - Sistem dibangun menggunakan model Gemini (Gemma 3 27B) melalui integrasi LangChain.

3. Membangun sistem berbasis LLM yang mampu mengestimasi rentang gaji tahunan kandidat berdasarkan analisis isi resume.
    - User mengunggah file resume berbentuk [.pdf .txt .docx .jpg .png .jpeg .webp].
    - Model menganalisis pengalaman kerja, dampak bisnis, durasi pengalaman, serta kompleksitas skill untuk menentukan tingkat senioritas sebenarnya (Entry-Level, Mid-Level, Senior, Lead, dll).
    - Sistem mengestimasi rentang gaji tahunan dalam USD berdasarkan standar global remote / US tech market.
    - Sistem memberikan justifikasi yang jelas mengapa rentang tersebut sesuai dengan profil kandidat.
    - Sistem juga menghasilkan 3–5 strategi negosiasi gaji yang spesifik dan disesuaikan dengan kekuatan serta kelemahan dalam resume.
    - Model yang digunakan adalah Gemini LLM yang diarahkan untuk bertindak sebagai Expert Tech Recruiter dan Compensation Analyst.

4. Membangun sistem LLM yang merekomendasikan proyek portfolio terbaik berdasarkan target role dan resume yg diupload oleh user
    - User menentukan target posisi yang ingin dicapai (misalnya: Senior AI Engineer) dan mengupload file yg berisi resume kandidat
    - Sistem mengidentifikasi skill yang masih kurang atau belum terlihat kuat pada resume kandidat.
    - Model menghasilkan 2 proyek portfolio nyata berdasarkan problem bisnis di dunia ini
    - Model diarahkan untuk bertindak sebagai Expert Tech Lead dan Career Mentor dalam merancang proyek yang benar-benar meningkatkan peluang diterima kerja.


