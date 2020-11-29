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

    def getEmployeeDailyWorkingHours(self):

        attendance = emp.checkAttendance()
        if attendance == "present":
            dailyWorkingHours = emp.checkPartTime()
        else:
            dailyWorkingHours=0
        return dailyWorkingHours

    def getTotalWorkHours(self):
        workingDays = 0
        totalWorkingHours = 0
        while totalWorkingHours < MAX_HOURS or workingDays < MAX_DAYS:
            dailyWorkingHours = emp.getEmployeeDailyWorkingHours()
            workingDays = workingDays + 1
            totalWorkingHours = totalWorkingHours + dailyWorkingHours
        print(totalWorkingHours)

        return totalWorkingHours

    def monthlyWageComputation(self):
        totalWorkingHours = emp.getTotalWorkHours()
        monthlyWage = totalWorkingHours * WAGE_PER_HOUR
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

