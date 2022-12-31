#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    
    def __init__(self, first, last):
        super().__init__(first, last)
        self.knowledge = ["str is a data type in Python",
                            "programming is hard, but it's worth it",
                            "JavaScript async web request",
                            "Python function call definition",
                            "object-oriented teacher instance",
                            "programming computers hacking learning terminal",
                            "pipenv install pipenv shell",
                            "pytest -x flag to fail fast",
                        ]

    def teach(self):
        return random.choice(self.knowledge)
        # index = random.randrange(0, len(self.knowledge))
        # return self.knowledge[index]
