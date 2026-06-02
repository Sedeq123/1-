import streamlit as st
import json
from datetime import datetime

# إعدادات الصفحة العامة للويب وتدعم اللغة العربية (RTL)
st.set_page_config(page_title="تطبيق نسيج الذكي", page_icon="🧶", layout="wide")

# تخصيص واجهة الويب لتدعم الكتابة من اليمين إلى اليسار
st.markdown("""
    <style>
    .reportview-container .main .block-container{ max-width: 90%; }
    body, p, h1, h2, h3, h4, h5, h6, span, div { text-align: right; direction: rtl; }
    div.stButton > button:first-child { background-color: #2E7D32; color:white; font-size:18px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# تفعيل قاعدة البيانات المؤقتة في الذاكرة لتجربة الويب
if 'app_data' not in st.session_state:
    st.session_state.app_data = {
        "designs": {
            "العاديات": {"type": "نحت 3D مخملي", "cost": "580-800", "price": 2500},
            "سيادة الأفق": {"type": "نحت 3D مطعم بالفضة", "cost": "650-850", "price": 2800},
            "ملحمة الشموخ والقوة": {"type": "هجين معقد (خيل وصقر)", "cost": "750-1000", "price": 3500},
            "حارس القافلة والأفق": {"type": "هجين حرير ذهبي (جمل وصقر)", "cost": "700-950", "price": 3200}
        },
        "hr": {
            "101": {"name": "أحمد", "role": "فني نحت ثلاثي أبعاد (3D)", "pay": 300, "tasks": []},
            "102": {"name": "خالد", "role": "فني نسيج بمسدس Tufting", "pay": 150, "tasks": []}
        },
        "crm": {
            "VIP_01": {"name": "سمو الأمير (قصر الرياض)", "cat": "كبار الشخصيات", "tasks": [], "feedback": []},
            "B2B_01": {"name": "شركة معارض دبي للسجاد", "cat": "جملة", "tasks": [], "feedback": []}
        },
        "suggestions": []
    }

data = st.session_state.app_data

st.title("🧶 لوحة تحكم إمبراطورية 'نسيج الذكي' - النسخة التجريبية")
st.write("مرحباً بك يا صديقي! هذه هي واجهة الويب التفاعلية لإدارة معملك وتصاميمك الملحمية الأربعة.")
st.markdown("---")

# تقسيم الشاشة إلى تبويبات رئيسية لسهولة التنقل بالضغط
tabs = st.tabs(["🎙️ الأوامر الصوتية", "📸 استلهام التصاميم", "👥 الموارد البشرية (HR)", "👑 إدارة زبائن النخبة", "💡 صندوق الأفكار"])

# ==========================================
# 1. تبويب الأوامر الصوتية والتنقل
# ==========================================
with tabs[0]:
    st.header("🎙️ التحكم الصوتي والذكي بالتطبيق")
    st.write("حاكي عمل المساعد الصوتي بكتابة أو محاكاة أمرك هنا:")
    voice_input = st.text_input("اكتب أمرك الصوتي هنا (مثال: افتح شاشة الحسابات، أو افتح الموارد البشرية):")
    
    if st.button("إرسال الأمر الصوتي"):
        cmd = voice_input.lower()
        if "الموارد" in cmd or "العمال" in cmd:
            st.success("🤖 مساعد الذكاء الاصطناعي: 'علم ويُنفذ! جاري نقلك تلقائياً إلى تبويب الموارد البشرية في الواجهة.'")
        elif "الزبائن" in cmd or "العملاء" in cmd:
            st.success("🤖 مساعد الذكاء الاصطناعي: 'تم استقبال أمرك، جاري فتح قسم زبائن النخبة والجملة.'")
        elif "تصميم" in cmd or "التصاميم" in cmd:
            st.success("🤖 مساعد الذكاء الاصطناعي: 'جاري فتح معرض ثلاثية الأصالة التجريدية.'")
        else:
            st.info("🤖 مساعد الذكاء الاصطناعي: 'تم استقبال أمرك الصوتي بنجاح، النظام جاهز للتنفيذ.'")

# ==========================================
# 2. تبويب التقاط واستلهام التصاميم من الصور
# ==========================================
with tabs[1]:
    st.header("📸 ميزة الالتقاط والاستلهام البصري")
    st.write("ارفع صورة الفكرة أو النقشة، واكتب مواصفات العميل ليقوم الذكاء الاصطناعي بتوليد السجادة:")
    
    uploaded_file = st.file_uploader("اختر صورة من الألبوم أو التقطها بالكاميرا:", type=["jpg", "png", "jpeg"])
    user_specs = st.text_area("أدخل المواصفات المطلوبة للتصميم (مثل: نوع الخيوط، الألوان، عمق النحت):", 
                              placeholder="مثال: أضف خيوط الحرير الذهبي اللامع، واجعل الخلفية بدقة ثلاثية الأبعاد...")
    
    if st.button("توليد التصميم المستوحى بالذكاء الاصطناعي"):
        if uploaded_file and user_specs:
            st.info("🔄 جاري الاتصال بمحرك الذكاء الاصطناعي الخارجي (Leonardo API)...")
            st.success("✨ تم توليد التصميم الجديد بنجاح مدمجاً بمواصفاتك!")
            st.image("https://images.unsplash.com/photo-1600121848594-d8644e57abab?q=80&w=600", 
                     caption="نموذج تخيلي للسجادة ثلاثية الأبعاد المستوحاة من الصورة", width=500)
            st.code(f"الـ Prompt النهائي المستخدم: Luxury 3D Carpet design with specifications: {user_specs}")
        else:
            st.warning("الرجاء رفع صورة وكتابة المواصفات الفنية أولاً لتتم عملية الاستلهام.")

# ==========================================
# 3. تبويب إدارة الموارد البشرية والعمال
# ==========================================
with tabs[2]:
    st.header("👥 إدارة الموارد البشرية وتوزيع مهام النحت")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("إسناد مهمة إنتاج جديدة")
        selected_worker = st.selectbox("اختر الفني المسؤول:", [f"{k} - {v['name']} ({v['role']})" for k, v in data["hr"].items()])
        selected_design = st.selectbox("اختر التصميم المراد إنتاجه ونحته:", list(data["designs"].keys()))
        area = st.number_input("المساحة المطلوبة بالمتر المربع (م٢):", min_value=1, value=4)
        
        if st.button("تأكيد وإسناد المهمة"):
            worker_id = selected_worker.split(" - ")[0]
            pay_per_m = data["hr"][worker_id]["pay"]
            total_pay = pay_per_m * area
            
            task = {
                "design": selected_design,
                "area": area,
                "payout": total_pay,
                "status": "قيد النحت والتشطيب"
            }
            data["hr"][worker_id]["tasks"].append(task)
            st.success(f"تم إسناد المهمة بنجاح للفني! الأجر المحسوب والمضاف لحسابه: {total_pay} ريال/درهم.")
            
    with col2:
        st.subheader("سجل إنتاجية الفنيين الحالي")
        for k, v in data["hr"].items():
            st.markdown(f"**الفني: {v['name']}** | التخصص: {v['role']}")
            if v["tasks"]:
                for t in v["tasks"]:
                    st.caption(f"📍 تصميم: {t['design']} | المساحة: {t['area']}م٢ | الأجر المستحق: {t['payout']} ريال/درهم ({t['status']})")
            else:
                st.caption("لا توجد مهام مسندة حالياً.")
            st.markdown("---")

# ==========================================
# 4. تبويب إدارة زبائن النخبة والجملة والآراء
# ==========================================
with tabs[3]:
    st.header("👑 نظام إدارة علاقات زبائن النخبة والجملة (Smart CRM)")
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("توثيق طلب ورأي زبون")
        selected_cust = st.selectbox("اختر الزبون:", [f"{k} - {v['name']} ({v['cat']})" for k, v in data["crm"].items()])
        cust_design = st.selectbox("المنتج المطلوب:", list(data["designs"].keys()))
        rating = st.slider("تقييم العميل للقطعة الفنية:", 1, 5, 5)
        comment = st.text_area("رأي وانطباع الزبون الفعلي (الآراء):")
        
        if st.button("حفظ وتوثيق رأي الزبون"):
            cust_id = selected_cust.split(" - ")[0]
            data["crm"][cust_id]["orders"].append(cust_design)
            data["crm"][cust_id]["feedback"].append({"product": cust_design, "rating": rating, "comment": comment})
            st.success("تم ربط رأي وتقييم العميل بالمنتج بنجاح وتحديث لوحة التحكم!")
            
    with col4:
        st.subheader("سجل زبائن النخبة والآراء الحالية")
        for k, v in data["crm"].items():
            st.markdown(f"👤 **الاسم: {v['name']}** | التصنيف: `<{v['cat']}>`")
            if v["feedback"]:
                for f in v["feedback"]:
                    st.info(f"💬 رأيه بمنتج '{f['product']}': {f['comment']} (تقييم: {f['rating']}/5)")
            else:
                st.caption("لم يتم تسجيل أي آراء لهذا العميل بعد.")
            st.markdown("---")

# ==========================================
# 5. تبويب الاقتراحات الشخصية لصاحب المعمل
# ==========================================
with tabs[4]:
    st.header("💡 صندوق الأفكار والمقترحات الشخصية")
    st.write("سجل أفكارك الإبداعية لتطوير المواد أو دمج الخيوط هنا لتبقى محفوظة في نظام معملك:")
    
    new_suggestion = st.text_area("اكتب فكرتك أو اقتراحك الشخصي هنا:")
    if st.button("حفظ الفكرة في صندوق الأفكار"):
        if new_suggestion:
            data["suggestions"].append({"idea": new_suggestion, "time": datetime.now().strftime("%Y-%m-%d %H:%M")})
            st.success("تم حفظ فكرتك الإبداعية بنجاح في صندوق مقترحاتك الشخصية التابع لـ نسيج الذكي! 💡")
        else:
            st.warning("الرجاء كتابة فكرة لحفظها.")
            
    if data["suggestions"]:
        st.subheader("🗒️ أفكارك المحفوظة سابقاً لتطوير المعمل:")
        for idx, s in enumerate(data["suggestions"]):
            st.markdown(f"{idx+1}. **{s['idea']}** *(تم الحفظ بتاريخ: {s['time']})*")
                            
