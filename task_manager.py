
"""
Note for reviewer: Please use my tasks.txt file when running the program. Thank you
"""

#===== importing libraries ===========

import datetime
from datetime import date

#===== Defining Functions ===========

# Define login function.
# Request user to enter an existing username and matching password to log into the system
# Print out error messages if user enters login details that are not valid
def login(username):

    # Validate the user's login details by determining whether the username and password is stored in the "user.txt" file
    # Open and read the user.txt file to read the usernames and associated password for each user
    with open("user.txt", "r") as file_login:

        # Combine the usernames in a list which can be searched through going forward.
        # Combine the passwords in a seperate list which can be searched through going forward.
        # Usernames and passwords will be linked as the index position of the relevant username in the username list will 
        # be the same as the index position of the password in the pwassword list.
        for lines in file_login:
            username_details = lines.split(", ")
            username_list.append(username_details[0])
            password_list.append(username_details[1].strip("\n"))

    # Use while loops to determine whether the username and password are in the user.txt file.
    # Repeatedly request user to enter a valid username and password until they provide the appropriate credentials.
    # Remove case-sensitivity of the username by converting to user input to lower case
    if username.lower() in username_list:
        password = input("Enter your password: ")

    else: 
        while username.lower() not in username_list:
            username = input("Error: Invalid username. The username you entered is not in the system. \nPlease enter a valid username: ")
        
            if username.lower() in username_list:
                password = input("Enter your password: ")
                break  

    # Obtain the index position of the username from the username list in order to determine the associated password with the username, 
    # by applying the index number obtained to the password list as well.
    # Password should be case-sensitive for additional security.
    existing_password_index = username_list.index(username.lower())

    if password == password_list[existing_password_index]:
        print("Thank you for your details. You have successfully logged in.")

    else:
        while password != password_list[existing_password_index]:
            password = input("Error: Password incorrect. Please enter the correct password: ")

            if password == password_list[existing_password_index]:
                print("Thank you for your details. You have successfully logged in.")
                break

# Define function that enables a user to register a new user by creating a new username and associated password.
# The function ensures that user should confirm the new password.
# The User is only registered once the confirmed password matches the value of the password entere.
# The function ensures that the user cannot duplicate any existing usernames that already exist.
# If the user attempts to add an existing username, the user will receive an error message and be required to enter a different username.
def register_user(new_username):
    while new_username.lower() in username_list:
        print("Error: This username already exists. Please select a different new username.")
        new_username = input("Enter a new username: ")

    if new_username.lower() not in username_list:
        while new_username:
            new_password = input("Enter a new password: ")
            password_confirm =  input("Confirm password by entering the new password again: ")

            if password_confirm == new_password:
                with open("user.txt", "a") as file1:
                    file1.write("\n" + new_username.lower() + ", " + password_confirm)
                print("New account registration is successful and complete.")
                break       
            else:
                print("Password confirmation entered does not match the intitial password entered.")

# Define a function that enables user to add a new task to the task.txt file, with the relevant details
# Add the data to the file task.txt and
# Include 'No' when the new task is added to indicate if the task is complete or not.   
def add_task(username_task, task_title, task_description, task_assigned_date , task_due_date):

    new_task_number = number_tasks_in_file() + 1

    with open("tasks.txt", "a") as file2:
        file2.write("\n" + str(new_task_number) + ". " + username_task.lower() + ", " + task_title + ", " + task_description + ", " + task_assigned_date + ", "  + task_due_date)
        file2.write(", No")

# Define function to calculate the number of tasks that have been generated and tracked using the tasks_manage.py program
def number_tasks_in_file():

    number_of_tasks = 0

    with open("tasks.txt", "r") as file2:
        for lines in file2:
            tasks = lines.strip("\n")
            tasks = tasks.split(",")
            number_of_tasks += 1
        return number_of_tasks

