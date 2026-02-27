import streamlit as st
from openai import OpenAI

# 1️⃣ إعدادات الصفحة والهوية البصرية (Dark Mode & Layout)
st.set_page_config(page_title="Benidik AI | Engineering Intelligent Growth", page_icon="🧠", layout="wide")

# تطبيق تنسيق CSS مخصص للون الأزرق النيون والخلفية الداكنة
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #00D4FF;
        color: black;
        border-radius: 10px;
        border: none;
        box-shadow: 0 0 15px #00D4FF;
    }
    h1, h2, h3 {
        color: #00D4FF !important;
        font-family: 'Inter', sans-serif;
    }
    .neon-text {
        text-shadow: 0 0 10px #00D4FF;
    }
    </style>
    """, unsafe_allow_html=True)

# 2️⃣ القائمة الجانبية للتنقل (Navigation)
with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/artificial-intelligence.png") 
    st.title("Benidik AI")
    page = st.radio("انتقل إلى:", ["الرئيسية (Home)", "خدماتنا (Services)", "من نحن (About Us)", "تواصل معنا (Contact)"])
    st.markdown("---")
    # خانة الـ API Key لتفعيل ميزات الذكاء الاصطناعي
    api_key = st.text_input("OpenAI API Key", type="password")
    st.markdown("---")
    st.caption("© 2026 Benidik AI. All rights reserved.")

# ---------------------------------------------------------
# 3️⃣ محتوى الصفحات
# ---------------------------------------------------------

# --- 1️⃣ Home Page ---
if page == "الرئيسية (Home)":
    st.markdown("<h1 class='neon-text'>Benidik AI – Engineering Intelligent Growth</h1>", unsafe_allow_html=True)
    st.subheader("مستقبلك يبدأ هنا: نحن نحول التعقيد إلى ذكاء رقمي ينمو معك.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        مرحباً بك في **Benidik AI**. نحن وكالة رائدة في هندسة النمو الذكي عبر حلول الأتمتة والذكاء الاصطناعي المخصصة.
        نساعد الشركات على توفير الوقت، تقليل التكاليف، ومضاعفة الإنتاجية.
        """)
        # رابط واتساب مباشر
        st.markdown(f'''
            <a href="https://wa.me/212688421543" target="_blank">
                <button style="background-color: #00D4FF; color: black; padding: 10px 20px; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; box-shadow: 0 0 15px #00D4FF;">
                    🚀 احجز استشارة مجانية عبر واتساب
                </button>
            </a>
            ''', unsafe_allow_html=True)

    with col2:
        st.image("https://img.freepik.com/free-vector/artificial-intelligence-ai-robot-concept-illustration_114360-7522.jpg", use_column_width=True)

# --- 2️⃣ Services Page ---
elif page == "خدماتنا (Services)":
    st.title("🤖 خدماتنا الاحترافية")
    st.write("نقدم حلولاً برمجية ذكية مصممة خصيصاً لاحتياجات عملك:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 💬 Chatbots\nبناء وكلاء محادثة ذكية تفهم عملائك وترد عليهم على مدار الساعة.")
        st.info("### 🧠 Custom AI Tools\nتطوير أدوات ذكاء اصطناعي خاصة ببيانات شركتك.")
        
    with col2:
        st.info("### ⚙️ Automation\nربط الأنظمة وأتمتة المهام المتكررة لتوفير الوقت.")
        st.info("### 📊 AI Analytics\nتحليل بياناتك بعمق لاستخراج رؤى تسويقية دقيقة.")

# --- 3️⃣ About Us Page ---
elif page == "من نحن (About Us)":
    st.title("📖 قصة Benidik AI")
    st.write("نحن في **Benidik AI** نؤمن أن الذكاء الاصطناعي هو المحرك الجديد للاقتصاد العالمي.")
    st.markdown("### 👁️ الرؤية\nأن نكون الشريك التقني الأول للشركات الراغبة في قيادة المستقبل الرقمي.")

# --- 4️⃣ Contact Page ---
elif page == "تواصل معنا (Contact)":
    st.title("📞 دعنا نتحدث عن مشروعك القادم")
    
    col_info, col_form = st.columns([1, 2])
    
    with col_info:
        st.subheader("معلومات التواصل")
        st.write("📍 المقر الرئيسي: عن بُعد / المغرب")
        # إضافة الرقم في صفحة التواصل
        st.markdown("[![WhatsApp](https://img.icons8.com/color/48/000000/whatsapp.png)](https://wa.me/212688421543) **+212 688-421543**")
        st.write("📧 support@benidikai.com")

    with col_form:
        with st.form("contact_form"):
            name = st.text_input("الاسم")
            message = st.text_area("رسالتك")
            if st.form_submit_button("إرسال"):
                st.success("تم الاستلام! سنتواصل معك عبر واتساب أو البريد.")
