import streamlit as st

# Add a fun, vibrant background using custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #e0e7ff 0%, #f3e7e9 100%) !important;
    }
    .stApp {
        background: linear-gradient(135deg, #e0e7ff 0%, #f3e7e9 100%) !important;
    }
    .fun-bg {
        background: repeating-radial-gradient(circle at 80% 20%, #fbbf24 0, #fbbf24 12px, transparent 14px, transparent 40px),
                    repeating-radial-gradient(circle at 20% 80%, #10b981 0, #10b981 14px, transparent 16px, transparent 50px),
                    linear-gradient(120deg, #6366f1 0%, #f472b6 100%);
        border-radius: 0 0 2rem 2rem;
        padding-bottom: 2rem;
    }
    .fun-card {
        background: linear-gradient(120deg, #fff7ed 60%, #a5b4fc 100%);
        box-shadow: 0 2px 16px rgba(60,60,60,0.10);
        border-radius: 1.2rem;
        padding: 2rem 2rem 1.5rem 2rem;
        margin-top: 1rem;
    }
    .fun-form input, .fun-form select {
        border-radius: 1rem !important;
        border: 1.5px solid #6366f1 !important;
        background: #f3f4f6 !important;
    }
    .impact-card {
        background: linear-gradient(90deg, #fbbf24 60%, #10b981 100%);
        color: #22223b;
        border-radius: 1rem;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 2px 8px #fbbf2433;
        display: inline-block;
    }
    .testimonial {
        background: #fff;
        border-left: 6px solid #6366f1;
        border-radius: 1rem;
        padding: 1.1rem 1.5rem;
        margin-bottom: 1.2rem;
        font-style: italic;
        box-shadow: 0 2px 8px #6366f133;
    }
    .how-works {
        background: linear-gradient(90deg, #a5b4fc 60%, #f472b6 100%);
        border-radius: 1rem;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
        color: #22223b;
        font-size: 1.05rem;
        box-shadow: 0 2px 8px #a5b4fc33;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main header section with fun background
st.markdown(
    """
    <div class="fun-bg" style="background: linear-gradient(90deg, #3b82f6 0%, #9333ea 100%); padding: 2.5rem 0 1.5rem 0; border-radius: 0 0 2rem 2rem; position: relative; overflow: hidden;">
        <h1 style="color: white; font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;">Unlock Your Potential This Summer</h1>
        <p style='color: #e0e7ef; font-size: 1.1rem; margin-bottom: 1.5rem;'>Join the Black at Microsoft program and help students gain valuable new skills</p>
        <a href="#signup" style="background: #fd7e14; color: white; padding: 0.75rem 2rem; border-radius: 2rem; font-weight: 600; text-decoration: none; font-size: 1.1rem;">Sign Up for Coaching</a>
        <img src="MyImages/A colorful and visually appealing web page mockup for additional coaching and tutor sign-up for the .jpeg" alt="Coaching Illustration" style="float: right; width: 320px; margin-top: -120px; margin-right: 2rem; border-radius: 1.5rem; box-shadow: 0 4px 24px rgba(0,0,0,0.08);">
        <div style="position: absolute; left: -60px; top: 40px; width: 120px; height: 120px; background: #fbbf24; border-radius: 50%; opacity: 0.18;"></div>
        <div style="position: absolute; right: -80px; bottom: -40px; width: 180px; height: 180px; background: #a5b4fc; border-radius: 50%; opacity: 0.13;"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# About Coaching section and layout using Streamlit columns
col1, col2, col3 = st.columns([1, 1.2, 1])

with col1:
    st.markdown("<h2 style='color: #22223b; font-size: 1.5rem; margin-bottom: 1.2rem;'>About Coaching</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; align-items: flex-start; margin-bottom: 1.2rem; background: #fbbf24; border-radius: 1rem; padding: 0.7rem 1rem; box-shadow: 0 2px 8px #fbbf2433;">
        <img src='https://img.icons8.com/color/48/000000/student-male--v2.png' style='margin-right: 1rem;'/>
        <div>
            <b>Make an Impact</b><br>
            <span style='font-size: 0.98rem;'>Help students reach their academic and career goals</span>
        </div>
    </div>
    <div style="display: flex; align-items: flex-start; margin-bottom: 1.2rem; background: #10b981; border-radius: 1rem; padding: 0.7rem 1rem; box-shadow: 0 2px 8px #10b98133; color: #fff;">
        <img src='https://img.icons8.com/color/48/000000/handshake.png' style='margin-right: 1rem;'/>
        <div>
            <b>One-on-One Support</b><br>
            <span style='font-size: 0.98rem;'>Deliver personalized guidance and mentorship</span>
        </div>
    </div>
    <div style="display: flex; align-items: flex-start; background: #f472b6; border-radius: 1rem; padding: 0.7rem 1rem; box-shadow: 0 2px 8px #f472b633; color: #fff;">
        <img src='https://img.icons8.com/color/48/000000/classroom.png' style='margin-right: 1rem;'/>
        <div>
            <b>Share Your Expertise</b><br>
            <span style='font-size: 0.98rem;'>Tutor students in STEM or business-related fields</span>
        </div>
    </div>
    <div class="impact-card">🎉 120+ students mentored last year!</div>
    <div class="impact-card">🌟 90% of students felt more confident after coaching</div>
    <div class="impact-card">🤝 50+ active volunteer coaches</div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="how-works"><b>How Coaching Works:</b><br>'
        '<ul style="margin: 0.5rem 0 0 1.2rem;">'
        '<li><b>Sign Up:</b> Fill out the form to express your interest.</li>'
        '<li><b>Get Matched:</b> We pair you with a student based on your interests and availability.</li>'
        '<li><b>Meet & Mentor:</b> Connect virtually for one-on-one or group sessions.</li>'
        '<li><b>Grow Together:</b> Share knowledge, set goals, and celebrate progress!</li>'
        '</ul></div>', unsafe_allow_html=True)
    st.markdown('<div class="testimonial">“The coaching I received helped me land my first internship and boosted my confidence!”<br><span style="font-size:0.95em; color:#6366f1;">– Student, 2024</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="testimonial">“I gained so much confidence and learned how to tackle real-world problems.”<br><span style="font-size:0.95em; color:#6366f1;">– Student, 2023</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="testimonial">“Being a coach let me give back and inspire the next generation of tech leaders.”<br><span style="font-size:0.95em; color:#10b981;">– Volunteer Coach</span></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="fun-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #22223b; font-size: 1.4rem; margin-bottom: 1.2rem;">Tutor Sign-Up</h2>', unsafe_allow_html=True)
    with st.form(key="tutor_signup_form"):
        st.markdown('<div class="fun-form">', unsafe_allow_html=True)
        name = st.text_input("Name")
        email = st.text_input("Email")
        area = st.selectbox("Area of interest", ["STEM", "Business", "Other"])
        availability = st.text_input("Availability (e.g. evenings, weekends)")
        submit = st.form_submit_button("Submit")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if 'submit' in locals() and submit:
    st.success(f"Thank you, {name}! Your sign-up has been received.")
    st.balloons()

# Streamlit form for Tutor Sign-Up (styled)
with st.form(key="tutor_signup_form"):
    st.markdown('<div class="fun-form">', unsafe_allow_html=True)
    name = st.text_input("Name")
    email = st.text_input("Email")
    area = st.selectbox("Area of interest", ["STEM", "Business", "Other"])
    availability = st.text_input("Availability (e.g. evenings, weekends)")
    submit = st.form_submit_button("Submit")
    st.markdown('</div>', unsafe_allow_html=True)

if 'submit' in locals() and submit:
    st.success(f"Thank you, {name}! Your sign-up has been received.")
    st.balloons()