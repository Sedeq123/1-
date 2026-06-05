import streamlit as st

st.set_page_config(
    page_title="Nasij AI",
    page_icon="🧶",
    layout="wide"
)

st.title("🧶 Nasij AI")

st.subheader("مصمم السجاد الذكي")

# رفع صورة
uploaded_file = st.file_uploader(
    "📷 ارفع صورة",
    type=["jpg", "jpeg", "png"]
)

# الوصف
description = st.text_area(
    "✍️ اكتب وصف السجادة"
)

# النمط
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

# الخامة
material = st.selectbox(
    "🧶 اختر الخامة",
    [
        "بوليستر",
        "أكريليك فاخر",
        "صوف نيوزيلندي",
        "حرير صناعي",
        "حرير طبيعي"
    ]
)

# المقاس
width = st.number_input(
    "📏 العرض بالمتر",
    min_value=1.0,
    value=4.0
)

height = st.number_input(
    "📏 الطول بالمتر",
    min_value=1.0,
    value=6.0
)

if uploaded_file:
    st.image(uploaded_file)

if st.button("🚀 إنشاء التصميم"):

    area = width * height

    material_prices = {
        "بوليستر": 45,
        "أكريليك فاخر": 75,
        "صوف نيوزيلندي": 120,
        "حرير صناعي": 180,
        "حرير طبيعي": 350
    }

    cost_per_m = material_prices[material]

    production_cost = area * cost_per_m

    selling_price = production_cost * 1.5

    profit = selling_price - production_cost

    st.success("تم إنشاء المشروع بنجاح")

    st.subheader("📋 مواصفات السجادة")

    st.write("🎨 النمط:", style)
    st.write("🧶 الخامة:", material)
    st.write("📏 المقاس:", f"{width} × {height} متر")
    st.write("📐 المساحة:", f"{area:.2f} م²")

    st.subheader("💰 التسعير الذكي")

    st.write("تكلفة الإنتاج:", f"{production_cost:.0f} ريال")
    st.write("سعر البيع المقترح:", f"{selling_price:.0f} ريال")
    st.write("الربح المتوقع:", f"{profit:.0f} ريال")

    if description:
        st.subheader("📝 الوصف")
        st.write(description)
