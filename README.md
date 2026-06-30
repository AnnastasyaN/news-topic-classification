# News Topic Classification

Klasifikasi topik berita bahasa Indonesia menggunakan **IndoBERT** (*fine-tuning*) dengan perbandingan terhadap **TF-IDF + Linear SVM** sebagai model *baseline*.

Proyek ini merupakan tugas UAS mata kuliah **Natural Language Processing** — Program Studi Informatika, Universitas Pembangunan Nasional Veteran Jawa Timur (UPN Veteran Jatim) — 2026.

---

## 📌 Ringkasan Proyek

| Item | Detail |
|------|--------|
| **Tujuan** | Mengklasifikasikan judul berita ke dalam 9 kategori topik secara otomatis |
| **Dataset** | [Indonesian News Title](https://www.kaggle.com/datasets/ibamibrahim/indonesian-news-title) (91.017 sampel) |
| **Fitur** | Judul berita (teks) |
| **Target** | 9 kategori topik: `finance`, `food`, `health`, `hot`, `inet`, `news`, `oto`, `sport`, `travel` |
| **Model Utama** | IndoBERT (`indobenchmark/indobert-base-p1`) — fine-tuning |
| **Baseline** | TF-IDF + Linear SVM |
| **Deployment** | Streamlit (web app interaktif) |

### Dataset

Dataset **Indonesian News Title** berisi **91.017 sampel** judul berita dari portal detik.com. Setiap sampel terdiri dari teks judul dan label kategori. Dataset ini sudah dalam format bersih dan slap pakai.

Distribusi kelas cukup seimbang dengan 9 kategori. Detail eksperimen dan distribusi data tersedia di notebook eksperimen.

---

## 🧪 Hasil Evaluasi

| Metrik | TF-IDF + SVM | IndoBERT | Improvement |
|--------|-------------|----------|-------------|
| Accuracy | 82.08% | **90.68%** | +8.60% |
| Precision (Macro) | 79.84% | **88.94%** | +9.10% |
| Recall (Macro) | 75.99% | **88.59%** | +12.60% |
| F1-score (Macro) | 77.76% | **88.74%** | +10.98% |

IndoBERT menunjukkan performa unggul di seluruh metrik, dengan peningkatan signifikan pada **Recall (+12.60%)** dan **F1-score (+10.98%)**, menandakan kemampuan lebih baik dalam menangani kelas yang bervariasi.

---

## 🛠️ Struktur Proyek

```
├── app.py                           # Streamlit web app (frontend + backend ringan)
├── run.bat                          # Script untuk menjalankan app di Windows
├── requirements.txt                 # Dependensi Python
├── src/                             # Source code inti
│   ├── __init__.py
│   ├── config.py                    # Konfigurasi path & load model/tokenizer
│   ├── model_loader.py              # Load model, tokenizer, & label encoder
│   ├── predictor.py                 # Fungsi prediksi dengan pipeline lengkap
│   └── preprocessing.py             # Text cleaning (case folding, hapus URL/HTML, dll)
├── saved_model/                     # Model IndoBERT hasil fine-tuning (format safetensors)
│   ├── model.safetensors
│   ├── config.json
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── label_encoder.pkl
│   ├── best_model.pkl
│   └── training_args.bin
├── docs/                            # Dokumentasi tambahan
│   └── daftar-istilah-teknis.md     # Glosarium istilah NLP untuk referensi
├── mengapa-indobert-tidak-perlu-stopword-stemming.md
└── UAS_NLP_Implementasi_Fine_Tuning_IndoBERT_untuk_Klasifikasi_Topik_Berita_Bahasa_Indonesia.ipynb
```

---

## ⚙️ Instalasi & Menjalankan

### Prasyarat

- Python 3.10+
- pip (Python package manager)

### Langkah-langkah

1. **Clone repositori**
   ```bash
   git clone <repo-url>
   cd UAS_NLP_news-topic-classification
   ```

2. **(Opsional) Buat virtual environment**
   ```bash
   python -m venv .venv
   ```

   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependensi**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit**
   ```bash
   python -m streamlit run app.py
   ```

   Atau jalankan `run.bat` (khusus Windows).

Aplikasi akan terbuka di browser Anda (default: `http://localhost:8501`).

---

## 🚀 Penggunaan

1. Buka aplikasi Streamlit di browser.
2. Masukkan judul berita dalam bahasa Indonesia pada kolom teks (contoh: *"Timnas Indonesia menang telak atas Thailand"*).
3. Klik tombol **🔍 Predict Category**.
4. Sistem akan menampilkan:
   - **Kategori** hasil prediksi (salah satu dari 9 kelas)
   - **Confidence** (tingkat keyakinan model dalam persentase)

---

## 📚 Detail Teknis

### Preprocessing

Pipeline pemrosesan teks dirancang minimalis karena IndoBERT sudah memiliki kemampuan memahami konteks secara bawaan:

| Langkah | Deskripsi |
|---------|-----------|
| Handling missing values | None/NaN diubah menjadi string kosong |
| Case folding | Seluruh teks diubah ke *lowercase* |
| Hapus URL | Menghapus tautan `http://` dan `www.` |
| Hapus HTML tags | Menghapus tag seperti `<br>`, `<p>`, dll. |
| Normalisasi whitespace | Mengganti spasi berlebih dengan satu spasi |
| Strip whitespace | Menghapus spasi di awal/akhir teks |

**Tidak dilakukan** stopword removal maupun stemming — hal ini tidak diperlukan untuk IndoBERT (dan model transformer pada umumnya) karena arsitektur *self-attention* mampu memahami hubungan antar kata tanpa perlu filtrasi leksikal.

### Tokenisasi

Menggunakan **WordPiece Tokenizer** bawaan IndoBERT dengan parameter:
- `max_length = 64` (cukup untuk judul berita yang umumnya pendek)
- `truncation = True` (memotong teks yang melebihi panjang maksimal)
- `padding = True` (menyamakan panjang sekuens dalam satu *batch*)

### Model IndoBERT

- **Arsitektur**: BERT-base (~110M parameter) — 12 *encoder layers*, 12 *attention heads*, 768 *hidden size*
- **Base model**: `indobenchmark/indobert-base-p1` — pretrained pada bahasa Indonesia
- **Head**: Sequence classification head (9 output units sesuai jumlah kategori)

### Hyperparameter Training

| Parameter | Nilai |
|-----------|-------|
| Epoch | 3 |
| Learning rate | 2e-5 |
| Batch size | 16 |
| Optimizer | AdamW |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Scheduler | Linear decay |
| Loss function | Cross-entropy |
| Saving format | Safetensors (aman & efisien) |

### Baseline: TF-IDF + Linear SVM

Sebagai model pembanding, digunakan pipeline:
- **TF-IDF Vectorizer**: Mengubah teks menjadi matriks numerik berdasarkan frekuensi kata yang dibobot dengan *inverse document frequency*
- **Linear SVM**: *Support Vector Machine* dengan kernel linear sebagai *classifier*

---

## 🧠 Arsitektur Pipeline

```
Input Text
    │
    ▼
Preprocessing (cleaning)
    │
    ├──► IndoBERT Tokenizer → IndoBERT Model → Softmax → Prediksi
    │
    └──► (Alternatif) TF-IDF → Linear SVM → Prediksi
```

---

## 👩‍💻 Developer

**Annastasya Nabila Elsa Wulandari**  
UAS Natural Language Processing — 2026  
Program Studi Informatika  
Universitas Pembangunan Nasional Veteran Jawa Timur

---

## 📖 Referensi

- [Indonesian News Title Dataset (Kaggle)](https://www.kaggle.com/datasets/ibamibrahim/indonesian-news-title)
- [IndoBERT: indobenchmark/indobert-base-p1 (Hugging Face)](https://huggingface.co/indobenchmark/indobert-base-p1)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Scikit-learn: SVM & TF-IDF](https://scikit-learn.org/)
