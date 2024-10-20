# Program info: Creates an executable from the name of the script passed in. If this program is run directly and not as a module it will prompt user input for the script name.

import subprocess

def create_executable(script_name):
    # Attempt to create the executable
    try:
        subprocess.run(["pyinstaller", "--onefile", script_name], check=True)
        print("Executable created successfully!")
    # Return error if failed
    except subprocess.CalledProcessError:
        print("Error: Failed to create executable.")

if __name__ == "__main__":
    script_name = input("Enter the name of your Python script (without the .py extension): ")
    create_executable(script_name + ".py")

