import streamlit as st
import pandas as pd

# ----------------------------------------
# COMSATS University Lahore Grading System
# ----------------------------------------
def get_grade_point(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0

# ----------------------------------------
# Streamlit Page Config
# ----------------------------------------
st.set_page_config(page_title="🎓 COMSATS GPA & CGPA Calculator", layout="centered")

st.title("🎓 COMSATS University Lahore - GPA & CGPA Calculator")
st.markdown("---")

# ----------------------------------------
# Input Section
# ----------------------------------------
st.subheader("📘 Enter Your Subject Details")

num_subjects = st.number_input("How many subjects do you have this semester?", min_value=1, step=1)

subjects = []
total_credit_hours = 0
total_quality_points = 0

if num_subjects:
    st.write("### 🧾 Enter Marks and Credit Hours")
    for i in range(num_subjects):
        col1, col2, col3 = st.columns(3)
        with col1:
            subject = st.text_input(f"Subject {i+1} Name", key=f"sub_{i}")
        with col2:
            marks = st.number_input(f"Marks ({subject})", min_value=0.0, max_value=100.0, step=0.5, key=f"marks_{i}")
        with col3:
            credit_hours = st.number_input(f"Credit Hours ({subject})", min_value=1.0, max_value=4.0, step=0.5, key=f"ch_{i}")
        
        grade_point = get_grade_point(marks)
        quality_points = grade_point * credit_hours
        total_credit_hours += credit_hours
        total_quality_points += quality_points
        
        subjects.append({
            "Subject": subject,
            "Marks": marks,
            "Credit Hours": credit_hours,
            "Grade Point": grade_point
        })

    # ----------------------------------------
    # GPA Calculation
    # ----------------------------------------
    if total_credit_hours > 0:
        gpa = total_quality_points / total_credit_hours
        st.markdown("---")
        st.subheader("📊 GPA Calculation Result")
        df = pd.DataFrame(subjects)
        st.dataframe(df, use_container_width=True)
        st.success(f"🎯 **Your Semester GPA = {gpa:.2f}**")

        # ----------------------------------------
        # CGPA Calculation
        # ----------------------------------------
        st.markdown("---")
        st.subheader("📈 CGPA Calculation")
        prev_cgpa = st.number_input("Enter your Previous CGPA (if any)", min_value=0.0, max_value=4.0, step=0.01)
        prev_credit_hours = st.number_input("Enter your Total Previous Credit Hours", min_value=0.0, step=1.0)
        
        if st.button("Calculate CGPA"):
            if prev_credit_hours > 0:
                cgpa = (prev_cgpa * prev_credit_hours + gpa * total_credit_hours) / (prev_credit_hours + total_credit_hours)
            else:
                cgpa = gpa

            st.success(f"🏆 **Your Updated CGPA = {cgpa:.2f}**")
