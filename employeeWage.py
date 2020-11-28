import random
class Employee:
    def checkAttendance(self):
        number=random.randint(0,1)
        if number == 1:
            return "present"
        else:
            return "absent"

    def calculateEmployeeDailyWage(self):
        attendance = emp.checkAttendance()
        if attendance == "present":
            dailyWage = WAGE_PER_HOUR * FULL_DAY_HOUR
        else:
            dailyWage = 0
        return dailyWage

if __name__=="__main__":
    WAGE_PER_HOUR=20
    FULL_DAY_HOUR=8
    emp=Employee()
    print(emp.calculateEmployeeDailyWage())
