# Backend - API & Machine Learning Server

Backend Batik MaduraKu adalah API yang membantu model untuk meelakukan klasifikasi Batik Madura vs Batik Luar Madura menggunakan framework Flask.

## Fitur

- Prediksi citra batik: Madura vs Non-Madura
- Terintegrasi dengan MongoDB Atlas untuk penyimpanan log prediksi
- Endpoint REST API siap untuk diakses oleh frontend
- Model diambil langsung dari URL (.keras)

## Teknologi

- Python 3.10+
- Flask
- Gunicorn
- TensorFlow / Keras
- MongoDB Atlas

## Instalasi Lokal

1. Clone repository:
    ```bash
    git clone <repo-url>
    cd <repo-folder>
    ```

2. Buat environment dan install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Siapkan file `.env`:
    ```env
    MODEL_URL=https://storage.googleapis.com/your-bucket/your-model.keras
    MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
    ```

4. Jalankan server:
    ```bash
    python run.py
    ```

## Endpoint

- `POST /predict`
  - Deskripsi: Menerima file gambar dan mengembalikan hasil prediksi klasifikasi batik.
  - Form-data:
    - `image`: file gambar `.jpg` atau `.png`
  - Response:
    ```json
    {
      "confidence": 0.94,
      "prediction": "Batik Luar Madura",
      "suggestion": "Ini adalah batik yang berasal dari luar Madura.",
      "timestamp": "13 Mei 2025 22:03 WIB"
    }
    ```
    
- `GET /predicts`
  - Deskripsi: Menampilkan semua riwayat hasil prediksi.
  - Form-data:
    - `image`: file gambar `.jpg` atau `.png`
  - Response:
    ```json
    {
      "_id": "682319d4c7bxxxxxxxxxx",
        "confidence": 0.999961256980896,
        "filename": "batik sampang.jpeg",
        "result": "Batik Madura",
        "suggestion": "Ini adalah batik yang berasal dari Madura.",
        "timestamp": "13 Mei 2025 17:07 WIB"
    }
    ```


---

