import streamlit as st
# Title
st.title("Student Mark Calculator")
# Input from user
name = st.text_input("Enter your name")
mark1 = st.number_input("Enter Maths mark")
mark2 = st.number_input("Enter Science mark")
# Button
if st.button("Calculate Average"):
    average = (mark1 + mark2) / 2
    st.write("Student Name:", name)
    st.write("Average Mark:", average)
    # Grade
    if average >= 90:
        st.success("Grade A")
    elif average >= 75:
        st.success("Grade B")
    elif average >= 50:
        st.warning("Grade C")
    else:
        st.error("Fail")
