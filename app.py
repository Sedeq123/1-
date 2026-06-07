import streamlit as st

# =========================
# إعداد الصفحة
# =========================

st.set_page_config(
    page_title="Nasij Studio",
    page_icon="🧶",
    layout="wide"
)

# =========================
# تنسيق بسيط
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
}

h1,h2,h3 {
    color: #D4AF37;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =========================
# الأسعار
# =========================

prices = {
    "بوليستر": 80,
    "نايلون": 120,
    "صوف": 220,
    "حرير": 450
}

# =========================
# القائمة الجانبية
# =========================

st.sidebar.title("🧶 Nasij Studio")

page = st.sidebar.radio(
    "القائمة الرئيسية",
    [
        "🏠 الرئيسية",
        "🎨 تصميم السجاد",
        "🧶 الخامات والمقاسات",
        "💰 التسعير",
        "📚 الكاتالوج",
        "🛒 الطلبات",
        "📞 التواصل"
    ]
)

# =========================
# الرئيسية
# =========================

if page == "🏠 الرئيسية":

    st.title("🧶 Nasij Studio")

    st.subheader("Smart Carpet Design Platform")

    st.write("""
    مرحباً بك في منصة نسيج ستوديو

    ✔ تصميم سجاد مخصص

    ✔ حساب الأسعار

    ✔ اختيار الخامات

    ✔ إدارة الطلبات

    ✔ تجهيز للإنتاج
    """)

    st.info("ابدأ من قسم تصميم السجاد في القائمة الجانبية")

# =========================
# التصميم
# =========================

elif page == "🎨 تصميم السجاد":

    st.title("🎨 تصميم السجاد")

    uploaded_file = st.file_uploader(
        "📷 ارفع صورة",
        type=["jpg", "jpeg", "png"]
    )

    description = st.text_area(
        "✍️ اكتب وصف التصميم"
    )

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

    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)

    if st.button("🚀 إنشاء التصميم"):

        st.success("تم استلام بيانات التصميم")

        st.write("النمط:", style)

        if description:
            st.write("الوصف:")
            st.write(description)

# =========================
# الخامات
# =========================

elif page == "🧶 الخامات والمقاسات":

    st.title("🧶 الخامات والمقاسات")

    material = st.selectbox(
        "اختر الخامة",
        list(prices.keys())
    )

    width = st.number_input(
        "العرض (متر)",
        min_value=1.0,
        value=4.0
    )

    height = st.number_input(
        "الطول (متر)",
        min_value=1.0,
        value=6.0
    )

    area = width * height

    st.metric(
        "المساحة",
        f"{area:.2f} م²"
    )

    st.metric(
        "سعر المتر",
        f"{prices[material]} ريال"
    )

# =========================
# التسعير
# =========================

elif page == "💰 التسعير":

    st.title("💰 التسعير الذكي")

    material = st.selectbox(
        "الخامة",
        list(prices.keys())
    )

    width = st.number_input(
        "العرض",
        min_value=1.0,
        value=4.0,
        key="price_width"
    )

    height = st.number_input(
        "الطول",
        min_value=1.0,
        value=6.0,
        key="price_height"
    )

    area = width * height

    total = area * prices[material]

    st.metric(
        "المساحة",
        f"{area:.2f} م²"
    )

    st.metric(
        "السعر التقديري",
        f"{total:,.0f} ريال"
    )

# =========================
# الكاتالوج
# =========================

elif page == "📚 الكاتالوج":

    st.title("📚 الكاتالوج")

    st.write("🏆 سجاد عربي")
    st.write("🏆 سجاد نجدي")
    st.write("🏆 سجاد إسلامي")
    st.write("🏆 سجاد مودرن")
    st.write("🏆 سجاد ملكي")

# =========================
# الطلبات
# =========================

elif page == "🛒 الطلبات":

    st.title("🛒 الطلبات")

    st.info("لا توجد طلبات حالياً")

# =========================
# التواصل
# =========================

elif page == "📞 التواصل":

    st.title("📞 التواصل")

    st.text_input("الاسم")

    st.text_input("رقم الجوال")

    st.text_area("الرسالة")

    if st.button("إرسال"):
        st.success("تم إرسال الرسالة بنجاح")

# =========================
# Footer
# =========================

st.markdown("---")
st.caption("© Nasij Studio 2026")
