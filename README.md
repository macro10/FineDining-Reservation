# FineDining-Reservation
A python program to programatically get reservations at any of High Point University's fine dining locations. Restaurants such as Prime, Kazoku, and Alo open reservations one week in advance at midnight. It's not uncommon for reservations to fill up within only a minute or two. To circumvent this issue, I allow users to choose the time they want to make a reservation and the program will handle the rest. This is accomplished by creating a scheduled task to execute a selenium service that gets the reservation.

How to use:
Restaurant, party size, time, date, and user credentials are input by the user. With these inputs you simply click create reservation, and it will schedule the task to execute a python script according to the parameters.

Features:
   * The Selenium Chrome Web Driver is used to target HTML elements on the web
   * Explicit waits allow the program to wait for each element to be clickable by the driver, reducing errors in high traffic
   * create_task() manipulates Windows COM objects to create tasks based on user time specifications.
   * The average execution time is around 11 seconds, meaning reservations are unlikely to already be filled
   * Written in Python


