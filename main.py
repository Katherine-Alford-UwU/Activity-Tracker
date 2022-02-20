from Tracker import StepTracker,  SleepTracker, WeatherTracker

track = WeatherTracker("Katherine", 12)
track.addDegree(42, "3/2/22")
track.addDegree(13, "1/5/22")
track.addDegree(90, "12/31/22")
print(track.degreeList)
print(track.dateList)

print(track.getDegree("12/31/22"))

#[5,17,9]
#[30, 32, 23]

#0
#track.printEnoughSteps()