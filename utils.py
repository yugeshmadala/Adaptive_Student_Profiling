import json 

def load_questions(path="datasets/questions.json"):
    with open(path,"r") as f:
        return json.load(f)
    