# Define function to view all tasks.
# Open and read the "tasks.txt" file and print out all the related task information available.
def view_all_tasks():

    list_task_headings = ["Task:", "Assigned to:", "Date assigned:", "Due date:", "Task complete:", "Task description:" ]
    index = 0

    with open("tasks.txt", "r") as file2:

        for lines in file2:
            task_details = lines.strip("\n").replace(".", ",")
            task_details = task_details.split(", ")
            print(" ")

            list_task_details= [task_details[2], task_details[1],task_details[4], task_details[5], task_details[6], task_details[3]]

            for index in range(0, len(list_task_details)):
                print(f"{list_task_headings[index]:<20} {list_task_details[index]}")

# Define function to create a dictionary from the tasks in the task
def task_dictionary():       
    list_tasks = []

    # open the "tasks.txt file and read from the file
    # cast the the task numbers into an integer
    # create a dictionary where the task number is the key and the task details are the value
    with open("tasks.txt", "r") as file2:

        for lines in file2:
            task_details = lines.split(". ")
            list_tasks.append((int(task_details[0]), task_details[1].replace("\n","")))
        
            task_dict = dict(list_tasks)
    return task_dict

# Define function that confirms whether tasks have been assgined to the user
def confirm_tasks_assigned_to_user(username):
    task_dict = task_dictionary()
    for key in task_dict:
        task_detail_per_category = task_dict[key].split(",")
        task_assigned_to = task_detail_per_category[0]
        if task_assigned_to.lower() == username.lower():
            return True

# Define function for the user to view their own tasks
# in the function, if none of the tasks are assigned to the user logged in, display a message to notify the user of that
def view_my_tasks():
    username_in_list_test = 0

    task_dict = task_dictionary()

    for key in task_dict:
        task_detail_per_category = task_dict[key].split(",")
        task_assigned_to = task_detail_per_category[0]

        if task_assigned_to.lower() == username.lower():
            task_details_ordered = [key, task_detail_per_category[1].strip(" "), task_detail_per_category[0], task_detail_per_category[3].strip(" "), task_detail_per_category[4].strip(" "), task_detail_per_category[5].strip(" "), task_detail_per_category[2].strip(" ")]

            for index in range(0, len(list_task_headings)):
                    print(f"{list_task_headings[index]:<30} {task_details_ordered[index]}")
            print("")
            
            # If the user has a task assigned to them, add 1 to the variable "username_in_list_test" to indicate that they have a task assigned.
            # If there are no tasks assigned to the user (shown by the variable "username_in_list_test" having a value of "0" ), print out a
            # message indicating that.      
            username_in_list_test += 1

    if username_in_list_test == 0:
        print("You currently have no tasks that have been assigned to you. Please check again later.")


