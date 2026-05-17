from Concert import Concert


def session():
   while True:
      print("""
      Welcome to the Concert Attendance System!
      >>>  (0) Exit
      >>>  (1) Create another concert entry.
      """)
      try:
         choice = int(input(">  "))
         if choice in (0, 1):
               return choice
         print(f">>>  {choice} is not a valid input!\n")
      except ValueError:
         print(">>>  Input must be an integer!\n")


def initConcert():
    while True:
      print(">>>  Enter concert duration in this format: hours minutes seconds")
      try:
         # Converts string input into a list of numbers
         duration = list(map(int, input(">  ").split(" ")))
         if len(duration) != 3:
               print(">>>  Please enter exactly 3 values: hours minutes seconds\n")
               continue
         hours, mins, secs = duration
         return Concert(hours=hours, mins=mins, secs=secs)
      except ValueError:
         print(">>>  Duration must be integers only!\n")


def operateConcert(concert):
    while True:
      print("""
      What would you like to do?
      >>>  (0) Exit
      >>>  (1) Push attendee
      >>>  (2) Pop attendee
      >>>  (3) Peek the last attendee
      >>>  (4) Get attendance duration
      >>>  (5) Detect rule violations
      >>>  (6) Display attendees
      >>>  (7) Generate attendance report
      """)
      try:
         choice = int(input(">  "))
      except ValueError:
         print(">>>  Input must be an integer!\n")
         continue

      if choice == 0: break
      elif choice == 1: concert.pushAttendee()
      elif choice == 2: concert.popAttendee()
      elif choice == 3: concert.peekLastAttendee()
      elif choice == 4: concert.getAttendanceDuration()
      elif choice == 5: concert.detectRuleViolations()
      elif choice == 6: concert.displayAttendees()
      elif choice == 7: concert.generateAttendanceReport()
      else: print(f">>>  {choice} is not a valid input!\n")

if __name__ == "__main__":
    while True:
        action = session()   
        if action == 0:
           # Exit   
           print(">>>  Goodbye! See you at the next concert!\n")
           break 
        else :
           # Init concert class then pass it to operateConcert
           print(">>>  Setting up a new concert entry...\n") 
           operateConcert(initConcert()) 