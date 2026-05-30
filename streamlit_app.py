import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Tabel Periodik Unsur",
    page_icon="🧪",
    layout="wide"
)

# Data contoh unsur
data_unsur = {
    "Unsur": ["Hidrogen", "Karbon", "Nitrogen", "Oksigen", "Natrium", "Klor"],
    "Simbol": ["H", "C", "N", "O", "Na", "Cl"],
    "Nomor Atom": [1, 6, 7, 8, 11, 17],
    "Konfigurasi Elektron": [
        "1s¹",
        "1s² 2s² 2p²",
        "1s² 2s² 2p³",
        "1s² 2s² 2p⁴",
        "1s² 2s² 2p⁶ 3s¹",
        "1s² 2s² 2p⁶ 3s² 3p⁵"
    ],
    "Golongan": ["IA", "IVA", "VA", "VIA", "IA", "VIIA"],
    "Periode": [1, 2, 2, 2, 3, 3],
    "Sifat": [
        "Nonlogam",
        "Nonlogam",
        "Nonlogam",
        "Nonlogam",
        "Logam Alkali",
        "Halogen"
    ],
    "Elektronegativitas": [
        2.20,
        2.55,
        3.04,
        3.44,
        0.93,
        3.16
    ],
    "Ikatan Umum": [
        "Kovalen",
        "Kovalen",
        "Kovalen",
        "Kovalen",
        "Ionik",
        "Ionik/Kovalen"
    ],
    "Polar/Nonpolar": [
        "Bergantung Molekul",
        "Umumnya Nonpolar",
        "Polar",
        "Polar",
        "Ionik",
        "Polar"
    ],
    "Hibridisasi (sp)": [
        "s",
        "sp, sp², sp³",
        "sp³",
        "sp³",
        "-",
        "sp³"
    ],
    "Elektron Valensi": [
        1,
        4,
        5,
        6,
        1,
        7
    ]
}

df = pd.DataFrame(data_unsur)

# Sidebar
st.sidebar.title("Menu Navigasi")

menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "Halaman 1 - Tabel Periodik",
        "Halaman 2 - Informasi Unsur",
        "Selesai"
    ]
)

# HALAMAN 1
if menu == "Halaman 1 - Tabel Periodik":

    st.title("🧪 Tabel Periodik Unsur")

    st.write("""
    Selamat datang di website pembelajaran Tabel Periodik Unsur.
    Pada halaman ini ditampilkan gambar tabel periodik.
    """)

    st.image(
        "https://share.google/jmSXkH9eKpHooJMeR",
        caption="Tabel Periodik Unsur",
        use_container_width=True
    )

# HALAMAN 2
elif menu == "Halaman 2 - Informasi Unsur":

    st.title("📖 Informasi Unsur")

    pilihan = st.selectbox(
        "Pilih Unsur",
        df["Unsur"]
    )

    hasil = df[df["Unsur"] == pilihan]

    st.subheader(f"Data {pilihan}")

    st.dataframe(hasil, use_container_width=True)

    st.markdown("### Penjelasan")

    st.write(
        f"""
        Unsur **{hasil['Unsur'].iloc[0]}**
        memiliki nomor atom **{hasil['Nomor Atom'].iloc[0]}**
        dengan konfigurasi elektron
        **{hasil['Konfigurasi Elektron'].iloc[0]}**.

        Unsur ini berada pada golongan
        **{hasil['Golongan'].iloc[0]}**
        dan periode
        **{hasil['Periode'].iloc[0]}**.

        Sifat unsur:
        **{hasil['Sifat'].iloc[0]}**

        Ikatan yang umum terbentuk:
        **{hasil['Ikatan Umum'].iloc[0]}**

        Polaritas:
        **{hasil['Polar/Nonpolar'].iloc[0]}**

        Hibridisasi:
        **{hasil['Hibridisasi (sp)'].iloc[0]}**
        """
    )

# HALAMAN SELESAI
elif menu == "Selesai":

    st.chemistry()

    st.success(
        "🎉 Terima kasih telah memakai website kami."
    )

    st.write("""
    Semoga website ini membantu Anda mempelajari
    tabel periodik unsur dengan lebih mudah.
    """)