# Define function where user can select a specific task assgined to them and
# can decide whether to mark the task as complete or edit the task assigned to username or due date.
# The user has the option to input "-1" if they choose to make no updates and exit   
def edit_tasks_assigned_to_user():
    task_confirmed_assgined_to_user = confirm_tasks_assigned_to_user(username)

    if task_confirmed_assgined_to_user == True:
        
        task_dict = task_dictionary()
        # Request user to select the task they could like to edit by entering the task number

        user_selection = int(input("Select either the specific task you would like to edit by entering the associated task number or enter '-1' return to the main menu: "))

        if user_selection in task_dict :

            # Print out the specific task they have selected as confirmation of their selection
            task_detail_per_category = task_dict[user_selection].split(",")
            task_assigned_to = task_detail_per_category[0]

            if task_assigned_to.lower() == username.lower():
                task_details_ordered = [user_selection, task_detail_per_category[1].strip(" "), task_detail_per_category[0], task_detail_per_category[3].strip(" "), task_detail_per_category[4].strip(" "), task_detail_per_category[5].strip(" "), task_detail_per_category[2].strip(" ")]
            
                print("Your task selection is the following: ")

                for index in range(0, len(list_task_headings)):
                    print(f"{list_task_headings[index]:<30} {task_details_ordered[index]}")
        
                # Of the specific task selected by the user, request the user to indicate whether they would like to
                # either mark the task as complete or edit the task.
                specific_task_update = input("Would you like to mark the task as complete (if so enter 'complete') or edit the task (if so, enter 'edit') ")

                # If user selects to mark the task as complete, update the tasks.txt file to change the completion status to "Yes"
                if specific_task_update.lower() == "complete":
                    task_detail_per_category[5]= " Yes"
                    updated_task_details = f"{user_selection}. {','.join(task_detail_per_category)}\n"

                    with open("tasks.txt", "r") as file2:
                        tasks_from_file = file2.readlines()
                    
                    tasks_from_file[user_selection - 1] = updated_task_details 

                    with open("tasks.txt", "w") as file2:
                        file2.writelines(tasks_from_file)

                # If the user selects to edit, request user to indicate whether they would like to edit the task assigned username and/or task due date.
                # Based on the user selection of what to edit, update and write the updated details inputed by the user to the external "tasks.txt" file.
                elif specific_task_update.lower() == "edit":

                    # Enable user to only edit the task if it has not been marked as complete
                    # If task is not marked as completed, proceed to ask the user further quaestions for the edit
                    if task_detail_per_category[5].lower() == " no":
                        edit_task_username = input("Would you like to update the task username (Yes/No): ")

                        if edit_task_username.lower() == "yes":
                            updated_task_username = input("Enter the new username for the task: ")
                            task_detail_per_category[0] = updated_task_username.lower()

                        edit_task_username = input("Would you like to update the due date for the task (Yes/No): ")
                        
                        if edit_task_username.lower() == "yes":
                            while True:
                                updated_task_due_date = input("Enter the new due date for the task (format: dd mmm yyyy): ")
                                if len(updated_task_due_date) == 11 and int(updated_task_due_date[0:2]) < 32 and len(updated_task_due_date[4:7])== 3 and int(updated_task_due_date[7:11]) > 0 and len(updated_task_due_date[7:11]) == 4:
                                    task_detail_per_category[4] = f" {updated_task_due_date}"

                                    updated_task_details = f"{user_selection}. {','.join(task_detail_per_category)}\n"

                                    with open("tasks.txt", "r") as file2:
                                        tasks_from_file = file2.readlines()
                                                    
                                    tasks_from_file[user_selection - 1] = updated_task_details 

                                    with open("tasks.txt", "w") as file2:
                                        file2.writelines(tasks_from_file)
                                        break

                                else: 
                                    print("Error: The value entered for the date is invalid. The format should be: mm ddd yyyy. Please try again")

                    elif task_detail_per_category[5].lower() == " yes":
                        print("Error. You can only edit this if the task is complete. Please select a different option.")

            else:
                print("Error: you have not selected from the task numbers assigned to you nor the number to exit. Please try again.")

        # if the user selects -1, enable user to return to the main menu
        elif user_selection == -1:
            print("You are about to return to the main menu.")

        # if the user does not select either one of the tasks assigned to them nor "-1", print out an error message
        else:
            print("Error: Task input selected is not valid. Please enter a task number (in the form of an integer) of a task that has been indicated as assigned to you above.")


# Define function that calculates the total number of completed tasks
def total_number_completed_tasks():
    
    number_of_completed_tasks = 0

    with open("tasks.txt", "r") as file2:
        for lines in file2:    
            tasks = lines.strip("\n")
            tasks = tasks.split(",")
            if tasks[5].lower() == " yes":
                number_of_completed_tasks += 1
        return number_of_completed_tasks

# Define function that calculates the total number of uncompleted tasks
def total_number_uncompleted_tasks():
    
    number_of_uncompleted_tasks = 0

    with open("tasks.txt", "r") as file2:
        for lines in file2:    
            tasks = lines.strip("\n")
            tasks = tasks.split(",")
            if tasks[5].lower() == " no":
                number_of_uncompleted_tasks += 1
        return number_of_uncompleted_tasks

