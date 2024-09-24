# Usage
PyQuiz is very easy to use, and here are a few examples to prove it:

## From the Earth to the Moon
```py
from quiz.ask import ask

ask(
    question="What is the distance (in km) between the Earth and the Moon?",
    answer="300,000",
    right="Yes, the distance between the Earth and the Moon is 300,000 km!",
    wrong="Unfortunately, that's not it.",
    right_color="\033[32m",             # ANSI code for green
    wrong_color="\033[31m",             # ANSI code for red
)
```

## 3 answers, 2 true, 1 false
```py
from quiz.choose import choose

choose(
    question="Find the wrong answer",
    answers=[
        "Elephants are rainbow",
        "Turtles can live in the sea",
        "PyQuiz is a nice library",
    ],
    right="Yes! The elephants are not rainbow.",
    wrong="That's false.",
    right_color="\033[32m",
    wrong_color="\033[31m",
    right_answers=["Elephants are rainbow"],
    enum=True,
    answer="The right answer is... ",
)
```

## Guess the number!
```py
from quiz.guessnum import guessnum
import random

guessnum(
    number=random.randint(1, 100),
    try_find="The number is...",
)
```

There are other functions we let you discover...