from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import datetime
from datetime import timedelta


# Create chrome webdriver object
driver = webdriver.Chrome()
# Create wait object
wait = WebDriverWait(driver, 30)

def elementWait(locator, path):
    element = wait.until(EC.element_to_be_clickable((locator, path)))
    return element

def findClick(locator, path):
    element = wait.until(EC.element_to_be_clickable((locator, path)))
    element.click()
    return element

def getRes(restaurant, pSize, hr, min, username, pswd, phone, complete):
    

    DEBUGGING = True

    # change time to string
    resTime = hr + ":" + min

    if DEBUGGING:
        print(resTime)

    # Time step
    t = 3



    # Set date to a week from current time. (Prime and Alo reservations open a week in advance at midnight.)    
    date = datetime.datetime.now()
    date = date + timedelta(days=7)
    date = date + timedelta(hours=1)

    if DEBUGGING:
        print(date.year)
        print(date.month)
        print(date.day)
        print(date.hour)
        print(date.minute)


    driver.get("https://finedining.highpoint.edu/1924-Prime/reservation")


    # Enlarge window
    driver.maximize_window()

    # Find username and password fields and input credentials
    userElement = findClick("id", "login-username")
    userElement.send_keys(username)
    pswdElement = findClick("id", "login-password")
    pswdElement.send_keys(pswd)


    # Find and click the Login button. In this case we find it by class since I couldn't find an id.
    loginButtonElement = findClick(By.CLASS_NAME, "btn-primary")

    # XPATH OF HIGH TRAFFIC SCREEN FOR IMPLEMENTATION: "/html/body/main/div/div/div[1]/div/h3"
    # Find and click the restaurant (by XPATH)
    if restaurant == 0:
        restaurantElement = findClick(By.XPATH, "/html/body/main/div/div/div/div[1]/a")
    elif restaurant == 1:
        restaurantElement = findClick(By.XPATH, "/html/body/main/div/div/div/div[2]/a")
    elif restaurant == 2:
        restaurantElement = findClick(By.XPATH, "/html/body/main/div/div/div/div[3]/a")







    # Find all elements in the class "day"
    elementWait(By.CLASS_NAME, "day")
    dateElements = driver.find_elements(By.CLASS_NAME, "day")

    # Iterate through all the days until the text matches the date we want, then click on it
    for dateElement in dateElements:
        print("Date Text: ", dateElement.text)
        if dateElement.text == str(date.day):
            dateElementLast = dateElement
    time.sleep(5)

    dateElementLast.click()

    # Find guest number selection bar (by XPATH)
    partyElement = findClick(By.XPATH, "/html/body/main/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div[1]/select")

    # Enter the correct number of guests and press enter
    partyElement.send_keys(str(pSize))
    partyElement.send_keys(Keys.ENTER)

    # Find the "Find Table" button and click it (by class name)
    TableElement = findClick(By.CLASS_NAME, "btn-primary")

    # Find and click the correct timeslot
    elementWait(By.CLASS_NAME, "timeslot")
    timeElements = driver.find_elements(By.CLASS_NAME, "timeslot")

    for timeElement in timeElements:
        print("Time Text: ", timeElement.text)
        if timeElement.text == resTime:
            timeElement.click()
            break

    # Enter phone number
    phoneElement = findClick(By.ID, "telephone")
    phoneElement.send_keys(phone)

    # Click the complete reservation button if the complete flag is enabled
    if complete == True:
        completeElement = findClick(By.XPATH, "/html/body/main/div/div/div[2]/div/div/div/div/form/button")

    # If debugging sleep for 3 minutes
    if DEBUGGING:
        time.sleep(180)

    driver.close()

getRes(0, 2, "6", "30", "mtrotte1", "Sydney6400", "7044515754", False)
# getRes(restaurant(int), pSize(int), hr(str), min(str), username(str), pswd(str), phone(str), complete(bool))

# Prime is 0, Alo is 1, Kazoku is 2