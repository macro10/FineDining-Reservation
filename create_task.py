import os
import win32com.client

def create_task(task_name, exe_path, start_time):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()

    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Define task settings
    task_def.RegistrationInfo.Description = 'Automated Reservation Task'
    task_def.Principal.UserId = "SYSTEM"
    task_def.Principal.LogonType = 3  # LogonType = Service Account

    # Define task trigger (to run daily at the specified time)
    trigger = task_def.Triggers.Create(2)  # TriggerType = Daily
    trigger.StartBoundary = start_time

    # Define action (execute the provided executable)
    action = task_def.Actions.Create(0)  # ActionType = Execute
    action.Path = exe_path

    # Register the task
    root_folder.RegisterTaskDefinition(
        task_name, task_def, 6, None, None, 3)  # TaskCreate, IgnoreConflicts, StartIfOnBatteries


    print("Task created successfully!")

if __name__ == "__main__":
    task_name = "ReservationTask"
    exe_path = r".\dist\get_res.exe"  # Replace with your executable path
    start_time = "2024-03-30T08:22:00"  # Replace with the desired start time in ISO 8601 format

    create_task(task_name, exe_path, start_time)
