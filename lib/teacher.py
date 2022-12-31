#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    
    def __init__(self, first, last):
        super().__init__(first, last)
        self.knowledge = ["This", "that", "those!"]

    def teach(self):
        index = random.randrange(0, len(self.knowledge))
        return self.knowledge[index]
