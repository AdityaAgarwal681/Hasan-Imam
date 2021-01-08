import info
#import timeTable
import time

#For zoom make sure you have zoom client installed, and signed in. 
# Google meet and Microsoft support will be added soon

def joinEnglish():
    driver.get(english)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(2325)#seconds
    driver.quit()

def joinPhysics():
    driver.get(physics)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(2325)#seconds
    driver.quit()

def joinChem():
    driver.get(chemistry)
    time.sleep(60) #seconds
    time.sleep(2325)#seconds
    driver.quit()

def joinMaths():
    driver.get(maths)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(2325)#seconds
    driver.quit()

def joinBio():
    driver.get(biology)
    time.sleep(60) #seconds
    time.sleep(2325)#seconds
    driver.quit()

def joinSS():
    driver.get(SS)
    time.sleep(60) #seconds
    time.sleep(2325)#seconds
    driver.quit()

def joinHindi():
    driver.get(Hindi)
    time.sleep(60)#seconds
    time.sleep(2325)#seconds
    driver.quit

 def joinDummy():
     driver.get(Dummy)
     time.sleep(10)#seconds
     time.sleep(100)#seconds
     driver.quit