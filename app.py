import streamlit as st

# ---------------------------------------------
# Streamlit Configuration
# ---------------------------------------------
st.set_page_config(page_title="🎓 COMSATS GPA & CGPA Calculator", layout="centered")

st.title("🎓 COMSATS University GPA & CGPA Calculator")
st.caption("Based on Official Grading Policy ")

# ---------------------------------------------
# COMSATS Grading Scale (Official Approximation)
# ---------------------------------------------
def percentage_to_gpa(percentage):
    if percentage >= 86:
        return 4.00
    elif 82 <= percentage <= 85:
        return 3.70
    elif 78 <= percentage <= 81:
        return 3.30
    elif 74 <= percentage <= 77:
        return 3.00
    elif 70 <= percentage <= 73:
        return 2.70
    elif 66 <= percentage <= 69:
        return 2.30
    elif 62 <= percentage <= 65:
        return 2.00
    elif 58 <= percentage <= 61:
        return 1.70
    elif 54 <= percentage <= 57:
        return 1.30
    elif 50 <= percentage <= 53:
        return 1.00
    else:
        return 0.00

# ---------------------------------------------
# GPA Calculation Section
# ---------------------------------------------
st.header("📘 Semester GPA Calculator")

num_subjects = st.number_input("Number of subjects this semester:", min_value=1, step=1)

subject_data = []
for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)
    with col1:
        marks = st.number_input(f"Marks for Subject {i+1} (%)", min_value=0.0, max_value=100.0, key=f"marks_{i}")
    with col2:
        credit = st.number_input(f"Credit Hours for Subject {i+1}", min_value=0.5, step=0.5, key=f"credit_{i}")
    subject_data.append((marks, credit))

if st.button("Calculate GPA"):
    total_quality_points = 0
    total_credits = 0
    for marks, credit in subject_data:
        gpa = percentage_to_gpa(marks)
        total_quality_points += gpa * credit
        total_credits += credit
    semester_gpa = total_quality_points / total_credits if total_credits > 0 else 0
    st.success(f"✅ Your Semester GPA is: **{semester_gpa:.2f}**")

# ---------------------------------------------
# CGPA Calculation Section
# ---------------------------------------------
st.header("📚 CGPA Calculator")

prev_semesters = st.number_input("Number of previous semesters:", min_value=0, step=1)

prev_data = []
for i in range(int(prev_semesters)):
    col1, col2 = st.columns(2)
    with col1:
        prev_gpa = st.number_input(f"GPA for Semester {i+1}", min_value=0.0, max_value=4.0, key=f"prev_gpa_{i}")
    with col2:
        prev_credit = st.number_input(f"Total Credit Hours for Semester {i+1}", min_value=1.0, step=0.5, key=f"prev_credit_{i}")
    prev_data.append((prev_gpa, prev_credit))

if st.button("Calculate CGPA"):
    total_quality_points = sum(g * c for g, c in prev_data)
    total_credits = sum(c for _, c in prev_data)

    # Include current semester GPA if calculated
    if 'semester_gpa' in locals():
        current_credits = sum(c for _, c in subject_data)
        total_quality_points += semester_gpa * current_credits
        total_credits += current_credits

    cgpa = total_quality_points / total_credits if total_credits > 0 else 0
    st.success(f"📊 Your Cumulative CGPA is: **{cgpa:.2f}**")
