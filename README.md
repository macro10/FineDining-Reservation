# FineDining-Reservation
A relatively simple python program to automate getting reservations at any of High Point University's three fine dining locations.

How to use:
Parameters such as restaurant, party size, time, date, and user credentials are hardcoded by the user. There is also a debugging flag, "complete" that will determine whether or not the final step of the reservation process is completed. (Note:  I will likely make a frontend soon for user input)

Features:
   * The Selenium Chrome Web Driver is used to target HTML elements on the web
   * Explicit waits allow the program to wait for each element to be clickable by the driver, reducing errors in high traffic
   * The average execution time is around 13.6 seconds, meaning reservations are unlikely to already be filled

To create executable (using pyinstaller):
pyinstaller --onefile primeRes.py
pyinstaller primeRes.spec

To configure execution time:
Create a scheduled task in windows task scheduler to execute the program weekly at midnight.
