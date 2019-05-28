# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-04-28 10:01:44
# @Last Modified by:   Phill
# @Last Modified time: 2019-04-30 15:57:56

class Score:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(instance):
            raise TypeError("Score must be integer!")
        if not 0 <= value <= 100:
            raise ValueError("Valid value must be in [0, 100]")

        self._score = value

    def __get__(self, instance, owner):
        return self._score

    def __delete__(self):
        del self._score

class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "<Student: {}, math: {}, chinese: {}, english: {}>".format(self.name, self.math, self.chinese, self.english)

