# Frontend - Klasifikasi Batik

Frontend Batik MaduraKu adalah implementasi UI/UX untuk website klasifikasi Batik Madura berbasis HTML, CSS, dan JavaScript (Vanilla JS).

## Fitur

- Upload gambar batik
- Preview hasil klasifikasi: Batik Madura atau Luar-Madura
- Tampilkan confidence dari model
- Terhubung langsung ke REST API dari backend Flask

## Teknologi

- HTML5
- CSS3
- JavaScript (Fetch API)
- Bootstrap (jika digunakan)

## Instalasi Lokal

1. Clone repository:
    ```bash
    git clone <repo-url>
    cd <repo-folder>
    git checkout FE
    ```

2. Jalankan menggunakan live server (misal dengan VSCode Live Server Extension) atau:
    ```bash
    python -m http.server 5500
    ```

3. Pastikan endpoint di `main.js` mengarah ke Cloud Run:
    ```javascript
    const API_URL = "https://batik-backend-xxxx.a.run.app/predict";
    ```

Pastikan `API_URL` diubah sesuai dengan URL backend kamu.

---

