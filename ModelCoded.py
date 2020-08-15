
import numpy as np
import random as rm
 
#The statespace
states = ["Charging","Not Charging"]
 
#Charging (C)
#Not Charging (N)
 
#Initializing transition probabilities
X1, Y1, X2, Y2  = 0, 0, 1, 1
 
#X1 Charging to Charging
#Y1 Not Charging to Charging
#X2 Charging to Not Charging
#Y2 Not Charging to Not Charging
 
#Possible transitions from states
transitionName = [["CC","CN"],["NC","NN"]]
#Charging to Charging (CC)
#Charging to Charging (CN)
#Not Charging to Charging (NC)
#Not Charging to Not Charging(NN)
 
#Probability Matrix: probability of staying or changing state
transitionMatrix = [[X1, X2],[Y1,Y2]]
#Probability corresponds to CC (X1), CN (X2), NC (Y1), NN (Y2)
 
#Probability of being home
placeMatrix = [["H", "P"],["H", "P"]]
placeProb = [[.7, .3],[.7, .3]]
 
#Probability of charging when at current battery level (e.g. 92% -> x = .92)
def probofcharging(x):
  return round((1/(5*(x+.2))), 3)
def numberofcharging():
  #Calling and inititialized transitionMatrix probs.
    global X1
    global X2 
    global Y1 
    global Y2
    X1, X2, Y1, Y2 = 0,1,0,1
    global transitionMatrix
  #Probability changes due to time (proportion of baterry change/time)
    increment = .02
    #Starting state (C or N)
    chargingstate = "Not Charging"
    #Sequence of states
    numberofhrscharging = 0
    timeOfDay = 0
    #Accounts for battery charge (averages probabilities of battery charge and time)
    batterycharge = 1
 
    place = "H"
    #Decides whether person is charging or not charging
    while timeOfDay != 16:
        #Current state of device identified
        #If state is charging
        if chargingstate == "Charging":
          #Generates a random transition (CC, CN)
          change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
          #Stays Charging
          if change == "CC":
            place = np.random.choice(placeMatrix[0],replace=True,p=placeProb[0])
            if place == "P":
              numberofhrscharging += 1
            pass
          #Changes to Not Charging
          elif change == "CN":
            chargingstate = "Not Charging"
          #Average battery increase from charging across cars, phones, tablets, laptops
          if batterycharge + .3166 < 1:
            batterycharge += .3166
          else:
            batterycharge = 1
 
        #If state is not charging
        elif chargingstate == "Not Charging":
          #Generates a random transition (NC, NN)
          change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
          #Changes to Charging
          if change == "NC":
            place = np.random.choice(placeMatrix[0],replace=True,p=placeProb[0])
            if place == "P":
              numberofhrscharging += 1
            chargingstate = "Charging"
            pass
          #Remains to Not Charging
          elif change == "NN":
            chargingstate = "Not Charging"
          #Average battery decrease from not charging across cars, phones, tablets, laptops
          if batterycharge - .10799 > 0:
            batterycharge -= .10799
          else:
            batterycharge = 0
        #Moves to next hours
        timeOfDay += 1
        #Changes probability of state transitions based on increment variable
        #Every two hours probability changes
        if(timeOfDay%2 == 0):
          X1 += increment
          X2 -= increment
          Y1 += increment
          Y2 -= increment
        #Averages time-adjusted probability with battery-adjusted probability
        X1 = (X1 + probofcharging(batterycharge))/2
        X2 = 1-X1
        Y1 = (Y1 + probofcharging(batterycharge))/2
        Y2 = 1-Y1
        transitionMatrix = [[X1, X2],[Y1,Y2]]
    #Counts number of C's to determine number of hours charging
    return numberofhrscharging
 
 
 
#Finds the number of hours spent charging over a day for a number of devices
daySum = 0
#Averages daySum
dayAvg = 0
#Finds the number of hours spent charging over total number of days
periodSum = 0;
#Averages periodSum
periodAvg = 0;
#Total number of hours spent charging over number of days for number of devices
totalNumOfHours = 0;
#Averages totalNumOfHours
totalAvgOfHours = 0;
 
#Tells us how many hours a single device charges for a day based on totalNumOfHours
perdeviceperday = 0;
 
#How many times this program reiterates
numOfTrials = 1
#How many days a number of devices state is examined over 16 hours
days = 1
#How many number of devices state is examined over 16 hours
numOfDevices = 30
 
#Number of total hours spent in charging for all devices of all days
periodSumList = []
 
#1) Loop first sums the hours of charging for a number of devices
#2) Loop then sums the total hours of charging for all devices for 
#all days to find total number of charging hours over number of days
#3) Repeats the process and averages the result from Loop 2
for iterations in range (0, numOfTrials):
  periodSum = 0
  for iterations in range(0,days):
    daySum = 0
    for iterations in range (0,numOfDevices):
      #Finds number of total hours for a number of devices with Markov Model
      daySum = daySum + numberofcharging()
    #Finds total hours over number of days - recursively adds each daySum
    periodSum = daySum + periodSum
  #Finds total hours of all trials 
  totalNumOfHours = periodSum + totalNumOfHours
  #Remembers individual trials for total charging hours over number of days
  periodSumList.append(periodSum)
#Average total charging hours over given days for number of trials
totalAvgOfHours = totalNumOfHours/numOfTrials
#Average total charging hours per day for each device
perdeviceperday = (totalAvgOfHours/days)/numOfDevices
 
#dayAvg = dayAvg/days
#totalAvgOfHours = totalNumOfHours/days
 
#Prints Results
print("Number of Devices: " + str(numOfDevices))
print("Number of Days: " + str(days))
print("Number of Trials: " + str(numOfTrials))
print("Average Total Hours of Charging For " + str(numOfDevices) + " Devices over " + str(days) + " days: " + str(totalAvgOfHours))
print("Average Charging Hours per day per device: " + str(perdeviceperday))
print("Individual Totals for Charging Hours over Given Number of Days: " + str(periodSumList))
 
#Sample Output:
#Number of Devices: 50
#Number of Days: 365
#Number of Trials: 10
#Average Total Hours of Charging For 50 Devices over 365 days: 22762.6
#Average Charging Hours per day per device: 1.2472657534246574
#Individual Totals for Charging Hours over Given Number of Days: [22736, 22767, 22631, 22864, 22762, 22843, 22602, 22803, 22884, 22734]
