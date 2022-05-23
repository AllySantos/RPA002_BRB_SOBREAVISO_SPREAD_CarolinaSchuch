# Remove not worked holidays and, with worked holidays, set isWorkHoliday as True

import sys


def remove_holiday(arrayHoliday, arrayWorkHoliday):
    for holiday in arrayHoliday:
        # If exist holiday that is user won't work
        if holiday not in arrayWorkHoliday:
            remove_holiday_day(holiday)

        else:
            # Set
            workHoliday = {
                "numberDay": holiday["numberDay"],
                "weekDay": holiday["weekDay"],
                "isWorkHoliday": True
            }

            indexWorkHoliday = monthDays.index(holiday)

            monthDays[indexWorkHoliday] = workHoliday

            # If holiday is on Friday, in next day there isn't overwatch shift
            if holiday["weekDay"] == 5 and indexWorkHoliday != (len(monthDays) - 1):
                indexNextHoliday = indexWorkHoliday + 1

                # Delete next day
                del monthDays[indexNextHoliday]


def remove_holiday_day(holiday):
    indexHoliday = monthDays.index(holiday)

    # If holiday is on Friday in next day there isn't overwatch shift
    if holiday["weekDay"] == 5 and indexHoliday != (len(monthDays) - 1):
        indexNextHoliday = indexHoliday + 1

        # Delete next day
        del monthDays[indexNextHoliday]

    # Delete holiday day
    del monthDays[indexHoliday]


if __name__ == '__main__':
    arrayHoliday = sys.argv[1]
   
    
    #arrayWorkHoliday = sys.argv[2]

    #monthDays = sys.argv[3]

    # remove_holiday(arrayHoliday, arrayWorkHoliday)

    #for holiday in arrayHoliday:
     #   print(str(holiday))
    print(arrayHoliday[0:10])
