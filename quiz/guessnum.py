def guessnum(number: int, try_find: str="The number is: ", right: str="Right answer.", lesser: str="Lesser.", greater: str="Greater.", right_color: str="\033[0m", wrong_color: str="\033[0m", rounds: bool=False):
    if rounds:
        _rounds = 0
        
    while True:
        answ = int(input(try_find))
        
        if answ == number:
            if rounds:
                _rounds += 1
            print(f"{right_color}{right}\033[0m")
            if rounds:
                print(f"Rounds: {_rounds}")
            break
        
        elif answ < number:
            if rounds:
                _rounds += 1
            print(f"{wrong_color}{greater}\033[0m")
            continue
        
        elif answ > number:
            if rounds:
                _rounds += 1
            print(f"{wrong_color}{lesser}\033[0m")
            continue
        
    return answ