
# getRes(0, 5, "6", "30", "mtrotte1", "***REMOVED***", "7044515754", True)
# getRes(restaurant(int), pSize(int), hr(str), min(str), username(str), pswd(str), phone(str), complete(bool))

# Prime is 0, Alo is 1, Kazoku is 2

from get_res import getRes
import tkinter as tk
from tkinter import messagebox

def make_reservation():
    # Get input values
    restaurant = int(restaurant_entry.get())
    party_size = int(party_size_entry.get())
    hour = str(hour_entry.get())
    minute = str(minute_entry.get())
    username = str(username_entry.get())
    password = str(password_entry.get())
    phone_number = int(phone_number_entry.get())
    complete = bool(complete_var.get())

    # Call backend function to make reservation
    try:
        getRes(restaurant, party_size, hour, minute, username, password, phone_number, complete)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to make reservation: {str(e)}")

# Create Tkinter window
root = tk.Tk()
root.title("Restaurant Reservation")

# Create labels and entry fields
tk.Label(root, text="Restaurant Choice:").grid(row=0, column=0)
restaurant_entry = tk.Entry(root)
restaurant_entry.grid(row=0, column=1)

# Create other labels and entry fields for other parameters
tk.Label(root, text="Party Size:").grid(row=1, column=0)
party_size_entry = tk.Entry(root)
party_size_entry.grid(row=1, column=1)

tk.Label(root, text="Hour:").grid(row=2, column=0)
hour_entry = tk.Entry(root)
hour_entry.grid(row=2, column=1)

tk.Label(root, text="Minute:").grid(row=3, column=0)
minute_entry = tk.Entry(root)
minute_entry.grid(row=3, column=1)

tk.Label(root, text="Username:").grid(row=4, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=4, column=1)

tk.Label(root, text="Password:").grid(row=5, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=5, column=1)

tk.Label(root, text="Phone Number:").grid(row=6, column=0)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=6, column=1)

# Use a Checkbutton for 'complete'
complete_var = tk.BooleanVar()
tk.Checkbutton(root, text="Complete", variable=complete_var).grid(row=7, columnspan=2)

# Create button to make reservation
tk.Button(root, text="Make Reservation", command=make_reservation).grid(row=8, columnspan=2)

# Create button to make reservation
tk.Button(root, text="Make Reservation", command=make_reservation).grid(row=8, columnspan=2)

root.mainloop()