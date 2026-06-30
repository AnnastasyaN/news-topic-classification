import streamlit as st

from src.predictor import predict_news

st.set_page_config(page_title="Klasifikasi Topik Berita", layout="centered")

st.markdown(
    """
    <style>
        :root {
            --card-bg: #ffffff;
            --card-border: #e2e8f0;
            --text-muted: #64748b;
            --text-primary: #1e3a5f;
            --text-accent: #2d6a9f;
            --footer-text: #94a3b8;
            --footer-border: #e2e8f0;
            --input-border: #d1d5db;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --card-bg: #1e1e2e;
                --card-border: #383850;
                --text-muted: #a0a0b8;
                --text-primary: #d0d0e0;
                --text-accent: #6ab0e8;
                --footer-text: #6a6a80;
                --footer-border: #383850;
                --input-border: #4a4a60;
            }
        }

        .result-card {
            background: var(--card-bg);
            padding: 1.5rem 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            border: 1px solid var(--card-border);
            border-left: 4px solid #2d6a9f;
            margin-top: 1.5rem;
        }

        .footer {
            text-align: center;
            padding: 2rem 0 0.5rem 0;
            color: var(--footer-text);
            font-size: 0.8rem;
            margin-top: 3rem;
            border-top: 1px solid var(--footer-border);
        }

        .stTextArea textarea {
            border-radius: 8px !important;
            border: 1px solid var(--input-border) !important;
        }
        .stTextArea textarea:focus {
            border-color: #2d6a9f !important;
            box-shadow: 0 0 0 2px rgba(45,106,159,0.15) !important;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #1e3a5f, #2d6a9f) !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 0.6rem 0 !important;
            border: none !important;
            border-radius: 8px !important;
            font-size: 1rem !important;
        }
        div.stButton > button:hover { opacity: 0.9 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### 📰 Info Aplikasi")
    st.markdown("---")
    st.markdown("**Model**")
    st.markdown("IndoBERT (indobenchmark/indobert-base-p1)")
    st.markdown("**Jumlah Kategori**")
    st.markdown("9 kelas")
    st.markdown("**Developer**")
    st.markdown("Annastasya Nabila Elsa Wulandari")

st.markdown(
    """
    <div style="background:linear-gradient(135deg,#1e3a5f,#2d6a9f);padding:1.5rem 2rem;border-radius:14px;text-align:center;color:white;margin-bottom:1.5rem;">
        <h1 style="font-size:1.8rem;font-weight:700;margin:0 0 0.3rem 0;">📰 Klasifikasi Topik Berita</h1>
        <p style="font-size:0.95rem;opacity:0.85;margin:0;">Prediksi kategori topik berita otomatis dengan IndoBERT</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### ✏️ Masukkan Judul Berita")
text = st.text_area(
    "",
    placeholder="Contoh: Timnas Indonesia menang telak atas Thailand",
    height=100,
    label_visibility="collapsed",
)

clicked = st.button("🔍 Predict Category", use_container_width=True)

if clicked:
    if not text or not text.strip():
        st.error("Silakan masukkan judul berita terlebih dahulu.")
    else:
        result = predict_news(text)
        cat = result["category"]
        conf = result["confidence"]
        st.markdown(
            f"""
            <div class="result-card">
                <h4 style="color:var(--text-muted);margin:0 0 0.5rem 0;font-size:0.8rem;text-transform:uppercase;letter-spacing:1px;">Hasil Prediksi</h4>
                <div style="font-size:1.6rem;font-weight:700;color:var(--text-primary);margin-bottom:0.75rem;">🏷️ {cat}</div>
                <h4 style="color:var(--text-muted);margin:0 0 0.25rem 0;font-size:0.8rem;text-transform:uppercase;letter-spacing:1px;">Confidence</h4>
                <div style="font-size:1.3rem;font-weight:700;color:var(--text-accent);">🎯 {conf}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer">
        Annastasya Nabila Elsa Wulandari &bull; IndoBERT Fine-Tuned &bull; 2026
    </div>
    """,
    unsafe_allow_html=True,
)
