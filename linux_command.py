import subprocess

def run_command(command):

    result = subprocess.run(command , shell=True ,text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.stderr:
        print("Error:", result.stderr)

    if result.stdout:
        print(result.stdout)


def run_command(command):

    result = subprocess.run(command , shell=True ,text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.stderr:
        print("Error:", result.stderr)

    if result.stdout:
        print(result.stdout)

for i in range(1,6):
    dir_name = f"my_test_directory{i}"

    print(f"Creating a directory {dir_name}...")

    run_command(f"mkdir {dir_name}")




print("Creating directory...")
run_command("mkdir my_file_directory")

print("Creating file...")
with open("my_file_directory/test_file.txt", "w") as file:
    file.write("Hello, this is a test file.")

print("Listing directory contents...")
run_command("ls -l my_file_directory")


