# Mengapa IndoBERT Tidak Perlu Stopword Removal, Stemming, dan Tokenisasi Manual?

## 1. WordPiece Tokenizer Bawaan

IndoBERT menggunakan **WordPiece Tokenizer** bawaan dari arsitektur Transformer. Tokenizer ini memecah kata menjadi sub-kata (*subword*), misalnya:

- `"menyelesaikan"` → `["menye", "##lesaikan"]`
- `"permainan"` → `["permainan"]`

Dengan pendekatan ini, IndoBERT tidak memerlukan tokenisasi manual karena seluruh proses tokenisasi sudah ditangani secara otomatis oleh tokenizer.

## 2. Stopword Removal Menghilangkan Konteks

Berbeda dengan pendekatan ML tradisional (TF-IDF + SVM), model Transformer seperti IndoBERT memanfaatkan **attention mechanism** yang menangkap hubungan kontekstual antar kata. Stopword seperti *"di"*, *"ke"*, *"dan"*, *"yang"* justru memberikan informasi penting terkait struktur kalimat dan hubungan antar entitas.

Contoh:
- *"berita **di** detik"* vs *"berita **dari** detik"* — makna berbeda karena preposisi.
- Menghapus stopword akan menghilangkan nuansa konteks ini.

## 3. Stemming Merusak Informasi Linguistik

IndoBERT dilatih pada korpus bahasa Indonesia dengan **kata utuh** (bukan bentuk akar kata). Stemming akan merusak representasi semantik karena:

- Bentuk imbuhan (prefiks, sufiks, konfiks) membawa makna gramatikal.
- Subword tokenizer sudah mampu menangani variasi morfologis tanpa perlu di-stem.

## 4. Model Memahami Konteks Secara Utuh

IndoBERT adalah model **bidirectional** yang melihat konteks kalimat dari kiri dan kanan secara simultan. Seluruh kalimat dipertahankan agar model dapat memahami makna secara utuh — berbeda dengan pendekatan *bag-of-words* yang hanya melihat frekuensi kemunculan kata.

## 5. Perbandingan dengan Pendekatan Tradisional

| Aspek | TF-IDF + SVM (Tradisional) | IndoBERT (Transformer) |
|-------|---------------------------|----------------------|
| Tokenisasi | Manual (NLTK, dll.) | Otomatis (WordPiece Tokenizer) |
| Stopword Removal | Wajib (mengurangi noise) | Tidak perlu (konteks penting) |
| Stemming/Lemmatization | Wajib (mereduksi dimensi) | Tidak perlu (subword coverage) |
| Representasi Teks | Sparse vector (BoW) | Dense embedding (kontekstual) |

## Kesimpulan

IndoBERT tidak memerlukan stopword removal, stemming, tokenisasi manual, atau lemmatization karena:

1. **Tokenizer bawaan** menangani pemecahan teks secara otomatis.
2. **Attention mechanism** memanfaatkan seluruh kata termasuk stopword sebagai sinyal konteks.
3. **Subword tokenization** sudah mengakomodasi variasi morfologis kata.
4. **Struktur kalimat utuh** diperlukan agar model memahami makna secara kontekstual.

Pada notebook ini, pembersihan teks hanya dibatasi pada: *case folding*, penghapusan URL, tag HTML, dan whitespace berlebih — tanpa menyentuh aspek linguistik yang diperlukan oleh model.
