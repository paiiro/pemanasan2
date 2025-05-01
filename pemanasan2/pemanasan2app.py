import streamlit as st
import time

# Navigasi
st.set_page_config(page_title="Simulasi Pangan", page_icon="🍽️", layout="centered")
halaman = st.sidebar.selectbox("📚 Pilih Halaman:", ["Beranda", "Simulasi"])

if halaman == "Beranda":
    st.title("🍽️ Simulasi Pemanasan Pada Pangan")
    st.markdown("Selamat datang di **aplikasi interaktif** untuk memahami bagaimana bahan pangan bereaksi terhadap panas.")
    st.markdown("🔍 Di sini, kamu bisa memilih berbagai bahan seperti telur, daging, gula, dan lainnya untuk melihat apa yang terjadi pada suhu tertentu.")
    st.markdown("👨‍🍳 Gunakan mode *Chef* untuk tips memasak, atau mode *Analis* untuk penjelasan ilmiah.")
    st.markdown("📊 Disertai info penyimpanan dan fakta menarik setiap bahan!")
    st.image("download (6).jpeg", caption="Bolu Pandan Topping Keju & Choco Chip", use_column_width=True)
    st.markdown("---")
    st.markdown("➡️ Mulai dengan memilih menu **Simulasi** di sidebar kiri.")

elif halaman == "Simulasi":
    st.title("🔥 Simulasi Pemanasan pada Pangan")

    # --- Data Makanan ---
    data_makanan = {
        "🥚 Telur": {
            "reaksi": [(30, "Telur mulai memanas."), (62, "Putih telur menggumpal (albumin denaturasi)."), (70, "Kuning telur mengeras (lipovitellenin denaturasi).")],
            "penjelasan": "Protein seperti albumin dan lipovitellenin pada telur mengalami denaturasi saat dipanaskan.",
            "fun_fact": "Memasak telur perlahan menghasilkan tekstur creamy sempurna!",
            "penyimpanan": {"suhu": "0-4°C", "masa_simpan": "3-5 minggu", "tips": "Simpan di karton asli, jangan di pintu kulkas."}
        },
        "🍬 Gula": {
            "reaksi": [(100, "Gula mulai meleleh."), (160, "Gula mengalami karamelisasi."), (180, "Gula terbakar dan terasa pahit.")],
            "penjelasan": "Karamelisasi mengubah molekul sukrosa menjadi senyawa aromatik berwarna coklat.",
            "fun_fact": "Karamelisasi mulai sekitar 160°C menghasilkan rasa toffee!",
            "penyimpanan": {"suhu": "20-25°C", "masa_simpan": "18-24 bulan", "tips": "Simpan di wadah kedap udara."}
        },
        # Tambahkan bahan lain di sini...
    }

    def get_multi_reaksi(makanan, suhu):
        reaksi_list = []
        for batas_suhu, reaksi in data_makanan[makanan]["reaksi"]:
            if suhu >= batas_suhu:
                reaksi_list.append(f"- {batas_suhu}°C: {reaksi}")
        if not reaksi_list:
            return ["Belum ada perubahan signifikan."]
        return reaksi_list

    mode = st.radio("🎭 Simulasi Sebagai:", ("Chef", "Analis"))
    makanan = st.selectbox("🔍 Pilih Bahan Makanan:", list(data_makanan.keys()))
    pilihan_simulasi = st.radio("🔥 Mau set suhu manual atau simulasi pemanasan?", ("Set Suhu Manual", "Simulasi Pemanasan"))

    if pilihan_simulasi == "Set Suhu Manual":
        suhu = st.slider("🌡️ Atur Suhu (°C):", 0, 300, 25)
    else:
        suhu = 0
        progress = st.progress(0)
        for i in range(301):
            suhu = i
            progress.progress(i / 300)
            time.sleep(0.005)
        st.success("Simulasi selesai!")

    st.subheader(f"🔥 Pada suhu {suhu}°C:")
    reaksi_multi = get_multi_reaksi(makanan, suhu)
    for r in reaksi_multi:
        if mode == "Chef":
            if any(k in r.lower() for k in ["karamelisasi", "garing", "renyah", "meleleh", "harum"]):
                st.success(r)
            elif "melunak" in r.lower() or "mengering" in r.lower():
                st.warning(r)
            else:
                st.info(r)
        else:
            if any(k in r.lower() for k in ["denaturasi", "karamelisasi", "maillard"]):
                st.success(r)
            elif "pecah" in r.lower() or "menggumpal" in r.lower():
                st.warning(r)
            else:
                st.info(r)

    if suhu >= 150:
        st.markdown("<h3 style='color:red;'>⚡ Reaksi besar terjadi! ⚡</h3>", unsafe_allow_html=True)
    elif suhu >= 100:
        st.markdown("<h4 style='color:orange;'>🔥 Memasak aktif! Aroma khas muncul! 🔥</h4>", unsafe_allow_html=True)
    elif suhu >= 50:
        st.markdown("<h5 style='color:green;'>🌡️ Reaksi awal mulai! 🌡️</h5>", unsafe_allow_html=True)
    else:
        st.markdown("<h5 style='color:gray;'>❄️ Belum ada reaksi signifikan. ❄️</h5>", unsafe_allow_html=True)

    st.divider()

    if mode == "Chef":
        st.subheader("🍳 Tips & Fun Fact untuk Chef:")
        st.info(f"💡 {data_makanan[makanan]['fun_fact']}")
    else:
        st.subheader("🔬 Penjelasan Kimia Lanjut:")
        st.write(data_makanan[makanan]["penjelasan"])

    st.divider()

    st.subheader("🧊 Cara Penyimpanan:")
    penyimpanan = data_makanan[makanan]["penyimpanan"]
    st.write(f"• **Suhu Penyimpanan:** {penyimpanan['suhu']}")
    st.write(f"• **Masa Simpan:** {penyimpanan['masa_simpan']}")
    st.write(f"• **Tips:** {penyimpanan['tips']}")

    st.caption("🎯 Simulasi by Kelompok 3 PMIP 1E-2")
