class Student(Person):
    
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores
    
    def calculate(self):
        avg = sum(scores)/len(scores)
        if 90 <= avg <= 100:
            return "O"
        elif 80 <= avg < 90:
            return "E"
        elif 70 <= avg < 80:
            return "A"
        elif 55 <= avg < 70:
            return "P"
        elif 40 <= avg < 55:
            return "D"
        else:
            return "T"