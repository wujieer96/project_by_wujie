class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60 and self.score < 80:
            return 'B'
        else:
            return 'C'