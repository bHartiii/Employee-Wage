import random


class Employee:
    def checkAttendance(self):
        number = random.randint(0, 1)
        switcher = {
            0: "absent",
            1: "present"
        }
        return switcher.get(number)

    def checkPartTime(self):
        is_part_time = random.randint(0, 1)
        switcher = {
            0: FULL_DAY_HOUR,
            1: PART_TIME_HOUR
        }
        return switcher.get(is_part_time)

    def calculateEmployeeDailyWage(self):
        """
        checks attendance and daily hours
        calculates daily wage
        :return dailyWage:
        """
        attendance = emp.checkAttendance()
        dailyWorkingHour = emp.checkPartTime()
        dailyWage = 0
        if attendance == "present":
            dailyWage = WAGE_PER_HOUR * dailyWorkingHour

        return dailyWage

    def monthlyWageComputation(self):
        count = 1
        monthlyWage=0
        while count <= 20:
            tempWage = emp.calculateEmployeeDailyWage()
            monthlyWage=monthlyWage+tempWage
            count = count + 1
        return monthlyWage

if __name__ == "__main__":
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_HOUR = 4
    emp = Employee()
    print(emp.monthlyWageComputation())