# Define function that calculates the total number of tasks that have not been completed and that are overdue  
def total_number_uncompleted_overdue_tasks():
    
    number_of_uncompleted_overdue_tasks = 0

    date_today = date.today()

    with open("tasks.txt", "r") as file2:
        for lines in file2:    
            tasks = lines.strip("\n")
            tasks = tasks.split(",")

            # convert the due date to the appropriate format to be able to compare to the date today from the datetime module
            due_date_string = tasks[4].strip(" ")
            format_str = '%d %b %Y'
            due_date_converted = datetime.datetime.strptime(due_date_string, format_str).date()

            if due_date_converted < date_today and tasks[5].lower() == " no":
                number_of_uncompleted_overdue_tasks += 1
        return number_of_uncompleted_overdue_tasks       
    

# Define function to generate a report showing the task overview statistics
def generate_task_overview_report():
    # In an external file named "task_overview.txt", generate a report that displays the following:
    # - The total number of tasks that have been generated and tracked using the task_manager.py.
    # - The total number of completed tasks.
    # - The total number of uncompleted tasks.
    # - The total number of tasks that haven’t been completed and that are overdue.
    # - The percentage of tasks that are incomplete.
    # - The percentage of tasks that are overdue (which means the tasks are overdue and incomplete as at the current date)

    percentage_tasks_incomplete = round(total_number_uncompleted_tasks()/number_tasks_in_file() * 100, 2)
    percentage_tasks_overdue = round(total_number_uncompleted_overdue_tasks()/number_tasks_in_file() * 100, 2)

    with open("task_overview.txt","w") as file3:
        file3.write(f"Total number of tasks generated and tracked: {str(number_tasks_in_file())}\n")
        file3.write(f"Total number of completed tasks: {str(total_number_completed_tasks())}\n")
        file3.write(f"Total number of uncompleted tasks: {str(total_number_uncompleted_tasks())}\n")
        file3.write(f"Total number of tasks that haven’t been completed and that are overdue: {str(total_number_uncompleted_overdue_tasks())}\n")
        file3.write(f"Percentage of tasks that are incomplete: {str(percentage_tasks_incomplete)}%\n")
        file3.write(f"Percentage of tasks that are overdue: {str(percentage_tasks_overdue)}%\n")

# Define function to determine the total number of users registered with the task.py program
def total_registered_users():

    number_of_users = 0

    with open("user.txt", "r") as file1:
        for lines in file1:
            user_detail = lines.strip("\n")
            number_of_users += 1
        return number_of_users

# Define function that calculates the total number of tasks assigned to a particular user
def total_tasks_assigned_user(username):

    number_of_tasks_assigned_user = 0

    with open("tasks.txt", "r") as file2:
        for lines in file2:    
            tasks = lines.strip("\n").replace(". ", ",")
            tasks = tasks.split(",")
            user_in_task = tasks[1]

            if user_in_task.lower() == username.lower():
                number_of_tasks_assigned_user += 1
        return number_of_tasks_assigned_user

# Define function that calculates the total number of tasks assigned to a particular user that have been completed
def total_tasks_completed_assigned_user(username):

    number_of_tasks_assigned_user = 0

    with open("tasks.txt", "r") as file2:
        for lines in file2:    
            tasks = lines.strip("\n").replace(". ", ",")
            tasks = tasks.split(",")
            task_status = tasks[6].replace(" ","")
            user_in_task = tasks[1]

            if user_in_task.lower() == username.lower() and task_status.lower() == "yes":
                number_of_tasks_assigned_user += 1
        return number_of_tasks_assigned_user

# Define function that calculates the total number of tasks assigned to a particular user that are incomplete and overdue
def total_tasks_uncompleted_and_overdue_assigned_user(username):

    number_of_tasks_assigned_user = 0

    date_today = date.today()

    with open("tasks.txt", "r") as file2:
        for lines in file2:    
            tasks = lines.strip("\n").replace(". ", ",")
            tasks = tasks.split(",")

            task_status = tasks[6].replace(" ","")

            user_in_task = tasks[1]

            # convert the due date to the appropriate format to be able to compare to the date today from the datetime module
            due_date_string = tasks[5].strip(" ")
            format_str = '%d %b %Y'
            due_date_converted = datetime.datetime.strptime(due_date_string, format_str).date()

            if user_in_task.lower() == username.lower() and task_status.lower() == "no" and due_date_converted < date_today:
                number_of_tasks_assigned_user += 1
        return number_of_tasks_assigned_user


