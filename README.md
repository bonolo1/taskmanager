# taskmanager

## Table of Contents

## Project Description

This project is a task management project management tool. It enables teams to allocate tasks to team members, monitor member tasks to view their status and and generate reports that help to track how the team is doing to identify tasks that are on track or behind to assist with completing the select project to which the tasks relate.

Users are able to create an account, login and create and allocate tasks to relevant team members, update the status of tasks, view tasks and task overview reports. The admin has the additional ability to view the overall statics which include the performance of all users with regards to their tasks and the overall task status.

This task manager tool is valuable to monitor the progress for task completion for a project and identify risk areas to support completion of a project on time.

## Installation
1. Download all the files in the repository which include:
- task_manager.py
- task_overview.txt
- tasks.txt
- user_overview.txt
- user.txt
2. Create a project folder named task_manager.
3. Move and save the downloaded files in the task_manager folder created.
4. Open your local Integrated Development Environment (IDE) such as VSCode.
5. Add the task_manager folder to your IDE.
6. Open the file named task_manager.py and run.
7. Use the program in the IDE terminal (i.e. this is where you can input the data and view output).

## Usage
1. When you run your IDE, ensure that you are in the correct project directory.

Check your location by typing:

```
 pwd
```
if you are not in the appropriate directory, enter:

```
cd task_manager
```

2. Log in.

You can either log in as admin, whereby the credentials are as follows:

<img width="742" alt="Screenshot 2023-04-18 at 17 04 30" src="https://user-images.githubusercontent.com/127111801/232822197-eacbedfa-8253-4df6-8e16-89d799185c27.png">

Or you can log in as a non-admin user, whereby you can use the following credentials:

<img width="742" alt="Screenshot 2023-04-18 at 17 31 09" src="https://user-images.githubusercontent.com/127111801/232827382-3f38945e-9d2c-4859-8f3e-ec1d2071ea4c.png">


Once you login successfully, your will see the notice for that and also the following menu options:

<img width="742" alt="Screenshot 2023-04-18 at 17 17 09" src="https://user-images.githubusercontent.com/127111801/232823294-18a7e896-b3a1-440b-b463-5d7bbc6a1e45.png">

3. To add new users to the task manager, select and enter "r" from the menu.

- Enter a new user name that you would like to add. If a username already exists, you will be notified of this and you'll need to try again with a different new username.
- Once the username has been added, choose a password and confirm the password. You will be notified if the password do not match whereby you'll need to try again with selecting a password.
- A success message will be printed if the passwords match and the new user will be added to the system.

<img width="742" alt="Screenshot 2023-04-18 at 17 04 09" src="https://user-images.githubusercontent.com/127111801/232823637-96d7d068-73c9-4c93-84f0-877b0d3db593.png">


4. To add a new task, select "a" from the menu.

- Enter the user to whom the task is to be assigned. If the user you enter is not in the system, the program will print out the list of usernames from which to select.
- Enter the title for the task.
- Enter the description for the task.
- Enter the the task due date (format: dd mmm yyyy).
- A message will be printed once the task has been successfully added.

<img width="746" alt="Screenshot 2023-04-18 at 17 33 46" src="https://user-images.githubusercontent.com/127111801/232828288-45263143-c478-47d0-ba70-8e0e943231ad.png">

5. To view all tasks in the system, enter "va" which will list all tasks and the related relevant details.

<img width="748" alt="Screenshot 2023-04-18 at 17 37 41" src="https://user-images.githubusercontent.com/127111801/232829277-d77386d6-43a4-4899-96cd-8bf63bc63935.png">

6. To view only the tasks assigned to the user that has logged in (i.e. my tasks), enter "vm":

<img width="809" alt="Screenshot 2023-04-18 at 17 40 51" src="https://user-images.githubusercontent.com/127111801/232829961-66412beb-b4d4-4f36-9023-1a8416dc28c0.png">

- If you would like to return to the main menu, enter "-1"

- If you would like to edit any of the tasks listed, enter the task number. 

<img width="812" alt="Screenshot 2023-04-18 at 17 44 44" src="https://user-images.githubusercontent.com/127111801/232831728-dc0b0505-63cf-4349-8abb-10f1219fc774.png">

Following this, a screen will appear confirming the selection made.

<img width="812" alt="Screenshot 2023-04-18 at 17 44 44" src="https://user-images.githubusercontent.com/127111801/232832606-0353cb21-4c34-451e-8c70-edab84a97727.png">

'- If you would like to mark the selected task as complete, enter "complete".

<img width="812" alt="Screenshot 2023-04-18 at 17 44 44" src="https://user-images.githubusercontent.com/127111801/232833190-4f3d462c-6fdc-496a-a596-6ff332d5c5fc.png">

'- If you would like to edit a selected task, enter "edit" instead of "complete.

<img width="813" alt="Screenshot 2023-04-18 at 17 46 16" src="https://user-images.githubusercontent.com/127111801/232833479-3edf0450-54fe-42f4-a3bb-db0e1f3bd466.png">

The following shows the updated output when entering "vm" from the main menu after the updates. This shows the update from marking task 3 as compelete and editing the date for task 9.

<img width="813" alt="Screenshot 2023-04-18 at 17 55 46" src="https://user-images.githubusercontent.com/127111801/232834240-9c2e4e12-3bec-4e4c-b0d8-5f4230b9d35f.png">












## Credit and Contribution

