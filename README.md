Adaptive Student Profiling Prototype:

  -->This project is a simple proof of concept (POC) for an adaptive student profiling system.
  -->The idea is to collect insights about a student’s knowledge level, learning style, and interests, and then generate a basic profile.
  -->It’s not meant to be a full product yet — just a prototype to demonstrate how such a system could work.

What it does:
  -->Knowledge Check (Grade 3 Science):Students answer 3 science questions. Their score decides whether they are Below Grade, At Grade, or Above Grade.
  -->Learning Style Identification:Students answer 2 questions about how they prefer to learn (Visual, Auditory, Kinesthetic, etc.).
  -->Interest Mapping:Students answer 2 fun questions to capture what excites them more (e.g., Space vs Animals).
  -->Profile Generation:At the end, the app shows a simple JSON-like profile

Tech Stack:
  -->Python 3
  -->Streamlit – for the interactive quiz app
  -->Custom JSON dataset – 15 questions (knowledge, style, interests)
  -->Simple scoring logic – no ML yet, just rule-based

How to run:
  -->Clone the repo or copy the project files.
  -->Install the requirements: pip install -r requirements.txt 
  -->Run the app: streamlit run app.py
  -->A browser window will open with the prototype.

Project Structure:

              |
              |---app.py                  #Main Streamlit app
              |---utils.py                #Loads dataset
              |---scorer.py               #Knowledge scoring logic
              |---profiler.py             #Learning style + profile builder
              |---questions.json          #Question dataset
              |---requirements.txt        #Python dependencies 
              |---Readme.md               # This file

Ideas for Future Work:
  -->Adaptive Questioning: dynamically pick the next question based on the student’s previous answer.
  -->Gamification: badges, progress bars, feedback messages.
  -->ML Integration: use NLP or recommendation models to refine student profiles.
  -->Larger Question Bank: import from Khan Academy or CK-12 to scale up.

Why this Project:
  -->This was built as a prototype task for exploring adaptive learning.
  -->The goal isn’t to replace a full system, but to show a direction:
         -->How we might profile students quickly,
         -->How we could personalize learning paths in the future.


