import streamlit as st
import time

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Lab Kimia Organik Virtual",
    page_icon="🧪",
    layout="wide"
)

# Kustomisasi CSS untuk Animasi Teks Terima Kasih
st.markdown("""
<style>
@keyframes pulse {
    0% { transform: scale(1); color: #ff4b4b; }
    50% { transform: scale(1.05); color: #1f77b4; }
    100% { transform: scale(1); color: #ff4b4b; }
}
.animated-thankyou {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    animation: pulse 2s infinite;
    padding: 20px;
    border-radius: 10px;
    background-color: #f0f2f6;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# Definisikan Data Pengujian Kimia Organik
data_uji = {
    "Hidrokarbon 🛢️": {
        "Uji Bromin ($Br_2/CCl_4$)": {
            "tujuan": "Mendeteksi adanya ikatan rangkap dua atau tiga (ketidakjenuhan) pada hidrokarbon.",
            "sifat": "Reaksi adisi halogen pada ikatan rangkap tanpa menghasilkan gas sampingan.",
            "kejadian": "Larutan bromin yang berwarna cokelat kemerahan diteteskan ke dalam sampel hidrokarbon alkana dan alkena.",
            "warna": "Pada alkena/alkuna warna cokelat merah **cepat memudar (jernih)**. Pada alkana warna tetap cokelat merah (kecuali ada cahaya UV).",
            "reaksi": "$$R-CH=CH-R + Br_2 \\rightarrow R-CH(Br)-CH(Br)-R$$",
            "gagal": "Reaksi gagal memudar pada senyawa jenuh (alkana), atau reagen bromin sudah terurai karena terlalu lama disimpan di tempat terang."
        },
        "Uji Baeyer ($KMnO_4$)": {
            "tujuan": "Mengidentifikasi ikatan rangkap alifatik tak jenuh.",
            "sifat": "Oksidasi ringan oleh reduktor kuat dalam suasana netral atau basa.",
            "kejadian": "Penambahan larutan kalium permanganat ungu ke dalam senyawa tak jenuh.",
            "warna": "Warna ungu $KMnO_4$ **hilang** dan terbentuk **endapan cokelat** ($MnO_2$).",
            "reaksi": "$$3R-CH=CH-R + 2KMnO_4 + 4H_2O \\rightarrow 3R-CH(OH)-CH(OH)-R + 2MnO_2\\downarrow + 2KOH$$",
            "gagal": "Warna ungu tidak hilang jika sampel adalah alkana atau aromatik stabil (seperti benzena)."
        }
    },
    "Protein 🧬": {
        "Uji Biuret": {
            "tujuan": "Mendeteksi keberadaan ikatan peptida dalam suatu zat.",
            "sifat": "Pembentukan senyawa kompleks koordinasi antara ion tembaga dengan nitrogen peptida.",
            "kejadian": "Larutan protein dicampur $NaOH$ kemudian ditetesi $CuSO_4$ encer.",
            "warna": "Perubahan warna larutan menjadi **ungu atau violet**.",
            "reaksi": "$$\\text{Protein} + Cu^{2+} + OH^- \\rightarrow \\text{Kompleks Koordinasi Biuret (Warna Ungu)}$$",
            "gagal": "Warna tetap biru muda. Gagal jika sampel hanya berupa asam amino tunggal (kecuali histidin) karena tidak memiliki ikatan peptida minimun minimal dua."
        },
        "Uji Xantoproteat": {
            "tujuan": "Mengidentifikasi asam amino yang memiliki cincin benzena (seperti tirosin, triptofan, fenilalanin).",
            "sifat": "Reaksi nitrasi pada inti benzena oleh asam nitrat pekat.",
            "kejabin": "Sampel dipanaskan bersama $HNO_3$ pekat, lalu didinginkan dan ditambahkan basa ($NaOH$/$NH_4OH$).",
            "warna": "Terbentuk **endapan/larutan kuning**, yang berubah menjadi **jingga** setelah ditambah basa.",
            "reaksi": "$$\\text{Cincin Benzena (Protein)} + HNO_3 \\xrightarrow{\\Delta} \\text{Turunan Nitro (Kuning)} \\xrightarrow{NaOH} \\text{Garam Nitro (Jingga)}$$",
            "gagal": "Warna tidak berubah jingga jika protein tidak mengandung gugus asam amino aromatik."
        }
    },
    "Asam Karboksilat 🍋": {
        "Uji Natrium Bikarbonat ($NaHCO_3$)": {
            "tujuan": "Menguji sifat keasaman relatif senyawa organik (membedakan asam karboksilat dengan fenol).",
            "sifat": "Reaksi asam-basa yang menghasilkan gas karbon dioksida.",
            "kejadian": "Sampel direaksikan dengan larutan $NaHCO_3$ 5%.",
            "warna": "Larutan tetap jernih, namun terlihat fasa gas yang aktif.",
            "reaksi": "$$R-COOH + NaHCO_3 \\rightarrow R-COONa + H_2O + CO_2\\uparrow$$",
            "gagal": "Tidak ada gelembung gas ($CO_2$). Gagal terjadi jika tingkat keasaman senyawa terlalu lemah ($pK_a > 7$) seperti pada alkohol biasa."
        },
        "Uji Esterifikasi": {
            "tujuan": "Mengidentifikasi gugus karboksilat melalui pembentukan senyawa ester berbau khas.",
            "sifat": "Reaksi kondensasi reversibel pelepasan air dengan bantuan katalis asam.",
            "kejadian": "Asam karboksilat dipanaskan bersama alkohol (misal etanol) dan beberapa tetes $H_2SO_4$ pekat.",
            "warna": "Tidak ada perubahan warna signifikan, terbentuk lapisan minyak tipis di permukaan air.",
            "reaksi": "$$R-COOH + R'-OH \\xrightarrow{H_2SO_4, \\Delta} R-COOR' + H_2O$$",
            "gagal": "Tidak tercium aroma buah (ester). Gagal karena pemanasan kurang lama, atau hilangnya katalis asam pekat yang berfungsi mengikat air."
        }
    },
    "Minyak dan Lemak 🧈": {
        "Uji Akrolein": {
            "tujuan": "Mendeteksi keberadaan gliserol atau lemak/minyak yang mengandung gliserol.",
            "sifat": "Dehidrasi gliserol oleh agen pendehidrasi pada suhu tinggi.",
            "kejadian": "Sampel dipanaskan kuat bersama agen pendehidrasi seperti $KHSO_4$ jenuh.",
            "warna": "Asap putih terbentuk disertai bau menusuk hidung yang sangat tajam (akrolein).",
            "reaksi": "$$\\text{Gliserol} \\xrightarrow{KHSO_4, \\Delta} \\text{Akrolein } (CH_2=CH-CHO) + 2H_2O$$",
            "gagal": "Tidak menghasilkan bau menusuk. Gagal jika sampel berupa minyak mineral/lilin hidrokarbon buatan yang tidak berbasis trigliserida."
        },
        "Uji Ketidakjenuhan Lemak": {
            "tujuan": "Membedakan lemak jenuh (padat/hewani) dan lemak tak jenuh (cair/nabati).",
            "sifat": "Adisi iodium/bromin pada asam lemak rantai karbon.",
            "kejadian": "Minyak ditetesi larutan iodium atau Hubl.",
            "warna": "Warna iodium **hilang/pudar** pada minyak nabati, namun **tetap berwarna** pada lemak jenuh.",
            "reaksi": "$$\\text{Asam Lemak Tak Jenuh} + I_2 \\rightarrow \\text{Senyawa Di-iodo Jenuh}$$",
            "gagal": "Warna merah iodium tidak hilang jika reagen terlalu pekat atau minyak sudah tengik (mengalami otooksidasi)."
        }
    },
    "Karbohidrat 🌾": {
        "Uji Molisch": {
            "tujuan": "Uji umum untuk mendeteksi keberadaan segala jenis karbohidrat.",
            "sifat": "Dehidrasi karbohidrat oleh asam pekat membentuk furfural yang berkondensasi dengan alfa-naftol.",
            "kejadian": "Larutan karbohidrat dicampur reagen Molisch, lalu dialirkan $H_2SO_4$ pekat lewat dinding tabung.",
            "warna": "Terbentuk **cincin berwarna ungu** di perbatasan kedua lapisan cairan.",
            "reaksi": "$$\\text{Heksosa} \\xrightarrow{H_2SO_4} \\text{Hidroksimetilfurfural} \\xrightarrow{\\alpha\\text{-naftol}} \\text{Kompleks Ungu}$$",
            "gagal": "Cincin ungu tidak terbentuk. Gagal jika penambahan asam sulfat terlalu cepat (mengocok tabung terlalu kuat) sehingga memicu pembakaran arang/karbon hitam."
        },
        "Uji Benedict": {
            "tujuan": "Mendeteksi keberadaan gula pereduksi (glukosa, fruktosa, maltosa, laktosa).",
            "sifat": "Reduksi ion $Cu^{2+}$ menjadi $Cu^+$ dalam suasana basa lemah sitrat.",
            "kejadian": "Sampel dicampur reagen Benedict lalu dipanaskan dalam penangas air mendidih selama 5 menit.",
            "warna": "Perubahan warna dari biru menjadi hijau, kuning, hingga terbentuk **endapan merah bata** ($Cu_2O$).",
            "reaksi": "$$R-CHO + 2Cu^{2+} (basa) + 2H_2O \\rightarrow R-COOH + Cu_2O\\downarrow + 4H^+$$",
            "gagal": "Warna tetap biru jernih (misal pada sukrosa atau amilum) karena tidak memiliki gugus aldehid/keton bebas yang dapat berikatan."
        }
    }
}

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.header("🔬 Navigasi Menu")
    
    # Tambahkan opsi Halaman Utama / Keluar
    menu_options = ["🏠 Halaman Utama"] + list(data_uji.keys()) + ["🚪 Keluar Aplikasi"]
    pilihan_halaman = st.radio("Pilih Bab Percobaan:", menu_options)
    
    st.divider()
    st.caption("Aplikasi Lab Kimia Organik Virtual © 2026")

# --- KONTEN HALAMAN UTAMA ---
if pilihan_halaman == "🏠 Halaman Utama":
    st.title("🧪 Laboratorium Virtual Kimia Organik")
    st.subheader("Selamat datang di platform simulasi praktikum kimia karbon.")
    st.write(
        "Silakan pilih **Bab Percobaan** pada menu di sebelah kiri untuk melihat detail prosedur "
        "analisis kualitatif, sifat fisik, visualisasi warna hasil, persamaan reaksi, hingga analisis kegagalan uji."
    )
    
    # Tampilkan ringkasan ringkas materi
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Tips Praktikum:** Pastikan reagen yang digunakan segar dan amati instruksi pemanasan tabung dengan saksama.")
    with col2:
        st.warning("**Aspek Keamanan:** Gunakan ruang asam saat mereaksikan asam nitrat pekat ($HNO_3$) dan asam sulfat ($H_2SO_4$).")

# --- KONTEN HALAMAN KELUAR (ANIMASI TERIMA KASIH) ---
elif pilihan_halaman == "🚪 Keluar Aplikasi":
    st.empty() # Membersihkan tampilan sementara
    st.markdown('<div class="animated-thankyou">terima kasih dan kembalilah lagi!</div>', unsafe_allow_html=True)
    st.balloons() # Efek animasi balon pendukung tambahan dari Streamlit

# --- KONTEN BAB PERCOBAAN ORGANIK ---
else:
    bab = pilihan_halaman
    st.title(f"Bab: {bab}")
    st.write(f"Berikut adalah daftar modul uji coba kualitatif fungsional untuk kategori **{bab}**.")
    
    # Mengambil daftar sub-uji berdasarkan bab yang dipilih
    daftar_sub_uji = list(data_uji[bab].keys())
    
    # Membuat tab dinamis untuk tiap sub-pengujian di dalam bab
    tabs = st.tabs(daftar_sub_uji)
    
