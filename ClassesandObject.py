class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        print(f"name-{name}, age-{age}, track-{tracks}, score-{score}")

    def change_name(self, newname):
        self.change_name = newname
        print(f"The name of the newstudent is {newname}")
    def change_age(self, age):
        print(f"The age of the new student is  {age}")
    def add_track(self, tracks):
        print(f"The track of the new student is  {tracks}")
    def get_score(self, score):
        print(f"The score of the new student is  {score}")
        
        
        
Bob = Student(name="Bob",age= 26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.90)