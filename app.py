import streamlit as st

# =========================
# إعداد الصفحة
# =========================

st.set_page_config(
    page_title="Nasij AI",
    page_icon="🧶",
    layout="wide"
)

# =========================
# تصميم الواجهة
# =========================

st.markdown("""
<style>

.main {
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827
    );
}

h1 {
    text-align:center;
    color:#D4AF37;
}

h3 {
    color:#D4AF37;
}

.stButton button {
    background-color:#D4AF37;
    color:black;
    font-weight:bold;
    border:none;
    border-radius:12px;
    height:55px;
    width:100%;
}

div[data-baseweb="select"]{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# العنوان
# =========================

st.title("🧶 مصمم السجاد الذكي")

st.markdown("""
### صمم سجادتك بسهولة

📷 ارفع صورة أو

✍️ اكتب وصفاً

ثم احسب السعر مباشرة
""")

st.divider()

# =========================
# رفع صورة
# =========================

uploaded_file = st.file_uploader(
    "📷 ارفع صورة",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)

# =========================
# الوصف
# =========================

description = st.text_area(
    "✍️ اكتب وصف السجادة"
)

# =========================
# النمط
# =========================

style = st.selectbox(
    "🎨 اختر النمط",
    [
        "عربي",
        "نجدي",
        "إسلامي",
        "مودرن",
        "ملكي"
    ]
)

# =========================
# الخامة
# =========================

material = st.selectbox(
    "🧶 اختر الخامة",
    [
        "بوليستر",
        "فريس",
        "أكريليك",
        "صوف"
    ]
)

# =========================
# المقاسات
# =========================

col1, col2 = st.columns(2)

with col1:
    width = st.number_input(
        "📏 العرض بالمتر",
        min_value=1.0,
        value=4.0
    )

with col2:
    length = st.number_input(
        "📏 الطول بالمتر",
        min_value=1.0,
        value=6.0
    )

# =========================
# أسعار الخامات
# =========================

prices = {
    "بوليستر": 80,
    "فريس": 120,
    "أكريليك": 180,
    "صوف": 300
}

# =========================
# إنشاء التصميم
# =========================

if st.button("🚀 إنشاء التصميم"):

    area = width * length

    price_per_meter = prices[material]

    total_price = area * price_per_meter

    st.success("تم إنشاء الطلب بنجاح")

    st.markdown("## 📋 ملخص الطلب")

    st.write("🎨 النمط:", style)
    st.write("🧶 الخامة:", material)
    st.write("📏 العرض:", width, "متر")
    st.write("📏 الطول:", length, "متر")

    st.write("📐 المساحة:", area, "م²")

    st.write("💰 سعر المتر:", price_per_meter, "ريال")

    st.write("💵 السعر الإجمالي:", total_price, "ريال")

    if description:
        st.markdown("### ✍️ الوصف")
        st.write(description)

    if uploaded_file:
        st.markdown("### 🖼️ الصورة المرجعية")
        st.image(uploaded_file, use_container_width=True)

# =========================
# تذييل
# =========================

st.divider()

st.caption("Nasij AI © 2026")
