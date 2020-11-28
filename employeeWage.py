import random
class Employee:
    def checkAttendance(self):
        number=random.randint(0,1)
        if number == 1:
            return "present"
        else:
            return "absent"

    def checkPartTime(self):
        isPartTime=random.randint(0,1)
        if isPartTime==0:
            return "true"
        else:
            return "false"

    def calculateEmployeeDailyWage(self):
        """
        checks attendance and daily hours
        calculates daily wage
        :return dailyWage:
        """
        attendance = emp.checkAttendance()
        partTime = emp.checkPartTime()
        dailyWage=0
        if attendance == "present":
            if partTime == "false":
                dailyWorkingHour = FULL_DAY_HOUR
            else:
                dailyWorkingHour = PART_TIME_HOUR
            dailyWage = WAGE_PER_HOUR * dailyWorkingHour

        return dailyWage

if __name__=="__main__":
    WAGE_PER_HOUR=20
    FULL_DAY_HOUR=8
    PART_TIME_HOUR=4
    emp=Employee()
    print(emp.calculateEmployeeDailyWage())
