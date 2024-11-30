# FineDining-Reservation
A python software project to programatically get reservations at High Point University's fine dining locations.

Purpose:
Restaurants Prime, Kazoku, and Alo open reservations one week in advance at midnight. Reservations fill quickly. To solve this issue, I wanted to make an app that schedules tasks to make reservations at a specified time and date.

How to use:
The user inputs reservation information, and then clicks "Create Reservation."

Inputs:
Restaurant, party size, time, date, and user credentials are input by the user. With these inputs you simply click create reservation, and it will schedule the task to execute a python script according to the parameters.

Features:
   * The Selenium Chrome Web Driver is used to interact with HTML elements on the web
   * Explicit waits allow the program to wait for each element to be clickable by the driver, reducing errors in high traffic
   * Software creates tasks on your OS (currently windows only), based on reservation specifications.
   * Average execution time is 11 seconds, meaning reservations are unlikely to already be filled
   * Written in Python


