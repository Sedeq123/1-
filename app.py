import streamlit as st

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="Nasij Studio",
    page_icon="🧶",
    layout="wide"
)

# =========================
# Custom CSS
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
}

h1, h2, h3 {
    color: #D4AF37;
}

.main-title {
    text-align: center;
    color: #D4AF37;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: white;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-box {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(212,175,55,0.25);
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    background-color: #D4AF37;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    height: 50px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================

st.markdown("""
<div class="main-title">
🧶 Nasij Studio
</div>

<div class="sub-title">
Smart Carpet Design Platform<br>
منصة تصميم السجاد الذكية
</div>
""", unsafe_allow_html=True)

# =========================
# Layout
# =========================

left, right = st.columns([2, 1])

# =========================
# LEFT SIDE
# =========================

with left:

    st.markdown("## 🎨 Design Studio")

    uploaded_file = st.file_uploader(
        "📷 Upload Image / رفع صورة",
        type=["jpg", "jpeg", "png"]
    )

    description = st.text_area(
        "✍️ Design Description / وصف التصميم",
        height=120
    )

    style = st.selectbox(
        "👑 Style / النمط",
        [
            "Arabic عربي",
            "Najdi نجدي",
            "Islamic إسلامي",
            "Royal ملكي",
            "Modern مودرن",
            "Gulf Heritage تراث خليجي"
        ]
    )

    material = st.selectbox(
        "🧶 Material / الخامة",
        [
            "Polyester",
            "Frieze",
            "Acrylic",
            "Natural Wool"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        width = st.number_input(
            "📏 Width (m)",
            min_value=1.0,
            value=4.0
        )

    with col2:
        height = st.number_input(
            "📏 Height (m)",
            min_value=1.0,
            value=6.0
        )

# =========================
# PRICE ENGINE
# =========================

prices = {
    "Polyester": 80,
    "Frieze": 120,
    "Acrylic": 180,
    "Natural Wool": 300
}

area = width * height
price_per_meter = prices[material]
total_price = area * price_per_meter

# =========================
# RIGHT SIDE
# =========================

with right:

    st.markdown("## 💰 Smart Pricing")

    st.metric(
        "Area / المساحة",
        f"{area:.2f} m²"
    )

    st.metric(
        "Price / m²",
        f"{price_per_meter} SAR"
    )

    st.metric(
        "Estimated Cost",
        f"{total_price:,.0f} SAR"
    )

# =========================
# SUMMARY
# =========================

st.markdown("---")

st.markdown("## 📋 Project Summary")

summary_col1, summary_col2 = st.columns([1, 1])

with summary_col1:

    st.info(f"👑 Style: {style}")
    st.info(f"🧶 Material: {material}")
    st.info(f"📐 Area: {area:.2f} m²")
    st.info(f"💰 Price: {total_price:,.0f} SAR")

with summary_col2:

    if description:
        st.write("### ✍️ Description")
        st.write(description)

# =========================
# IMAGE PREVIEW
# =========================

if uploaded_file:

    st.markdown("---")
    st.markdown("## 🖼️ Design Preview")

    st.image(
        uploaded_file,
        use_container_width=True
    )

# =========================
# ORDER BUTTON
# =========================

st.markdown("---")

if st.button("🚀 Create Project / إنشاء المشروع"):

    st.success("✅ Project Created Successfully")

    st.balloons()

# =========================
# Footer
# =========================

st.markdown("---")

st.caption(
    "© 2026 Nasij Studio - Smart Carpet Design Platform"
)
