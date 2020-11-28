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
        emp.dailyWorkingHours = emp.checkPartTime()
        dailyWage = 0
        if attendance == "present":
            dailyWage = WAGE_PER_HOUR * emp.dailyWorkingHours

        return dailyWage

    def monthlyWageComputation(self):
        monthlyWage = 0
        workingDays = 0
        workingHours = 0
        while workingHours < 100 or workingDays < 20:
            tempWage = emp.calculateEmployeeDailyWage()
            monthlyWage = monthlyWage + tempWage
            workingDays = workingDays + 1
            workingHours = workingHours + emp.dailyWorkingHours
        return monthlyWage


if __name__ == "__main__":
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_HOUR = 4
    MAX_HOURS = 100
    MAX_DAYS = 20
    dailyWorkingHours = 0
    emp = Employee()
    print(emp.monthlyWageComputation())
