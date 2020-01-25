import re

date_regex = re.compile(r'(\d\d/\d\d/\d\d\d\d)')

text='''
Date Detection
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

01/01/1000
02/05/2015
42/20/2015
30/01/2000
02/29/2000
02/29/2001
02/29/2100
01/50/2000
04/50/2000
02/30/2000
03/01/1980

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
'''
good_dates = list() # make a new list of only the good dates. When a bad date found, continue
mo = re.findall(date_regex, text) # all matches are found and put in a list called mo
for n in range(len(mo) - 1):
    item = mo[n] # variable to make cleaner code
    if int(item[0:2]) > 12: # check for months that don't exist and remove them
        continue
    if int(item[0:2]) in [1, 3, 5, 7, 8, 10, 12]: # months with 31 days
        if int(item[3:5]) > 31: # eliminate entries where the date is too high
            continue
    if int(item[0:2]) in [4, 6, 9, 11]: # months with 30 days
        if int(item[3:5]) > 30: # eliminate entries where the date is too high
            continue
    if item[0:2] == '02': # February rule
        if int(item[3:5]) > 29: # these days never happen
            continue
        if int(item[3:5]) == 29: # the leap year rule
            if int(item[6:]) % 100 == 0 and int(item[6:]) % 400 != 0:
                continue # clears years divisible by 100 but not 400
            if int(item[6:]) % 4 != 0:
                continue # clears years not divisible by 4. Though this would include years divisible by 100, the prior if already cleared them out

    good_dates.append(item)
print(good_dates)
