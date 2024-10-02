import streamlit as st
import time

# Initialize session state variables
if 'projects' not in st.session_state:
    st.session_state.projects = []
if 'studies' not in st.session_state:
    st.session_state.studies = ""


# Function to add project
def add_project(name, topic, description):
    st.session_state.projects={
        'name': name,
        'topic': topic,
        'description': description # this will be what i did
    }
    st.success("Project added!")
    time.sleep(2)
    st.switch_page("pages/project_evaluation.py")


# Function to add study topic
def add_study(topic):
    st.session_state.studies = topic
    st.success("Study topic added!")
    time.sleep(2)
    st.switch_page("pages/Testing_screen.py")

# Function to listen to struggles
def listen_to_struggles():
    # Logic for navigating to the struggles page can be implemented here
    st.write("Navigating to Listen to My Struggles Page...")
    # Here you can add further functionality or navigation

# Set the title of the app
st.title("What did you do today?")

# Section for Work & Projects
st.header("Work & Projects")
work_projects = st.checkbox("Did you work on any projects?")

if work_projects:
    with st.form(key='project_form'):
        project_name = st.text_input("Project Name")
        project_topic = st.text_input("Project Topic")
        project_description = st.text_area("What did you do?")
        submit_button = st.form_submit_button("Test what i learnt")

    if submit_button:
        add_project(project_name, project_topic, project_description)
        #st.switch_page("Project_based_testing.py")


# Section for Study & Skills
st.header("Study & Skills")
study_skills = st.checkbox("Did you study any new skills?")

if study_skills:
    with st.form(key='study_form'):
        study_topic = st.text_input("What topic did you study?")
        study_submit_button = st.form_submit_button("Test my understanding" )

    if study_submit_button:
        add_study(study_topic)


# Navigation Buttons
st.header("What else?")
if st.button("Thought of some more ideas"):
    # Here you can define navigation to the ideas page
    st.write("Navigating to Ideas Page...")
    time.sleep(3)
    st.switch_page("pages//Idea_management.py")
    # Implement navigation logic or create a new function/page as needed

if st.button("Listen to my struggles"):
    st.write("Navigating to Chat Page...")
    time.sleep(3)
    st.switch_page("pages/Struggles.py") # Call the function to navigate or listen to struggles

if st.button("Nothing, I need motivation"):
    # Here you can define navigation to the motivation page
    st.write("Navigating to Motivation Page...")
    # Implement navigation logic or create a new function/page as needed



