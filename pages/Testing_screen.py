import google.generativeai  as genai
import streamlit as st
import datetime as dt
import os
import Consistancy_tables as su    #short for Sending_utility
def get_mykey():
    found = 0
    dir_per =""
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        if "api_key.txt" in filenames:
            found = 1
            dir_per = dirpath
            break
    if found == 1:
        with open(os.path.join(dir_per, "api_key.txt")) as f:
            api_k = f.readlines()
        return api_k[0].replace("\n","")
    else:
        st.error("No api_key.txt found")
        st.stop()
        return None

api_key_from_func = get_mykey()
if api_key_from_func is None:
    st.error("No api_key.txt found in the current directory.\n Please make sure that api_key.txt is present in the current directory")
    st.stop()
else:
    genai.configure(api_key=api_key_from_func)

def evaluate_and_send():
    overall_score = 0 # 1 or 2
    if "suggestions_learning" in st.session_state:
        if st.session_state.suggestions_learning is not None and len(st.session_state.suggestions_learning) > 0:
            the_suggestion_1 = ". ".join(st.session_state.suggestions_learning[0:])
            the_suggestion = "".join([s for s in the_suggestion_1.splitlines(True) if s.strip("\r\n")])
            the_suggestion = the_suggestion.replace('"'," ")
            the_suggestion = the_suggestion.replace("'"," ")
    if "Marks_learning" in st.session_state:
        if st.session_state.Marks_learning is not None:
            overall_score = st.session_state.Marks_learning
            if overall_score <30:
                my_score = 0
            elif 30< overall_score <89:
                my_score = 1
            else:
                my_score = 2

    if "studies" in st.session_state:
        my_topic = st.session_state.studies
    if my_topic is not None and my_score is not None and the_suggestion is not None:

        Query = f"Insert into my_progress (The_topic,The_test_result, The_suggestion) values ('{my_topic}',{my_score},'{str(the_suggestion)}')"
        db, cur =su.connnecting()
        try:
            cur.execute(Query)
            db.commit()
            st.success(f"Query executed {Query}")
        except Exception as e:
            st.error(e)
        finally:
            db.close()
    if "studies" in st.session_state and len(st.session_state.studies) > 0:
        st.session_state["studies"] = ""
    delete_from_sessionstate()

def delete_from_sessionstate():
    if "suggestions_learning" in st.session_state:
        del st.session_state["suggestions_learning"]
    if "Marks_learning" in st.session_state:
        del st.session_state["Marks_learning"]
    if "Questions_learning" in st.session_state:
        del st.session_state["Questions_learning"]

def Evaluate_new(topic, old_topic):
    if topic != "":
        delete_from_sessionstate()
        if st.session_state.studies == old_topic:
            st.session_state.studies = topic
def Redo_Assesment():
    delete_from_sessionstate()
    
class My_EVAL:
    Questions = []
    Answer_user = []

    def generate_Quetions(self, topic):
        # first Question will be easy
        generation_config = {
          "temperature": 0.9,
          "top_p": 0.95,
          "top_k": 64,
          "max_output_tokens": 8192,
          "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config)
        prompt_gen_all_questions_end_with_special_char = f"Generate 1 easy,2 medium and 2 difficult Questions, the topic is {topic}, make sure that each Question can be answered within 100 words and you can test them later. All Questions must be dissimilar to cover diverse range in the topic. separate each Question by characters- 'END1:STA2' only and no need to specify anything else. "
        character = "END1:STA2"
        res = model.generate_content(prompt_gen_all_questions_end_with_special_char)
        self.Questions = res.text.split(character)
        
    def Evaluate_Answer_user(self,specific_question,the_usr_answer):
        generation_config = {
          "temperature": 0.9,
          "top_p": 0.95,
          "top_k": 64,
          "max_output_tokens": 8192,
          "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config)
        prompt_to_evaluate = f"evaluate,only say one word correct or incorrect my answer : {the_usr_answer} for the Question: {specific_question}.Consider various answer formats (e.g., single words, phrases, sentences) and context. Please be generous and only say incorrect when the factual or logical aspect of answer is clearly wrong."
        res = model.generate_content(prompt_to_evaluate)
        my_eval = {
            "Correctedness": res.text
        }

        if "incorrect" in my_eval["Correctedness"] or "Incorrect" in my_eval["Correctedness"]:
            correct_answer = model.generate_content(f"I gave an incorrect answer for the question: {specific_question}. My answer was {the_usr_answer}. What is the correct answer?")
            suggestions = model.generate_content(f"I gave an incorrect answer for the question: {specific_question}. My answer was {the_usr_answer}. What did i miss to get it wrong? What further improvements can be done to learn better?")
            my_eval["suggestions"] = suggestions.text
            my_eval["correct_answer"] = correct_answer.text
            
            return my_eval, 3
        elif "correct" in my_eval["Correctedness"] or "Correct" in my_eval["Correctedness"]:
            improvements = model.generate_content(f"My answer is correct,do you want to add something to it? My answer is: {the_usr_answer}, the question is: {specific_question}")
            my_eval["suggestions"] = improvements.text
            
            return my_eval, 2
        return my_eval,0
if "studies" in st.session_state and len(st.session_state.studies) > 0:
    if "Questions_learning" not in st.session_state:
        this_instance_evaluation = My_EVAL()
        this_instance_evaluation.generate_Quetions(st.session_state.studies)
        st.session_state.Questions_learning = this_instance_evaluation.Questions    
    st.write(st.session_state)
    @st.fragment()
    def take_answers():
        for i in range(len(st.session_state.Questions_learning)):
            with st.form(f"form {i}"):
                st.write(st.session_state.Questions_learning[i])
                answer = st.text_area("Your answer for "+ str(i))
                submit = st.form_submit_button("Check answer" +str(i))
                if submit:
                    eval, score = this_instance_evaluation.Evaluate_Answer_user(st.session_state.Questions_learning[i],answer)
                    st.write(eval)
                    if score == 2:
                        if "suggestions_learning" not in st.session_state:
                            st.session_state.suggestions_learning = []
                        st.session_state.suggestions_learning.append(eval["suggestions"])
                        if "Marks_learning" not in st.session_state:
                            st.session_state.Marks_learning = 10
                        elif i==0:
                            st.session_state.Marks_learning += 10
                        elif i== 1 or i== 2:
                            st.session_state.Marks_learning += 20
                        elif i== 3 or i== 4:
                            st.session_state.Marks_learning += 25
                    if score == 3:
                        if "suggestions_learning" not in st.session_state:
                            st.session_state.suggestions_learning = []
                        st.session_state.suggestions_learning.append(eval["suggestions"])
                        st.session_state.suggestions_learning.append(eval["correct_answer"])
                    st.write(score)
               
    take_answers()
    # work with Questions
    col1,col2,col3 = st.columns([1,3,1])
    submit_eval =col1.button("Submit evaluation")
    # delete everything from session state
    if submit_eval:
        evaluate_and_send()
    redo = col3.button("Clear evaluation",on_click= Redo_Assesment)
    # delete everything except for topic

    new_topic = col2.text_input("Add New topic")
    new_true = col2.button("Add new topic", on_click=Evaluate_new, args=(new_topic, st.session_state.studies))
    # delete Questions and change topic
    

    st.write(st.session_state)
else:
    # say that you should ho to generate the studies in main app 
    st.write("Go to main app and generate topic")
    st.page_link( "pages/Main_app.py",label="Go to main app",icon="🏠")

    
# make a functionality in streamlit to evaluate based on Session state then clear it on button cli