# Define function to generate a report showing the user overview statistics
def generate_user_overview_report():
    # In an external file named "user_overview.txt", generate a report that displays the following:
    # - The total number of users registered with tasks_manager.py program
    # - The total number of tasks that have been generated and tracked using task_manager.py.
    # - For each user:
    #          - Total number of tasks assigned to that user.
    #          - Percentage of the total number of tasks that have been assigned to that user
    #          - Percentage of the tasks assigned to that user that have been completed
    #          - Percentage of the tasks assigned to that user that must still be completed
    #          - Percentage of the tasks assigned to that user that have not yet been completed and are overdue
    # Indicate "N/A" where no tasks have been assigned to user and the percentage calculation would cause an error due to dividing a number by zero

    with open("user_overview.txt","w") as file4:
        file4.write(f"Total number of users registered with tasks_manager.py: {str(total_registered_users())}\n")
        file4.write(f"Total number of tasks that have been generated and tracked using task_manager.py: {str(number_tasks_in_file())}\n")

        for user in username_list:

            percent_tasks_assigned_to_user = round(total_tasks_assigned_user(user)/number_tasks_in_file() * 100, 2)

            try: 
                percent_tasks_assigned_to_user_complete = round(total_tasks_completed_assigned_user(user)/total_tasks_assigned_user(user) * 100, 2)
            except ZeroDivisionError:
                percent_tasks_assigned_to_user_complete = "N/A"
                

            try: 
                percent_tasks_assigned_to_user_incomplete = round((total_tasks_assigned_user(user) - total_tasks_completed_assigned_user(user))/total_tasks_assigned_user(user) *100, 2)
            except ZeroDivisionError:
                percent_tasks_assigned_to_user_incomplete = "N/A"

            try: 
                percent_tasks_assigned_to_user_incomplete_and_overdue = round(total_tasks_uncompleted_and_overdue_assigned_user(user)/total_tasks_assigned_user(user) * 100, 2)
            except ZeroDivisionError:
                percent_tasks_assigned_to_user_incomplete_and_overdue = "N/A"

            file4.write(f"\n{user} user details:\n")

            file4.write(f"Total number of tasks assigned to {user}: {str(total_tasks_assigned_user(user))}\n")
            file4.write(f"Percentage of total number of tasks assigned to {user}: {str(percent_tasks_assigned_to_user)}%\n")
            file4.write(f"Percentage of tasks assigned to {user} that have been completed: {str(percent_tasks_assigned_to_user_complete)}%\n")
            file4.write(f"Percentage of tasks assigned to {user} that have not been completed: {str(percent_tasks_assigned_to_user_incomplete)}%\n")
            file4.write(f"Percentage of tasks assigned to {user} that have not been completed and are overdue: {str(percent_tasks_assigned_to_user_incomplete_and_overdue)}%\n")



#===== Lists for Storage ==========

list_task_headings = ["Task number:", "Task:", "Assigned to:", "Date assigned:", "Due date:", "Task complete:", "Task description:" ]

username_list = []

password_list = []

#===== Program ==========

print("Login: ")

# Request user to enter their username. 
# Once username is entered, call the login function where the user will be required to enter a valid
# password that is associated with the username in order to be able to proceed.
username = input("Enter your username: ")

login(username)

