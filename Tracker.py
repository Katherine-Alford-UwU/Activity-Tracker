class SleepTracker:
  hourList = []
  dateList = []
  def __init__(self, name, age):
    self.name=name
    self.age=age
    
  def addHours(self, hours, sleepDate):
    self.hourList.append(hours)
    self.dateList.append(sleepDate)
  
  def getHours(self, sleepDate):
    idx = self.dateList.index(sleepDate)
    return self.hourList[idx]
  
  def getRecommendedHours(self):
    if (self.age >= 3 and self.age <= 5):
      return 10
    if (self.age > 5 and self.age <= 12):
      return 9
    if (self.age > 12 and self.age <= 18):
      return 8
    else:
      return 7
    
  def getAverageHours(self):
    length = len(self.hourList)
    sum = 0
    for i in self.hourList:
      sum = sum + i
    return sum/length

  def printEnoughSleep(self):
    if self.getRecommendedHours() > self.getAverageHours():
      print("Not sleeping enough >:l")   
      
    if self.getRecommendedHours() < self.getAverageHours():
      print("Enough Sleep BD")
    if self.getRecommendedHours() == self.getAverageHours():
      print("B Student")

class StepTracker:
  amountList = []
  dateList = []
  def __init__(self, name, age):
    self.name=name
    self.age=age
    
  def addAmount(self, ammount, stepDate):
    self.amountList.append(ammount)
    self.dateList.append(stepDate)
  
  def getAmount(self, stepDate):
    idx = self.dateList.index(stepDate)
    return self.amountList[idx]
  
  def getRecommendedSteps(self):
    if (self.age >= 6 and self.age <= 11):
      return 15000
    if (self.age > 12 and self.age <= 25):
      return 10000
    if (self.age > 25 and self.age <= 65):
      return 8000
    else:
      return 1000
    
  def getAverageAmount(self):
    length = len(self.amountList)
    sum = 0
    for i in self.amountList:
      sum = sum + i
    return sum/length

  def printEnoughSteps(self):
    if self.getRecommendedSteps() > self.getAverageAmount():
      print("Not walking enough >:l")   
      
    if self.getRecommendedSteps() < self.getAverageAmount():
      print("Enough Steps BD")
    if self.getRecommendedSteps() == self.getAverageAmount():
      print("B Student")

      
class WeatherTracker:
  degreeList = []
  dateList = []
  def __init__(self, season, city):
    self.season=season
    self.city=city
    
  def addDegree(self, degree, date):
    self.degreeList.append(degree)
    self.dateList.append(date)

  def getDegree(self, weatherDate):
    idx = self.dateList.index(weatherDate)
    return self.degreeList[idx]