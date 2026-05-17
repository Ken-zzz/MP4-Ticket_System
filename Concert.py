from datetime import timedelta 

class Concert:
   def __init__(self, **dur):
      # Converts int into time (minutes), eto basihan natin sa ibang functions
      self.duration = timedelta(hours=dur['hours'], minutes=dur['mins'], seconds=dur['secs'])
      # Stack
      self.attendees = []
   
   def pushAttendee(self):
      pass
   
   def popAttendee(self):
      pass
   
   def peekLastAttendee(self):
      pass
   
   def getAttendanceDuration(self):
      pass
   
   def detectRuleViolations(self):
      pass
   
   def displayAttendees(self):
      pass
   
   def generateAttendanceRep(self):
      pass
   
