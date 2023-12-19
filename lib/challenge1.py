#Converting 12-hour time to 24-hour time
def convert_to_24_hour(hour, minute, period):
    #check if the period is 'am' and if the hour is 12. 
    #If true, it sets the hour to 0. 
    if period == 'am':
        if hour == 12:
            hour = 0
#If the period is 'pm' and the hour is not 12, it adds 12 to the hour.
    else:
        if hour != 12:
            hour += 12

    return '{:02d}{:02d}'.format(hour, minute)
#Taking user input for hours, minutes, and periods.


print(convert_to_24_hour(12, 30, 'am')) 


print( convert_to_24_hour(10, 30, 'pm')) 