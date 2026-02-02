#FutureTime.py
#Name: Jaylen Atsou
#Date: Feburary 1, 2026 
#Assignment: Lab 2

import datetime

def main():
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute
  
  print("Please enter hours and minutes to calculate future time.\nNumbers must be whole numbers.")
  
  moreHours = int(input("Enter hours: "))
  moreMinutes = int(input("Enter minutes: "))

  futureMinutes = currentMinute + moreMinutes
  futureHours = futureMinutes // 60
  futureMinutes = futureMinutes % 60

  futureHours = currentHour + moreHours + futureHours
  futureHours = futureHours % 24

  print(f"The future time is {futureHours:02}:{futureMinutes:02}")

if __name__ == '__main__':
  main()
