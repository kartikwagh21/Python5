class Students:
    name=""
    roll_number=0

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
     
s1=Students()
s1.display()
s1.name="Kartik"
s1.roll_number=1234
s1.display()