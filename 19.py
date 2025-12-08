import datetime

def solution():
    numSundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            day = datetime.date(year=year, month=month, day=1)
            if day.weekday() == 6:
                numSundays += 1
    return numSundays

print(solution())