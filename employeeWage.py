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
        dailyWorkHoursList = []
        while totalWorkingHours < MAX_HOURS and workingDays < MAX_DAYS:
            dailyWorkingHours = emp.getEmployeeDailyWorkingHours()
            dailyWorkHoursList.append(dailyWorkingHours)
            workingDays = workingDays + 1
            totalWorkingHours = totalWorkingHours + dailyWorkingHours
        return dailyWorkHoursList

    def monthlyWageComputation(self):
        workingHours = emp.getTotalWorkHours()
        count=1
        monthlyWage=0
        for dailyWorkingHour in workingHours:
            dailyWage = dailyWorkingHour * WAGE_PER_HOUR
            monthlyWage = monthlyWage+dailyWage
            dailyWageList["day-"+str(count)]=dailyWage
            count = count+1
        return monthlyWage


if __name__ == "__main__":
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_HOUR = 4
    MAX_HOURS = 100
    MAX_DAYS = 20
    dailyWageList = {}
    dailyWorkingHours = 0
    emp = Employee()
    print("Total Monthly wage - "+str(emp.monthlyWageComputation()))
    print(dailyWageList)

