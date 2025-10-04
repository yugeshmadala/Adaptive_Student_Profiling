def score_knowledge(answers,dataset):
    score=0
    for q_id,ans in answers.items():
        for q in dataset['knowledge']:
            if q['id']==q_id and ans==q['answer']:
                score=score+1
    if score<=1:
        return "Below Grade"
    elif score==2:
        return "At Grade"
    else:
        return "Above Grade"
    

