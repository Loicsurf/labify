# labify
This is my lab application
  The project Computerize Management of Hospital Laboratory includes registration of patients, storing their details into the system, and also computerized billing in the pharmacy, and labs. The software has the facility to give a unique id for every patient and stores the clinical details of every patient and hospital tests done automatically. It includes a search facility to know the current status of each patient. User can search details of a patient using the id. The platform can be entered using a username and password. It is accessible either by an administrator or a lab technician. Only they can add data into the database. The data can be retrieved easily. The interface is very user-friendly. The data are well protected for personal use and makes the data processing very fast.
  
  I. Installation Guide
In other to have the application running there are some requirements we have to fulfill to have it up and working.
a. Requirements

Ø Python

Ø Any browser but preferably Google Chrome Ø Django Framework

Ø Terminal or command line prompt.

b. Installation

Prepare Your Environment

  When you’re ready to start your new Django web application, create a new folder and navigate into it. In this folder, you’ll set up a new virtual environment using your command line:
  
$ python3 -m venv env

This command sets up a new virtual environment namedenvin your current working directory. Once the process is complete, you also need to activate the virtual environment:

$ source env/bin/activate

If the activation was successful, then you’ll see the name of your virtual environment, (env), at the beginning of your command prompt. This means that your environment setup is complete.

You can learn more about how to work with virtual environments in Python, and how to perfect your Python development setup, but for your Django setup, you have all you need. You can continue with installing the django package.

Install Django and Pin Your Dependencies
Once you’ve created and activated your Python virtual environment, you can install Django into this dedicated development workspace:

(env) $ python -m pip install django

This command fetches the django package from the Python Package Index (PyPI) using pip. After the installation has completed, you can pin your dependencies to make sure that you’re keeping track of which Django version you installed:

(env) $ python -m pip freeze > requirements.txt

This command writes the names and versions of all external Python packages that are currently in your virtual environment to a file calledrequirements.txt. This file will include the django package and all of its dependencies.

(env) $ python -m pip install django==4.1.1

You should always include a record of the versions of all packages you used in your project code, such as in arequirements.txtfile. The requirements.txtfile allows you and other programmers to reproduce the exact conditions of your project build.

Suppose you’re working on an existing project with its dependencies already pinned in a requirements.txt file. In that case, you can install the right Django version as well as all the other necessary packages in a single command:

(env) $ python -m pip install -r requirements.txt

The command reads all names and versions of the pinned packages from yourrequirements.txtfile and installs the specified version of each package in your virtual environment.

Keeping a separate virtual environment for every project allows you to work with different versions of Django for different web application projects. Pinning the dependencies with pip freeze enables you to reproduce the environment that you need for the project to work as expected.
