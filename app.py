import streamlit as st

st.set_page_config(
    page_title="Nasij AI",
    page_icon="🧶",
    layout="wide"
)

st.title("🧶 Nasij AI")

st.subheader("مصمم السجاد الذكي")

uploaded_file = st.file_uploader(
    "📷 ارفع صورة",
    type=["jpg", "jpeg", "png"]
)

description = st.text_area(
    "✍️ اكتب وصف السجادة"
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
    st.image(uploaded_file)

if st.button("🚀 إنشاء التصميم"):
    st.success("تم استلام الصورة والوصف بنجاح")

    st.write("الوصف:")
    st.write(description)

    st.write("النمط:")
    st.write(style)
