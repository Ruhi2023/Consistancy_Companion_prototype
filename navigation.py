import streamlit as st
nav = st.navigation({
    "Home": [st.Page("pages/Main_app.py")],
    "Evaluation": [st.Page("pages/Testing_screen.py"),st.Page("pages/project_evaluation.py")],
    "Improvement":[st.Page("pages/Idea_management.py"), st.Page("pages/Struggles.py"), st.Page("pages/Improv_sug.py")]
})
nav.run()