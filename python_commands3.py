import subprocess

def check_and_install_package(package_name):

   try:

    command_first = ("dpkg", "-s", package_name)
    subprocess.run(command_first, check= True, stdout=subprocess.PIPE)
    print(f"{package_name} is already installed.")
  
   except subprocess.CalledProcessError:

    print(f'{package_name} is not installed')
    command = ["sudo", "apt-get", "install", package_name, "-y"]

    subprocess.run(command, check=True)

   
check_and_install_package("httrack")
 

