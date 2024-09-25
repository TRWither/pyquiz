# PyQuiz
`quiz` (or PyQuiz) is a Python library that makes it easier to create quizzes, thanks to a few very useful functions.

## Why use PyQuiz?
Why use PyQuiz? Well, there are several reasons. Firstly, let's imagine that, in one of your projects, you plan to ask the user a question (an enigma, for example). Well, you'll have to make the question yourself. Well, with PyQuiz, you don't have to! All you have to do is describe your riddle, and it's ready!

## How to install?
To install PyQuiz, simply use `pip`.
```bash
cd pyquiz
pip install .
```

## Some examples
Here is a simple example to give you an idea of the functionality of the :
```py
from quiz.ask impor ask

ask(
    question="What is the color of Pacman? ",
    answer="yellow",
    right_color="\033[32m",
)
```
But to find out more, take a look at the [docs](docs/USAGE.md)
