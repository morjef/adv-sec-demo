# Example 9: Command Injection
import subprocess
def execute_command(user_input):
    command = "ls " + user_input #Vulnerable line
    subprocess.run(command, shell=True)
