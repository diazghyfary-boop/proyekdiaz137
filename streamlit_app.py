import streamlit as st

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Lab Kimia Organik Virtual v2",
    page_icon="🧪",
    layout="wide"
)

# Kustomisasi CSS untuk Animasi Teks Terima Kasih dan Kartu Informasi
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
.metric-box {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 8px;
    border-left: 5px solid #1f77b4;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Definisikan Data Pengujian Kimia Organik Lengkap
data_uji = {
    "Hidrokarbon 🛢️": {
        "Uji Bromin ($Br_2/CCl_4$)": {
            "tujuan": "Mendeteksi adanya ikatan rangkap dua atau tiga (ketidakjenuhan) pada hidrokarbon.",
            "sifat": "Reaksi adisi halogen pada ikatan rangkap tanpa menghasilkan gas sampingan.",
            "kejadian": "Larutan bromin diteteskan ke dalam sampel hidrokarbon secara perlahan.",
            "hasil": "Positif pada alkena/alkuna (senyawa tak jenuh). Negatif pada alkana.",
            "warna": "Warna cokelat kemerahan dari bromin berubah menjadi jernih/tidak berwarna.",
            "kelarutan": "Produk hasil reaksi bersifat non-polar dan larut sempurna dalam pelarut $CCl_4$ atau kloroform.",
            "waktu": "1 - 5 detik",
            "reaksi": "$$R-CH=CH-R + Br_2 \\rightarrow R-CH(Br)-CH(Br)-R$$",
            "gagal": "Warna cokelat merah tidak memudar. Hal ini terjadi jika sampel adalah alkana jenuh, atau reagen bromin sudah rusak/terurai akibat paparan cahaya matahari langsung."
        },
        "Uji Baeyer ($KMnO_4$)": {
            "tujuan": "Mengidentifikasi ikatan rangkap alifatik tak jenuh.",
            "sifat": "Oksidasi ringan oleh oksidator kuat dalam suasana netral atau basa.",
            "kejadian": "Penambahan larutan kalium permanganat ungu ke dalam senyawa sampel.",
            "hasil": "Terbentuk glikol (diol) dan endapan mangan dioksida.",
            "warna": "Warna ungu tua $KMnO_4$ hilang dan berganti menjadi endapan cokelat tua.",
            "kelarutan": "Endapan cokelat $MnO_2$ yang terbentuk tidak larut dalam air dan mengendap di dasar tabung.",
            "waktu": "5 - 15 detik",
            "reaksi": "$$3R-CH=CH-R + 2KMnO_4 + 4H_2O \\rightarrow 3R-CH(OH)-CH(OH)-R + 2MnO_2\\downarrow + 2KOH$$",
            "gagal": "Warna ungu tidak hilang dan tidak ada endapan cokelat. Gagal jika sampel adalah alkana atau senyawa aromatik stabil seperti benzena."
        }
    },
    "Protein 🧬": {
        "Uji Biuret": {
            "tujuan": "Mendeteksi keberadaan ikatan peptida dalam suatu zat.",
            "sifat": "Pembentukan senyawa kompleks koordinasi antara ion tembaga dengan nitrogen dari ikatan peptida.",
            "kejadian": "Larutan protein dicampur $NaOH$ kemudian ditetesi $CuSO_4$ encer.",
            "hasil": "Positif menunjukkan adanya senyawa dengan minimal dua ikatan peptida.",
            "warna": "Perubahan warna dari biru muda (reagen) menjadi ungu/violet murni.",
            "kelarutan": "Kompleks protein-tembaga yang terbentuk larut sempurna dalam air (membentuk larutan jernih berwarna ungu).",
            "waktu": "30 detik - 1 menit",
            "reaksi": "$$\\text{Protein} + Cu^{2+} + OH^- \\rightarrow \\text{Kompleks Koordinasi Biuret (Warna Ungu)}$$",
            "gagal": "Warna tetap biru muda. Reaksi gagal jika sampel merupakan asam amino tunggal (misal glisin) karena tidak memiliki ikatan peptida."
        },
        "Uji Xantoproteat": {
            "tujuan": "Mengidentifikasi asam amino yang memiliki cincin benzena (tirosin, triptofan, fenilalanin).",
            "sifat": "Reaksi nitrasi pada inti benzena oleh asam nitrat pekat.",
            "kejadian": "Sampel dipanaskan bersama $HNO_3$ pekat, didinginkan, lalu ditambahkan basa kuat.",
            "hasil": "Terbentuk senyawa turunan nitro-benzena.",
            "warna": "Saat dipanaskan terbentuk warna kuning, setelah ditambah basa berubah menjadi jingga/oranye.",
            "kelarutan": "Sebbagian protein terkoagulasi (menggumpal dan tidak larut) saat ditambah asam pekat, namun larut kembali sebagian setelah suasananya menjadi basa.",
            "waktu": "1 - 2 menit",
            "reaksi": "$$\\text{Cincin Benzena (Protein)} + HNO_3 \\xrightarrow{\\Delta} \\text{Turunan Nitro (Kuning)} \\xrightarrow{NaOH} \\text{Garam Nitro (Jingga)}$$",
            "gagal": "Warna larutan tidak berubah menjadi jingga. Gagal terjadi jika protein tidak mengandung asam amino aromatik (seperti pada gelatin murni)."
        }
    },
    "Asam Karboksilat 🍋": {
        "Uji Natrium Bikarbonat ($NaHCO_3$)": {
            "tujuan": "Menguji sifat keasaman relatif senyawa organik (membedakan asam karboksilat dengan fenol).",
            "sifat": "Reaksi asam-basa kuat-lemah yang menghasilkan gas karbon dioksida.",
            "kejadian": "Sampel padat atau cair direaksikan dengan larutan $NaHCO_3$ 5%.",
            "hasil": "Terbentuk garam natrium karboksilat air, dan pelepasan gas.",
            "warna": "Larutan tetap jernih/tidak berwarna, namun terlihat gelembung gas yang bergerak aktif.",
            "kelarutan": "Asam karboksilat yang awalnya sukar larut dalam air akan menjadi larut sempurna karena berubah menjadi garam natrium yang polar.",
            "waktu": "1 - 3 detik",
            "reaksi": "$$R-COOH + NaHCO_3 \\rightarrow R-COONa + H_2O + CO_2\\uparrow$$",
            "gagal": "Tidak ada gelembung gas sama sekali. Gagal jika tingkat keasaman senyawa terlalu lemah ($pK_a > 7$) seperti alkohol atau fenol terhambat sterik."
        },
        "Uji Esterifikasi": {
            "tujuan": "Mengidentifikasi gugus karboksilat melalui pembentukan senyawa ester berbau khas.",
            "sifat": "Reaksi kondensasi reversibel pelepasan air dengan bantuan katalis asam kuat pekat.",
            "kejadian": "Asam karboksilat dipanaskan bersama alkohol (etanol) dan beberapa tetes asam sulfat pekat.",
            "hasil": "Terbentuk senyawa ester (alkil alkanoat).",
            "warna": "Larutan tetap jernih/tidak berwarna.",
            "kelarutan": "Ester yang terbentuk bersifat non-polar sehingga tidak larut dalam air dan membentuk lapisan minyak tipis tersendiri di permukaan cairan.",
            "waktu": "5 - 10 menit",
            "reaksi": "$$R-COOH + R'-OH \\xrightarrow{H_2SO_4, \\Delta} R-COOR' + H_2O$$",
            "gagal": "Tidak tercium aroma buah (aroma khas ester) dan tidak ada lapisan minyak. Gagal karena pemanasan kurang lama atau kontaminasi air yang menggeser kesetimbangan ke arah kiri."
        }
    },
    "Minyak dan Lemak 🧈": {
        "Uji Akrolein": {
            "tujuan": "Mendeteksi keberadaan gliserol atau senyawa lemak/minyak yang mengandung struktur gliserol.",
            "sifat": "Dehidrasi gliserol oleh agen pendehidrasi kuat pada suhu tinggi.",
            "kejadian": "Sampel minyak dipanaskan kuat bersama kristal kalium hidrogen sulfat ($KHSO_4$).",
            "hasil": "Terbentuk senyawa aldehid tak jenuh bernama akrolein.",
            "warna": "Muncul asap putih tebal di dalam tabung reaksi.",
            "kelarutan": "Gas akrolein yang terbentuk menguap ke udara, sementara residu sisa pembakaran karbon berwarna hitam tidak larut di dasar tabung.",
            "waktu": "2 - 3 menit",
            "reaksi": "$$\\text{Gliserol} \\xrightarrow{KHSO_4, \\Delta} \\text{Akrolein } (CH_2=CH-CHO) + 2H_2O$$",
            "gagal": "Tidak menghasilkan bau menusuk hidung yang khas. Gagal jika sampel merupakan minyak bumi (minyak mineral/parafin) yang tidak tersusun atas senyawa trigliserida."
        },
        "Uji Ketidakjenuhan Lemak": {
            "tujuan": "Membedakan asam lemak jenuh (lemak padat) dan asam lemak tak jenuh (minyak nabati cair).",
            "sifat": "Adisi halogen (iodium atau bromin) pada rantai karbon berikatan rangkap.",
            "kejadian": "Minyak dilarutkan dalam kloroform lalu ditetesi larutan iodium.",
            "hasil": "Adisi sukses pada titik ikatan rangkap minyak nabati.",
            "warna": "Warna merah/merah muda dari iodium hilang/pudar pada minyak tak jenuh, dan tetap berwarna merah pada lemak jenuh.",
            "kelarutan": "Seluruh komponen reagen dan sampel larut sempurna di dalam pelarut kloroform.",
            "waktu": "1 - 2 menit",
            "reaksi": "$$\\text{Asam Lemak Tak Jenuh} + I_2 \\rightarrow \\text{Senyawa Di-iodo Jenuh}$$",
            "gagal": "Warna merah tidak pudar pada sampel minyak nabati. Gagal akibat minyak sudah terlalu lama disimpan dan mengalami tengik (oksidasi alami) sehingga ikatan rangkapnya sudah rusak."
        }
    },
    "Karbohidrat 🌾": {
        "Uji Molisch": {
            "tujuan": "Uji umum universal untuk mendeteksi keberadaan segala jenis karbohidrat.",
            "sifat": "Dehidrasi karbohidrat oleh asam pekat membentuk senyawa furfural yang berkondensasi dengan alfa-naftol.",
            "kejadian": "Larutan karbohidrat dicampur reagen Molisch, lalu dialirkan $H_2SO_4$ pekat lewat dinding tabung.",
            "hasil": "Positif untuk golongan monosakarida, disakarida, dan polisakarida.",
            "warna": "Terbentuk cincin berwarna ungu tua/violet tepat di perbatasan kedua lapisan cairan.",
            "kelarutan": "Asam sulfat pekat berada di lapisan bawah karena massa jenisnya lebih besar dan membentuk batas fasa yang tidak bercampur secara langsung dengan sampel.",
            "waktu": "30 - 60 detik",
            "reaksi": "$$\\text{Heksosa} \\xrightarrow{H_2SO_4} \\text{Hidroksimetilfurfural} \\xrightarrow{\\alpha\\text{-naftol}} \\text{Kompleks Ungu}$$",
        }
    }
}
