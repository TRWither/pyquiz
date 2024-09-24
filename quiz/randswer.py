import random

def randswer(question: str, answers: list=[], right: str="Right answer.", wrong: str="Wrong answer.", right_color: str="\033[0m", wrong_color: str="\033[0m"):
    """
    Ask a question, but the answer is
    a random answer.
    Parameters:
    - question: the question that the user must answer to
    - answers: the list of the answers
    - right: the message if the user answer is the right
    - wrong: the message if the user gives a wrong answer
    - right_color: the color of the message of the param 'right'
    - wrong_color: the color of the message of the param 'wrong'
    """
    answ = input(question)
    
    right_answer = random.choice(answers)
    
    if answ == right_answer:
        print(f"{right_color}{right}\033[0m")
    else:
        print(f"{wrong_color}{wrong}\033[0m")
        
    return answ