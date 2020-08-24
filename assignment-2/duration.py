''' 8.	Units of Time
Create a program that reads duration from the user as a number of days, hours, minutes, and seconds.
 Compute and display the total number of seconds represented by this duration. 
'''
days=int(input("Enter the duration as a number of days: "))
hours=int(input("Enter the duration as a number of hours: "))
minutes=int(input("Enter the duration as a number of minutes: "))
seconds=int(input("Enter the duration as a number of seconds: "))
min_in_sec=minutes*60
hour_in_sec=hours*60*60
days_in_sec=days*24*60*60
total_time_in_sec = seconds + min_in_sec + hour_in_sec + days_in_sec
print("\nThe total number of seconds represented by this duration: ",total_time_in_sec)