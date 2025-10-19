import streamlit as st

# -----------------------------------------
# Page setup
# -----------------------------------------
st.set_page_config(page_title="COMSATS GPA & CGPA Calculator", layout="centered")
st.title("🎓 COMSATS GPA & CGPA Calculator")

st.markdown("""
Enter your **marks and credit hours** for each subject.  
This app calculates **Semester GPA** and **CGPA** according to the COMSATS official grading policy.
""")

# -----------------------------------------
# Grade mapping
# -----------------------------------------
def get_grade_point(percentage):
    if percentage >= 85:
        return 4.00, "A"
    elif percentage >= 80:
        return 3.67, "A-"
    elif percentage >= 75:
        return 3.33, "B+"
    elif percentage >= 70:
        return 3.00, "B"
    elif percentage >= 65:
        return 2.67, "B-"
    elif percentage >= 61:
        return 2.33, "C+"
    elif percentage >= 58:
        return 2.00, "C"
    elif percentage >= 55:
        return 1.67, "C-"
    elif percentage >= 50:
        return 1.00, "D"
    else:
        return 0.00, "F"

# -----------------------------------------
# Maintain state for number of subjects
# -----------------------------------------
if "num_subjects" not in st.session_state:
    st.session_state.num_subjects = 1

num_subjects = st.number_input(
    "Enter number of subjects this semester", 
    min_value=1, step=1, value=st.session_state.num_subjects
)
st.session_state.num_subjects = num_subjects

# -----------------------------------------
# Dynamic inputs (safe using session state)
# -----------------------------------------
marks = []
credits = []

st.markdown("---")
st.subheader("📘 Enter Subject Details")

for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input(f"Marks (%) for Subject {i+1}", 0.0, 100.0, key=f"m{i}")
    with col2:
        c = st.number_input(f"Credit Hours for Subject {i+1}", 1.0, 5.0, 3.0, key=f"c{i}")
    marks.append(m)
    credits.append(c)

# -----------------------------------------
# GPA Calculation
# -----------------------------------------
if st.button("Calculate GPA & CGPA"):
    total_qp = 0
    total_ch = 0

    st.markdown("### 📊 Subject Summary")
    for i in range(int(num_subjects)):
        gp, grade = get_grade_point(marks[i])
        total_qp += gp * credits[i]
        total_ch += credits[i]
        st.write(
            f"**Subject {i+1}:** Marks = {marks[i]} | Credit Hours = {credits[i]} | Grade = {grade} | Grade Point = {gp}"
        )

    if total_ch > 0:
        gpa = total_qp / total_ch
        st.success(f"🎯 Semester GPA: **{gpa:.2f}**")

        # Optional CGPA
        st.markdown("---")
        st.subheader("🧮 CGPA Update (Optional)")
        prev_cgpa = st.number_input("Enter previous CGPA (if any)", 0.0, 4.0, 0.0)
        prev_credits = st.number_input("Enter total previous credit hours", 0.0, 200.0, 0.0)

        total_qp_all = (prev_cgpa * prev_credits) + (gpa * total_ch)
        total_ch_all = prev_credits + total_ch
        cgpa = total_qp_all / total_ch_all if total_ch_all > 0 else 0
        st.success(f"🏆 Updated CGPA: **{cgpa:.2f}**")
    else:
        st.warning("Please enter valid marks and credit hours.")
