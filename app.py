import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", layout="centered")
st.title("🎓 GPA & CGPA Calculator")
st.caption("Enter your academic results to calculate GPA and CGPA")

# Function to calculate GPA
def calculate_gpa(courses):
    total_quality_points = sum(gp * credit for _, _, _, gp, credit in courses)
    total_credits = sum(credit for _, _, _, _, credit in courses)
    return round(total_quality_points / total_credits, 2) if total_credits > 0 else 0.0

# Input number of semesters
num_semesters = st.number_input("Number of semesters to enter:", min_value=1, step=1)

all_courses = []
semester_gpas = []

for sem in range(int(num_semesters)):
    st.subheader(f"📘 Semester {sem+1}")
    num_courses = st.number_input(f"Number of courses in Semester {sem+1}:", min_value=1, step=1, key=f"num_courses_{sem}")
    
    semester_courses = []
    for i in range(int(num_courses)):
        col1, col2 = st.columns([2, 2])
        with col1:
            course_title = st.text_input(f"Course {i+1} Title", key=f"title_{sem}_{i}")
            marks = st.number_input(f"Marks (%)", min_value=0.0, max_value=100.0, key=f"marks_{sem}_{i}")
        with col2:
            grade_point = st.number_input(f"Grade Point", min_value=0.0, max_value=4.0, step=0.01, key=f"gp_{sem}_{i}")
            credit = st.number_input(f"Credit Hours", min_value=0.5, step=0.5, key=f"credit_{sem}_{i}")
        semester_courses.append((f"SEM{sem+1}", course_title, marks, grade_point, credit))
    
    gpa = calculate_gpa(semester_courses)
    semester_gpas.append((gpa, sum(course[4] for course in semester_courses)))
    all_courses.extend(semester_courses)
    st.success(f"GPA for Semester {sem+1}: **{gpa}**")

# CGPA Calculation
if st.button("Calculate CGPA"):
    total_quality_points = sum(gpa * credits for gpa, credits in semester_gpas)
    total_credits = sum(credits for _, credits in semester_gpas)
    cgpa = round(total_quality_points / total_credits, 2) if total_credits > 0 else 0.0
    st.header("📊 Cumulative GPA")
    st.success(f"Your CGPA is: **{cgpa}**")

    with st.expander("📋 View Full Course Breakdown"):
        for sem, title, marks, gp, credit in all_courses:
            st.write(f"{sem} | {title} | Marks: {marks}% | GPA: {gp} | Credit: {credit}")

