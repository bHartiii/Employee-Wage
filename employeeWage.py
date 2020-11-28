import random
class Employee:
    def checkAttendance(self):
        number=random.randint(0,1)
        if number == 1:
            return "present"
        else:
            return "absent"

if __name__=="__main__":
    emp=Employee()
    print(emp.checkAttendance())