import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one special character (!@#$%^&*).")

    # Scoring System
    if score == 5:
        return "🟢 Strong Password ✅", feedback
    elif score >= 3:
        return "🟡 Moderate Password ⚠️", feedback
    else:
        return "🔴 Weak Password ❌", feedback

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    st.subheader(strength)

    if feedback:
        for f in feedback:
            st.write(f)
    else:
        st.success("Your password is strong! ✅")
