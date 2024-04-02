# Creates a task in windows task scheduler
# Takes in parameters for task name, executable path, start time, and day of the week
# Note: You must run this program as an administrator for it to work

import os
import win32com.client

def create_task(task_name, exe_path, start_time, day_of_week):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Define task settings
    task_def.RegistrationInfo.Description = 'Automated Reservation Task'
    task_def.Principal.UserId = "macth"
    task_def.Principal.LogonType = 3  # LogonType = Service Account
    task_def.Principal.RunLevel = 1  # HighestAvailable

    # Define task trigger (to run weekly on the specified day at the specified time)
    trigger = task_def.Triggers.Create(3)  # TriggerType = Weekly
    trigger.StartBoundary = start_time
    trigger.DaysOfWeek = day_of_week  # Set the day of the week

    # Define action (execute the provided executable)
    action = task_def.Actions.Create(0)  # ActionType = Execute
    action.Path = exe_path

    
    # Configure power conditions
    settings = task_def.Settings
    settings.DisallowStartIfOnBatteries = False
    settings.StopIfGoingOnBatteries = False
    
    # Register the task with compatibility set for Windows 10 (3rd flag set to '6')
    root_folder.RegisterTaskDefinition(
        task_name, task_def, 6, None, None, 3)  # TaskCreate, IgnoreConflicts, StartIfOnBatteries

    print("Task created successfully!")


# Uses this these parameters if this program is run directly
if __name__ == "__main__":
    task_name = "get_res"
    exe_path = "C:\\Users\\macth\\Desktop\\Github Repositories\\FineDining-Reservation\\dist\\get_res.exe"  # Replace with your executable path
    start_time = "2024-04-01T19:46:45"  # Replace with the desired start time in ISO 8601 format
    day_of_week = 2  # Monday (you can change this value to represent another day of the week)

    create_task(task_name, exe_path, start_time, day_of_week)

# day of the week flags
# 1 - sunday
# 2 - monday
# 4 - tuesday
# 8 - wednesday
# 16 - thursday
# 32 - friday
# 64 - saturday

# exe path
# C:\\Users\\macth\\Desktop\\Github Repositories\\FineDining-Reservation\\dist\\get_res.exe