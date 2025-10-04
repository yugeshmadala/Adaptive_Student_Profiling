def determine_learning_style(style_answers):
    counts = {"Visual": 0, "Auditory": 0, "Read/Write": 0, "Kinesthetic": 0}
    for ans in style_answers:
        if ans in ["Watching a video", "Pictures"]:
            counts["Visual"]=counts['Visual']+1
        elif ans in ["Listening"]:
            counts["Auditory"]=counts["Auditory"]+1
        elif ans in ["Reading a book"]:
            counts["Read/Write"]=counts["Read/Write"]+1
        elif ans in ["Doing an experiment", "Hands-on practice"]:
            counts["Kinesthetic"]=counts["Kinesthetic"]+1
    return max(counts, key=counts.get)

def build_profile(knowledge_level,learning_style,interests):
    return {
        "Proficiency_Level":knowledge_level,
        "Learning_Style":learning_style,
        "Interests":interests
    }

