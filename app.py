import streamlit as st 
from utils import load_questions 
from scorer import score_knowledge 
from profiler import determine_learning_style,build_profile 

st.title("ADAPTIVE STUDENT PROFILING PROTOTYPE")

dataset=load_questions()

st.header("Knowledge Questions")
knowledge_answers={}
for q in dataset['knowledge'][:3]:
    ans=st.radio(q['question'],q['choices'],key=q['id'],index=None)
    if ans is not None:
        knowledge_answers[q["id"]] = q['choices'].index(ans)
    else:
        knowledge_answers[q["id"]] = None

st.header("Learning Style Questions")
style_answers=[]
for q in dataset['learning_style']:
    ans=st.radio(q['question'],q['choices'],key=q['id'],index=None)
    style_answers.append(ans)

st.header("Interest Questions")
interest_answers=[]
for q in dataset['interests']:
    ans=st.radio(q['question'],q['choices'],key=q['id'],index=None)
    interest_answers.append(ans)

if st.button("Submit"):
    if None in knowledge_answers.values() or None in style_answers or None in interest_answers:
        st.error("Please answer all questions before submitting.")
    else:
        knowledge_level = score_knowledge(knowledge_answers, dataset)
        learning_style = determine_learning_style(style_answers)
        profile = build_profile(knowledge_level, learning_style, interest_answers)

        st.subheader("Student Profile")
        st.json(profile)



