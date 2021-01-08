import datetime
from selenium import webdriver
import schedule
import time
from join import *
import info

driver =  webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
e = datetime.datetime.now()

#timeTable.py combined in main.py to simplfy working 

def monday():
    schedule.every().monday.at(firstClass).do(joinPhysics())
    schedule.every().monday.at(secondClass).do(joinHindi())
    schedule.every().monday.at(thirdClass).do(joinEnglish())
    schedule.every().monday.at(fourthClass).do(joinSS())
    schedule.every().monday.at(fifthClass).do(joinMaths())
    
def tuesday():
    schedule.every().tuesday.at(firstClass).do(joinHindi())
    schedule.every().tuesday.at(secondClass).do(joinSS())
    schedule.every().tuesday.at(thirdClass).do(joinPhysics())
    schedule.every().tuesday.at(fourthClass).do(joinEnglish())
    schedule.every().tuesday.at(fifthClass).do(joinMaths())

def wednesday():
    schedule.every().wednesday.at(firstClass).do(joinMaths())
    schedule.every().wednesday.at(secondClass).do(joinBio())
    schedule.every().wednesday.at(thirdClass).do(joinHindi())
    schedule.every().wednesday.at(fourthClass).do(joinEnglish())
    schedule.every().wednesday.at(fifthClass).do(joinSS())
    schedule.every().wednesday.at(dummyclass).do(joinDummy())
def thursday():
    schedule.every().thursday.at(firstClass).do(joinChem())
    schedule.every().thursday.at(secondClass).do(join())
    schedule.every().thursday.at(thirdClass).do(joinMaths())
    schedule.every().thursday.at(fourthClass).do(joinSS())
    schedule.every().thursday.at(fifthClass).do(joinEnglish())

def friday():
    schedule.every().friday.at(firstClass).do(joinSS())
    schedule.every().friday.at(secondClass).do(joinHindi())
    schedule.every().friday.at(thirdClass).do(joinBio())
    schedule.every().friday.at(fourthClass).do(joinEnglish())
    schedule.every().friday.at(fifthClass).do(joinMaths())

def dumm():
    schedule.every().saturday.at(firstClass).do(join())
 schedule.every().saturday.at(secondClass).do(join())
 schedule.every().saturday.at(thirdClass).do(joinMaths())
 schedule.every().saturday.at(fourthClass).do(joinChem())
 schedule.every().saturday.at(fifthclass).do(joinHindi())
while True:
    schedule.run_pending()
    time.sleep(1)#seconds


# Code for Timetable.py ends here 

day = (e.strftime("%a"))
print(day)

if day=="Mon":
    monday()
elif day=="Tue":
    tuesday() 
elif day=="Wed":
    wednesday()
elif day=="Thu":
    thursday()
elif day=="Fri":
    friday()
elif day=="Sat":
    saturday()


