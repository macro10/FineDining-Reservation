from create_executable import create_executable
from create_task import create_task

exe = "main.py"

task_name = "get_res"
exe_path = "C:\\Users\\macth\\Desktop\\Repositories\\FineDining-Reservation\\dist\\main.exe"  # Replace with your executable path
start_time = "2024-04-11T00:00:05"  # Replace with the desired start time in ISO 8601 format
day_of_week = 16 # (you can change this value to represent another day of the week)

create_executable(exe)

create_task(task_name, exe_path, start_time, day_of_week)
