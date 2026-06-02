import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time

# ================= إعداد الصفحة =================
st.set_page_config(page_title="Nasij Smart Factory", layout="wide")

# ================= تصميم فاخر =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#0f0f0f,#1b3b2f);
    color:white;
    direction:rtl;
}

/* Glass Effect */
.glass {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 16px;
    padding: 20px;
    backdrop-filter: blur(10px);
}

/* عنوان */
h1,h2,h3 {
    color:#d4af37;
}
</style>
""", unsafe_allow_html=True)

# ================= بيانات =================
if "orders" not in st.session_state:
    st.session_state.orders = [
        {"id":1,"area":5},
        {"id":2,"area":8},
        {"id":3,"area":3}
    ]

data = st.session_state.orders

# ================= Sidebar =================
menu = st.sidebar.radio("🧶 Nasij OS",[
    "👑 Dashboard",
    "📦 الطلبات",
    "🧠 AI Manager",
    "🏭 Digital Twin",
    "📄 التقارير"
])

# ================= Dashboard =================
if menu == "👑 Dashboard":

    st.title("👑 لوحة القيادة التنفيذية")

    total_orders = len(data)
    total_profit = sum(o["area"]*500 for o in data)
    predicted_profit = int(total_profit * random.uniform(1.1,1.4))
    total_time = sum(o["area"]*2 for o in data)

    col1,col2,col3 = st.columns(3)
    col1.metric("📦 الطلبات", total_orders)
    col2.metric("💰 الربح", total_profit)
    col3.metric("🔮 المتوقع", predicted_profit)

    st.markdown("---")

    df = pd.DataFrame(data)

    colA,colB = st.columns(2)

    with colA:
        fig = px.bar(df, x="id", y="area", title="الإنتاج")
        st.plotly_chart(fig, use_container_width=True)

    with colB:
        fig2 = px.line(df, x="id", y="area", title="نمو الطلبات")
        st.plotly_chart(fig2, use_container_width=True)

# ================= Orders =================
elif menu == "📦 الطلبات":

    st.header("📦 إدارة الطلبات")

    design = st.text_input("اسم التصميم")
    area = st.number_input("المساحة",1)

    if st.button("➕ إضافة طلب"):
        data.append({
            "id": len(data)+1,
            "design": design,
            "area": area
        })
        st.success("تمت الإضافة")

    for o in data:
        st.markdown(f"""
        <div class="glass">
        طلب #{o['id']}<br>
        المساحة: {o['area']} م²
        </div>
        """, unsafe_allow_html=True)

# ================= AI =================
elif menu == "🧠 AI Manager":

    st.header("🧠 المدير الذكي")

    if st.button("تشغيل الذكاء"):
        sorted_orders = sorted(data, key=lambda x: x["area"], reverse=True)
        st.success("تم تحليل المصنع")

        for i,o in enumerate(sorted_orders):
            st.write(f"طلب {o['id']} → أولوية {i+1}")

# ================= Digital Twin =================
elif menu == "🏭 Digital Twin":

    st.header("🏭 محاكاة المصنع")

    if st.button("تشغيل المحاكاة"):
        total_time = 0
        total_profit = 0

        for o in data:
            time.sleep(0.3)
            t = o["area"]*2
            p = o["area"]*500

            total_time += t
            total_profit += p

            st.progress(o["area"]/10)
            st.write(f"طلب {o['id']} → {t} ساعة | ربح {p}")

        st.success(f"⏱️ الوقت الكلي: {total_time}")
        st.success(f"💰 الربح: {total_profit}")

# ================= Reports =================
elif menu == "📄 التقارير":

    st.header("📄 تقرير المصنع")

    total_orders = len(data)
    total_profit = sum(o["area"]*500 for o in data)

    report = f"""
عدد الطلبات: {total_orders}
إجمالي الربح: {total_profit}
"""

    st.download_button("📥 تحميل التقرير", report)
