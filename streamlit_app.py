import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Personal Skill Gap Analyzer")

st.write(
    "Discover your skills and build your career roadmap!"
)

st.divider()

st.header("👨‍🎓 Student Details")

name = st.text_input("Enter Your Name")

career = st.selectbox(
    "Select Your Dream Career",
    ["Data Analyst", "Data Scientist",
     "AI Engineer", "Business Analyst"]
)

st.divider()

st.header("📊 Skill Assessment")

python = st.slider("Python", 0, 100, 30)
sql = st.slider("SQL", 0, 100, 40)
excel = st.slider("Excel", 0, 100, 20)
powerbi = st.slider("Power BI", 0, 100, 10)

if st.button("Analyze My Skills 🚀"):

    st.subheader("Your Skill Analysis")

    skills = {
        "Python": python,
        "SQL": sql,
        "Excel": excel,
        "Power BI": powerbi
    }

    required = {
        "Python": 80,
        "SQL": 90,
        "Excel": 80,
        "Power BI": 80
    }

    average = sum(skills.values()) / 4

    st.metric("Overall Skill Score", f"{average:.1f}%")

    st.subheader("Skill Gap Report")

    for skill in skills:

        gap = required[skill] - skills[skill]

        if gap > 0:
            st.warning(
                f"{skill}: Improve by {gap}%"
            )
        else:
            st.success(f"{skill}: Target achieved!")

    st.subheader("📈 Skill Comparison")

    st.bar_chart({
        "Current Skills": skills,
        "Required Skills": required
    })

    st.subheader("💡 Learning Recommendations")

    for skill in skills:

        if skills[skill] < 40:
            st.write(f"📘 Learn {skill} from basics")

        elif skills[skill] < 70:
            st.write(f"📗 Practice {skill} regularly")

        else:
            st.write(f"🏆 Improve advanced {skill} skills")

    st.success(
        f"Great {name}! Your career goal is {career}."
    )
st.divider()

st.header("🎯 Career Readiness Prediction")

readiness = (
    (min(python, 80) / 80 +
     min(sql, 90) / 90 +
     min(excel, 80) / 80 +
     min(powerbi, 80) / 80) / 4
) * 100

st.metric(
    "Career Readiness Score",
    f"{readiness:.1f}%"
)

if readiness >= 75:
    st.success("🟢 You are Job Ready!")
elif readiness >= 50:
    st.warning("🟡 You are Almost Ready!")
else:
    st.error("🔴 You Need More Training!")

st.progress(int(readiness))
st.divider()

st.subheader("📊 Skill-wise Performance")

st.write(f"Python: {python}%")
st.write(f"SQL: {sql}%")
st.write(f"Excel: {excel}%")
st.write(f"Power BI: {powerbi}%")
st.subheader("📈 Skill Comparison")

skill_data = {
    "Python": python,
    "SQL": sql,
    "Excel": excel,
    "Power BI": powerbi
}

st.bar_chart(skill_data, horizontal=True)
st.divider()

st.subheader("🎯 Skill Gap Summary")

required = {
    "Python": 80,
    "SQL": 90,
    "Excel": 80,
    "Power BI": 80
}

for skill, score in skill_data.items():
    gap = max(0, required[skill] - score)
    st.write(f"{skill} - Need to improve: {gap}%")
st.divider()

st.subheader("📅 Your 7-Day Learning Plan")

if readiness < 50:
    st.write("Day 1: Python Basics")
    st.write("Day 2: SQL Basics")
    st.write("Day 3: Excel Basics")
    st.write("Day 4: Power BI Basics")
    st.write("Day 5: Python Practice")
    st.write("Day 6: SQL Practice")
    st.write("Day 7: Mini Project")

else:
    st.write("Day 1: Advanced Python")
    st.write("Day 2: SQL Queries")
    st.write("Day 3: Excel Dashboard")
    st.write("Day 4: Power BI Dashboard")
    st.write("Day 5: Data Analysis")
    st.write("Day 6: Mini Project")
    st.write("Day 7: Interview Preparation")