while True:
    # Present the menu of options available to the the user logged in as admin, which includes the option to view statistics.
    # Remove case-sensitivity of the username.
    if username.lower() == "admin":
            menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - Generate reports
        ds - Display statistics
        e - Exit
        : ''').lower()

    # Present the menu of options available to other users that are not logged in as admin, which exclude the view statistics option
    else:
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - Generate reports
        e - Exit
        : ''').lower()
 

    if menu == 'r':
    # If the user selects "r" and is logged in as admin, enable user to register a new user.
    # Request user enter the new username they would like to register.
    # Call the register_user function to register the user, with their associated password and add their details to the user.txt file.
        if username.lower() == "admin":
            new_username = input("Enter a new username: ")
            register_user(new_username)
        else:
            print("Only admin user can register new users. If you're admin, please log in as admin and if you're not admin, please select a different option from the menu.")


    elif menu == 'a':
    # If user selects "a", call the function that enables user to add a new task to the task.txt file

        # Request user to input the following details: 
        # - A username of the person whom the task is assigned to,
        # - A title of a task,
        # - A description of the task and 
        # - the due date of the task.
        # - Then get the current date.
        username_task = input("Enter the username of the person to whom the task is assigned: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")

        # Request user to enter the due date for the task
        # Print out error message and request the user to try again if their format differs to the required format
        # and the date entered is not valid.
        while True:
            try:
                task_due_date= input("Enter the the task due date (format: dd mmm yyyy): ")
                if len(task_due_date) == 11 and int(task_due_date[0:2]) < 32 and len(task_due_date[4:7])== 3 and int(task_due_date[7:11]) > 0 and len(task_due_date[7:11]) == 4:
                    break
                else:
                    print("Error: The value entered for the date is invalid. The format should be: mm ddd yyyy. Please try again")
            except ValueError:
                print("Error: The value entered for the date is invalid. The format should be: mm ddd yyyy. Please try again")


        # Use datetime module to automatically determine the current date for the task assigned date.
        today = date.today()
        task_assigned_date = today.strftime("%d %b %Y")

        # If the username entered matches a username already in the system, call the add_task(function) to add the
        # new task to the tasks.txt file.
        # If the user tries to assign and add a task to as username that is not in the system,
        # print out an error for an invalid input and request the user to try again
        if username_task.lower() in username_list:
            add_task(username_task, task_title, task_description, task_assigned_date, task_due_date)
            print("Done- You have successfully added the task.")
        else:
            print("Error: The user you are assigning this task to does not exist in the system. Please try again. ")
            print(f"To assist, the available users to which you can assign tasks are as follows: ")
            for username in username_list:
                print(username)
            

    elif menu == 'va':
    # if user selects "va", call the view_all_tasks function to print out all of the tasks in system.

        view_all_tasks()


    elif menu == 'vm':
    # if user selects "vm", enable user to view their own tasks assigned to them

        # call function to print out the tasks that are assigned to the user
        view_my_tasks()

        # Call function that provides the user to either mark any of the tasks assigned to them as complete
        # or edit the task assigned to username or task assigned due date.
        # Update the external tasks.txt file with their selected updates (if any).
        edit_tasks_assigned_to_user()
   

    elif menu == 'gr':
    # If the user selects "gr", enable the user to generate 2 reports: "task overview.txt and the "user_overview.txt"
    # If these text files don’t exist (because the user hasn’t selected to generate them yet), first call the code to generate the text files.

        generate_task_overview_report()

        generate_user_overview_report()

                
    elif menu == 'ds' and username.lower() == "admin":
    # if the user is logged in as admin, when the user selects "ds",
    # enable user to view and display the user over statistics from the "user_overview.txt file and
    # task overview statistics from the "task_over_view.txt" file
    
        generate_task_overview_report()

        generate_user_overview_report()

        with open("user_overview.txt", "r") as file4:
            print("User Overview Statistics:")
            print(file4.read())

        with open("task_overview.txt", "r") as file3:
            print("Task Overview Statistics:")
            print(file3.read())


# if user selects "e", exit them from the program and diplay to notify them of that
    elif menu == 'e':
        print('You have logged out. Goodbye!')
        exit()


    else:
        print("You have made a wrong choice. Please Try again")