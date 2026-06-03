import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
import time
from sklearn.linear_model import LinearRegression

# =========================
# إعداد الصفحة
# =========================
st.set_page_config(page_title="Smart Factory AI", layout="wide")

# =========================
# تصميم فاخر
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0f0f, #1b3b2f);
    color: white;
    direction: rtl;
    font-family: 'Cairo', sans-serif;
}

.glass {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

h1, h2, h3 {
    color: gold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# عنوان
# =========================
st.title("🏭 المصنع الذكي - Digital Twin + AI")

# =========================
# Digital Twin (محاكاة)
# =========================
machines = ["نسيج", "صباغة", "تجفيف", "تغليف"]

data = {
    "الآلة": machines,
    "الحرارة": np.random.randint(40, 100, 4),
    "الاهتزاز": np.random.randint(10, 50, 4),
    "الإنتاج": np.random.randint(200, 1000, 4)
}

df = pd.DataFrame(data)

# =========================
# كروت الحالة
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("📦 الإنتاج", df["الإنتاج"].sum())
col2.metric("🔥 أعلى حرارة", df["الحرارة"].max())
col3.metric("⚠️ أعلى اهتزاز", df["الاهتزاز"].max())

# =========================
# رسم الأداء
# =========================
st.markdown('<div class="glass">', unsafe_allow_html=True)

fig = px.bar(df, x="الآلة", y="الإنتاج", color="الإنتاج", title="الإنتاج لكل آلة")
st.plotly_chart(fig, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# AI توقع الأعطال
# =========================
st.subheader("🤖 تنبؤ الأعطال (AI)")

# تدريب نموذج بسيط
X = df[["الحرارة", "الاهتزاز"]]
y = np.random.randint(0, 2, len(df))  # 0 = سليم / 1 = خطر

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(X)

df["مستوى الخطر"] = prediction

# عرض النتائج
st.dataframe(df)

# =========================
# تنبيه ذكي
# =========================
for i, row in df.iterrows():
    if row["مستوى الخطر"] > 0.7:
        st.error(f"🚨 خطر عالي في آلة {row['الآلة']}")

# =========================
# رسم الحرارة
# =========================
fig2 = px.line(df, x="الآلة", y="الحرارة", title="مراقبة الحرارة")
st.plotly_chart(fig2, use_container_width=True)

# =========================
# تحديث تلقائي
# =========================
time.sleep(2)
st.rerun()
