import streamlit as st

st.set_page_config(page_title="COMSATS GPA/CGPA Calculator", layout="centered")
st.title("🎓 COMSATS GPA & CGPA Calculator ")

st.markdown("""
Enter your **marks and credit hours** for each subject.  
This app automatically applies COMSATS grading policy and calculates **GPA** and **updated CGPA** accurately.
""")

# --- COMSATS Grade Conversion ---
def get_grade_point(percentage):
    if percentage >= 85:
        return 4.00
    elif percentage >= 80:
        return 3.67
    elif percentage >= 75:
        return 3.33
    elif percentage >= 70:
        return 3.00
    elif percentage >= 65:
        return 2.67
    elif percentage >= 61:
        return 2.33
    elif percentage >= 58:
        return 2.00
    elif percentage >= 55:
        return 1.67
    elif percentage >= 50:
        return 1.00
    else:
        return 0.00

# --- INPUT SECTION ---
num_subjects = st.number_input("Enter number of subjects this semester", min_value=1, step=1)

marks = []
credit_hours = []
st.markdown("---")

for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input(f"Marks (%) for Subject {i+1}", 0.0, 100.0, key=f"marks{i}")
    with col2:
        c = st.number_input(f"Credit Hours for Subject {i+1}", 1.0, 5.0, 3.0, key=f"credit{i}")
    marks.append(m)
    credit_hours.append(c)

# --- GPA CALCULATION ---
if st.button("Calculate GPA & CGPA"):
    total_qp = 0
    total_ch = 0
    st.markdown("### 📘 Subject-wise Details")
    st.write("")

    for i in range(int(num_subjects)):
        gp = get_grade_point(marks[i])
        total_qp += gp * credit_hours[i]
        total_ch += credit_hours[i]
        st.write(f"**Subject {i+1}:** Marks = {marks[i]} | Credit Hours = {credit_hours[i]} | Grade Point = {gp}")

    if total_ch == 0:
        st.warning("Please enter valid credit hours.")
    else:
        gpa = total_qp / total_ch
        st.success(f"🎯 Semester GPA: **{gpa:.2f}**")

        st.markdown("---")
        st.markdown("### 🧮 CGPA Calculation (Cumulative)")
        prev_cgpa = st.number_input("Enter previous CGPA (if any)", 0.0, 4.0, 0.0)
        prev_credits = st.number_input("Enter total credit hours completed before this semester", 0.0, 200.0, 0.0)

        total_qp_all = (prev_cgpa * prev_credits) + (gpa * total_ch)
        total_ch_all = prev_credits + total_ch
        cgpa = total_qp_all / total_ch_all if total_ch_all > 0 else 0

        st.success(f"🏆 Updated CGPA: **{cgpa:.2f}**")
        st.markdown(f"**Total Credit Hours:** {total_ch_all}")
