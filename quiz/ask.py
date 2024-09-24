def ask(question: str, answer: str, right: str="Right answer.", wrong: str="Wrong answer.", right_color: str="\033[0m", wrong_color: str="\033[0m"):
    """
    Ask a question.
    Parameters:
    - question: the question which the user must answer to
    - answer: the right answer
    - right: the message if the user answer is the right
    - wrong: the message if the user gives a wrong answer
    - right_color: the color of the message of the param 'right'
    - wrong_color: the color of the message of the param 'wrong'
    """
    answ = input(question)
    
    if answ == answer:
        print(f"{right_color}{right}\033[0m")
    else:
        print(f"{wrong_color}{wrong}\033[0m")
        
    return answ