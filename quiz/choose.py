def choose(question: str, answers: list=[], right: str="Right answer", wrong: str="Wrong answer", right_color: str="\033[0m", wrong_color: str="\033[0m", enum: bool=False, right_answers: list=[], select: str="Answer: "):
    """
    Ask a question. The user must choose
    the answer which he think it's right.
    Parameters:
    - question: the question that the user must answer to
    - answers: the list of the answers proposed to the user
    - right: the message if the user answer is the right
    - wrong: the message if the user answer is the wrong
    - right_color: the color of the message of param 'right'
    - wrong_color: the color of the message of param 'wrong'
    - right_answers: the list of the right answers
    - answer: the select answer message
    """
    for rgt in right_answers:
        if rgt in answers:
            pass
        else:
            raise IndexError(f"{rgt} not in right answers")
    
    print(question)
    
    if enum:
        for answ in enumerate(answers, start=1):
            print(answ)
    else:
        for answ in answers:
            print(answ)
            
    ans = input(select)
    
    if ans in right_answers:
        print(f"{right_color}{right}\033[0m")
    else:
        print(f"{wrong_color}{wrong}\033[0m")
        
    return ans