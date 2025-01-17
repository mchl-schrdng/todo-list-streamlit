import streamlit as st

def apply_theme(is_dark_mode):
    gradients = {
        "Light Mode": "linear-gradient(to right, #ff7e5f, #feb47b)",
        "Dark Mode": "linear-gradient(to right, #6441a5, #2a0845)"
    }

    selected_gradient = gradients["Dark Mode"] if is_dark_mode else gradients["Light Mode"]

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: {selected_gradient};
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )