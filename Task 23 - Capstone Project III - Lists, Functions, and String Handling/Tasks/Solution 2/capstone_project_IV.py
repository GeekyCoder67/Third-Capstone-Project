# Task 25
# Capstone Project IV - Compulsory Task

# This project works with the previous Capstone project submitted.
# It will make use of lists or dictionaries and functions to extend the functionality of the project.

# This program is designed for use in a small business.
# It works to manage tasks assigned to team members.

# Importing the datetime module to use to compare dates later on in the code i.e. to tell if a task managed is overdue.
import datetime
from datetime import *
        
# Firstly, a few functions need to be defined for use in the program.
# Function 1: reg_user is called when the user selects 'r' to register a user.
def reg_user(menu_choice):

    if menu_choice == "r":  # Setting if statement for menu_choice.

        new_user = input("Please enter a new username: \n")

        # Checking if the username already exists in the usernames_list.
        # Whilst listed, the user is prompted to re-enter a new username and an error message is displayed.
        while new_user in usernames_list:

            print("The username you entered is already listed.")

            new_user = input("Please enter a new username: \n")
   
        # If the new username is not already listed, it is added to usernames_list.
        if new_user not in usernames_list:

            usernames_list.append(new_user)

            user_details["Usernames"] = usernames_list  # The updated list is then updated in the dictionary user_details.
          
        # The user will then be prompted to enter a password.       
        new_password = input("Please enter a new password: \n")

        # The user is asked to confirm their new password.
        pass_confirm = input("Please confirm your new password: \n")        

        # If the new and confirmed password values do not match, an appropriate error message is displayed.
        # The user is then prompted to enter their new password and confirm it until they match.
        while new_password != pass_confirm:

            print("Your confimed password does not match the original password.")
            new_password = input("Please enter your new password: \n")
            pass_confirm = input("Please confirm your new password: \n") 
            
        # If the new and confirmed password values match, a successful message is displayed.
        if new_password == pass_confirm:

            #print("Your password is valid.")

            passwords_list.append(new_password)  # The new password is added to the passwords_list.

            user_details["Passwords"] = passwords_list  # The updated list is updated in the dictionary user_details.

            # user.txt file opened to write to.
            with open('user.txt', 'r+') as f:

                # Using for statement to print username and passwords on separate lines.
                # The number of lines is equal to the number of items in usernames_list.
                for i in range(len(usernames_list)):

                        # Writing from the apppropriate dictionary keys, in the correct format. 
                        f.write(user_details["Usernames"][i] + ", " + user_details["Passwords"][i] + '\n')
                        
        # Message returned at the end of function.
        return("Your new username and password have been successfully added.")


# Function 2: add_task is called when a user selects 'a' to add a new task. 
def add_task(menu_choice):

    if menu_choice == "a":

        import datetime
        from datetime import date

        # Getting user input on the username of the person the task is assigned to.
        name = input("Please enter the username of the person you wish to assign the task to: \n")
        
        # Getting user input on the title of the task being added. 
        title = input("Please enter the title of the task: \n")
        
        # Getting information regarding the description of the added task.
        descrip = input("Please enter a description of the task: \n")

        # Using the previously imported datetime module today() function to calculate the current date.
        current_date = datetime.date.today()

        # Changing the date object to a string in the correct date format.
        assigned_date = current_date.strftime('%d %b %Y')

        # Getting input on the due date of the task being added.
        date_format = input("Please enter the due date of the task (e.g. dd-mm-yyyy): \n")

        date_list = date_format.split("-")

        numbers_date = [int(x) for x in date_list]

        due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime('%d %b %Y') 

        # task_completed is automatically set to "No" when adding a new task. 
        task_completed = "No"

        # Casting all the user input info into a list, to add to the tasks_dict.
        task_list = [name, title, descrip, assigned_date, due_date, task_completed]

        tasks_dict[f"Task {count} details:"] = task_list    

        # Opening the tasks.txt file to enter the new task information.
        with open('tasks.txt', 'r+') as f2:

            # Printing the list values for each key in tasks_dict to a new line.
            for key in tasks_dict:

                line_string = str(tasks_dict[key])  # Casting to a string enabling the info to be written to the file.

                bad_chars = ["[", "]", "\'",]  

                for i in bad_chars:  # Taking out characters pertaining to previous list/dictionary format.

                    line_string = line_string.replace(i, "")

                f2.write(line_string + '\n')  # Writing the correct format of each string line to the file. 

        # Message returned at the end of the function. 
        return("Your new task has been added successfully.")

# Function 3: view_all is called when a user selects 'va' to view all tasks listed in tasks.txt.
# These tasks are already stored in the dictionary 'tasks_dict'.
# Therefore, the dictionary will be used to view all the tasks.
def view_all(menu_choice):

    if menu_choice == "va":

        task_count = 0

        for key in tasks_dict:

            task_count += 1

            print(f"""____________________________________________

Task {str(task_count)}:     {str(tasks_dict[key][1])}
Assigned to:            {str(tasks_dict[key][0])}
Date assigned:          {str(tasks_dict[key][3])}
Due Date:               {str(tasks_dict[key][4])}
Task Complete?          {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
________________________________________________""")

    return("End of Tasks.")

# Function 4: view_mine is called when a user selects 'vm' to view all tasks assigned to them.
def view_mine(menu_choice, username):

    if menu_choice == "vm":

        task_count = 0  # Setting a count for number of tasks.

        for key in tasks_dict:

            task_count += 1  # calculating the total number of tasks by increasing the count through tasks_dict. 

            if username == (tasks_dict[key][0]):  # If the task is assigned to the user, it is displayed.

                print(f"""____________________________________________

Task {str(task_count)}:      \t{str(tasks_dict[key][1])}
Assigned to:        {str(tasks_dict[key][0])}
Date assigned:      {str(tasks_dict[key][3])}
Due Date:           {str(tasks_dict[key][4])}
Task Complete?      {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
________________________________________________""")  # This is a user friendly format with numbered tasks.


    # The user can now choose to either edit a task by number or return to the main menu.
    task_selection = input("\nPlease select a a task by number to edit (e.g. 1, 2,3) or type -1 to return to the main menu. \n")

    if task_selection == "-1":  # If they select '-1', they return to the outer while loop main menu.

        return(menu)        
            
    else:  # If they enter a task number, they can choose to mark as complete or edit.

       option = input("Would you like to mark the task as complete or edit the task? (e.g. mark OR edit) \n")
       
       if option == "mark":

           # If they choose to mark, the item linked to that task for completion is changed to 'Yes' in tasks_dict.
           tasks_dict[f"Task {task_selection} details:"][5] = "Yes"

           return("Your task has been successfully marked as complete.")
                
       # If they choose to edit, the task must be incomplete, i.e. appropriate item in dictionary list equal to 'No'.
       elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "No"):

           #They are given the option to edit username or due date.
           edit_choice = input("Would you like to edit the task username or due date? (Type 'U' or 'D') \n").lower()
      
           if edit_choice == "u":  # If they choose to edit the username, they are prompted to enter a new username for the task.

               name_edit = input("Please enter a new username for the task: \n")

               tasks_dict[f"Task {task_selection} details:"][0] = name_edit  # The new name is assigned in the dictionary.

               return("The task username has been updated successfully.")  # Successful return message.
          
           elif edit_choice == "d":  # If they choose to edit the due date, they are prompted to enter a new date. 

               due_date_change = input("Please enter a new due date (e.g. 12 May 2020) \n")

               tasks_dict[f"Task {task_selection} details:"][4] = due_date_change  # New date is updated in the tasks_dict.

               return("The due date has been updated successfully.")  # Sucessful return message.
            
       elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "Yes"):

           return("You can only edit tasks that are not already complete. \nChoose 'vm' from menu below to select another task to edit.")
           
            

# Function 5: over_due_check
# I decided to define a function to compare dates as this would be a lot of repeated code to incorporate into the actual program.
# This ascertains whether a task is overdue by comparing the due date in the task file and current date,
# i.e., if the current date is greater than the due date, then the task is over due. 
def over_due_check(due_date):

    over_due = False  # Setting Boolean variable for the task as over_due.  

    # Importing datetime and dates to enable the comparison and to retrieve the current date.
    import datetime
    from datetime import date
    

    # The dates in this task are in the format '10 Dec 2015' as a string.
    # So, this needs to be converted to integers to compare dates.
    # First, the variable is split into a list.
    list_dates = due_date.split()
    
    day = int(list_dates[0])  # The first item is cast into an integer and stored in the 'day' variable.
    year = int(list_dates[2])  # The second item is cast into an integer and stored in the 'year' variable.

    # A month dictionary with number values is set to enable calculation of string month into an integer. 
    months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep':  9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    # The corresponding value of the key in months_dict which is equal to list_dates[1] (i.e. 'Dec', 'Oct' etc.) is stored in 'month'.
    # This will be a number value from the appropriate key in months_dict.
    month = months_dict[list_dates[1][0:3]]

    # Getting the current date using the datetime module and formatting it into the same format at the due date initially was.
    date_now = datetime.date.today().strftime('%d %b %Y')

    # The same process is repeated for the current date.
    # Firstly, it is split into a list of items.
    date_now_list = date_now.split()

    day_2 = int(date_now_list[0])  # The first item is stored as an integer in day_2.
    year_2 = int(date_now_list[2])  # Second item is stored as an integer in year_2.
    month_2 = months_dict[date_now_list[1]]  # The corresponding integer value from months_dict at appropriate key is stored in month_2.

    # Now that we have integers for year, day and month to work with, two dates can be created in the correct format for comparison.
    # date_1 is the due date and date_2 is the current date.
    date_1 = date(year, month, day)
    date_2 = date(year_2, month_2, day_2)

    if date_2 > date_1:  # If current date is greater than set due date, over_due is changed to 'True'.

        over_due = True
        return(over_due)  # over_due value is returned.

    elif date_1 > date_2 or date_1 == date_2:  # If set due date is greater than current date, over_due is 'False'.

        over_due = False
        return(over_due)  # over_due value is returned.

# Function 6: Generating text files 'task_overview.txt' and 'user_overview.txt'.
# I made this a function because it is needed twice in the menu, for the 'generate reports' option and 'display statistics.
# I did not want to repeat the code, so therefore a function was needed.
def generate_reports():

    task_overview = ""  # Setting blank strings to store info in to be written to the generated text files.
    user_overview = ""

    tasks_total = len(tasks_dict)  # Total number of tasks is equal to the key count of tasks_dict.
        
    # Adding a string with the total tasks number to the tas_overview string. 
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."

    x = 0  # Setting variables for integers concerning complete tasks, incomplete tasks and overdue tasks respectively.
    y = 0
    z = 0
    
        
    for key in tasks_dict:

        if tasks_dict[key][5] == "Yes":  # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict.

            x += 1  # If the task is complete, i.e. 'Yes' string item is present, variable x is increased by 1.     

        elif tasks_dict[key][5] == "No":  # Checking for which tasks are complete by finding the 'No' string in each key of tasks_dict.

           y += 1  # If the task is complete, i.e. 'No' string item is present, variable y is increased by 1. 

           if over_due_check(tasks_dict[key][4]):  # If the over_due_check function returns 'True', a task is overdue and incomplete.

               z += 1  # 'z' is increased by 1 to count the incomplete, overdue tasks.
            

    # All of the numbers calculated above are now built into sentences in the task_overview string.
    # Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences.
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(x)}." + f"\nThe total number of incomplete tasks is {str(y)}."
    task_overview = task_overview + f"\nThe total number of incomplete and overdue tasks is {str(z)}."
    task_overview = task_overview + f"\nThe percentage of incomplete tasks is {str(round((y / len(tasks_dict)) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are overdue {str(round((z / len(tasks_dict)) * 100, 2))}%."

    # Now generating a 'task_overview' file.
    # The task_overview string is then written to the file in an easy to read format.
    with open('task_overview.txt', 'w') as f3:

        f3.write(task_overview)

    # Setting variables to store information regarding total users, complete tasks for a user, incomplete tasks for the user,
    # incomplete and over-due tasks for the user respectively.
    a = 0
    b = 0
    c = 0
    d = 0

    for key in tasks_dict:

        if tasks_dict[key][0] == username:  # Counting the number of tasks assigned to the user by identifying the first list item.

            a += 1  # Integer 'a' is increased by 1 if the task is for the user.

        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes":  # Checking if the task for the user is complete.

           b += 1  # Integer 'b' is increased by 1 if the task is complete.     

        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No":  # Checking if the task for the user is incomplete.

            c += 1  # Integer 'c' is increased by 1 if the task is incomplete.  

            if over_due_check(tasks_dict[key][4]):  # Checking if the task is incomplete and overdue.

                d += 1  # If overdue, integer 'd' is increased by 1.
         
    # Writing all the info calculated above into sentence strings which are built into the user_overview string variable.
    user_overview = user_overview + f"The total number of users registered with task_manager.py is {str(len(user_details))}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks assigned to {username} is {str(a)}."
    user_overview = user_overview + f"\nThe percentage of the total number of tasks assigned to {username} is {str(round((a / len(tasks_dict)) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks assigned to {username} that have been completed is {str(round((b / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {username} is {str(round((c / a) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of incomplete and overdue tasks assigned to {username} is {str(round((d / a) * 100, 2))}%."

    # Now generating a 'user_overview' file.
    # The user_overview string is then written to the file in an easy to read format.
    with open('user_overview.txt', 'w') as f4:

        f4.write(user_overview)        

    # The user then views a message stating that their reports have been successfully generated.
    # They do not have the option to view the reports.
    # The admin user can select to display statistics from their main menu.
    return("Your reports have been generated successfully.")

    
# Writing the program.    
# Firstly, I will build the current info from tasks.txt and user.txt into appropriate lists and dictionaries.
# This will allow me to build and work with the information in an easier way. 
# In the first version of this code, I used a string to store the user and task contents.
# Now, the user and tasks details will be stored in corresponding dictionaries for use in the program.
user_details = {}

# The user details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
usernames_list = []
passwords_list = []

tasks_dict = {}

# Opening the tasks.txt file to read and write information from it.
# Adding the info in the user.txt file into the set list.
with open('user.txt', 'r+') as f:

    for line in f:

        newline = line.rstrip('\n')  # Stripping newline characters from the line.
        
        split_line = newline.split(", ")  # Splitting the line into a list.
        
        usernames_list.append(split_line[0])  # Assigning items from the list into corresponding list.
        passwords_list.append(split_line[1])

        user_details["Usernames"] = usernames_list  # Lists are now stored as values assigned to keys in user_details dictionary.
        user_details["Passwords"] = passwords_list      


# Setting a count to keep track of the number of lines in the tasks.txt file.
count = 1

# Opening the tasks.txt file to read and write information to it.
with open('tasks.txt', 'r+') as f2:

    for line in f2:

        
        newline = line.rstrip('\n')  # Stripping newline characters.
        
        split_line = newline.split(", ")  # Splitting line into a list of items.

        tasks_dict[f"Task {count} details:"] = split_line # Assigning each list of items to a key in tasks_dict.

        count += 1  # Count used to change key value for each list of info.


# Writing the program for the task manager.
# Getting input from the user on their login details.
username = input("Please enter your username: \n")
password = input("Please enter your password: \n")

# Creating a while loop to run indefinitely whilst login details are incorrect.
# Appropriate error messages are displayed.
# Use of the words 'in' and 'not in' used to test whether the username and password appear in the appropriate lists.
while (username not in usernames_list) or (password not in passwords_list):

        # If username is correct and password is correct, the following message is displayed.
        if (username not in usernames_list) and (password in passwords_list):

            print("Your username is not listed.")

            username = input("Please re-enter your username: \n")  # User is prompted to re-enter details. 
            password = input("Please re-enter your password: \n")

        # If password is incorrect and username is correct, the following message is displayed.
        elif (password not in passwords_list) and (username in usernames_list):

            print("Your password is incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

        # If both the username and password are incorrect, the following message is displayed. 
        elif (username not in usernames_list) and (password not in passwords_list):

            print("Your username and password are incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

# If both username and password are correct, the successful login message is displayed.            
if (username in usernames_list) and (password in passwords_list):

    print("You are successfully logged in.")


# Indefinite loop created to display the menu once the user is logged in.
# This allows the user to return to the menu after each option.
# If they wish to exit the program, they can choose the 'exit' option from the menu. 
while 1:

    if username == "admin":  # The admin user views a specific menu with extra options (gr and ds).

        menu = input("""\nPlease select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit

""").lower()            

    else:  # All other users can only view the basic menu. 

       menu = input("""\nPlease select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
e - exit

""").lower()
    
    if menu == "r":  # Choosing 'r' from the menu causes the reg_user function to be called.

        print(reg_user(menu))

    elif menu == "a":

        print(add_task(menu))

    elif menu == "va":  # Choosing 'va' from the menu causes the view_all function to be called.

        print(view_all(menu))

    elif menu == "vm":  # Choosing 'vm' from the menu causes the view_mine function to be called.

       print(view_mine(menu, username))

    elif menu == "gr":  # Choosing 'gr' from the menu causes text files user_overview and task_overview to be generated.

        print(generate_reports())  # Calling function to generate report files.
        
    elif menu == 'ds':

        print(generate_reports())  # Calling function generate files in case they do no exist yet.

        print("""\n____________________________________________________

The task overview report is as follows:
____________________________________________________\n""")  # Heading printed for user-friendly display.

        with open('task_overview.txt', 'r+') as f3:  # Opening the task_overview file to get info from it.

            for line in f3:

                print(line)  # Printing/displaying each line in the file.

        print("""\n_____________________________________________________

The user overview report is as follows:
_____________________________________________________\n""")  # Heading printed for user_friendly display.

        with open('user_overview.txt', 'r+') as f4:  # Opening user_overview file.

            for line in f4:

                print(line)  # Displaying each line of the file.

        print("""\n______________________________________________________

End of Statistics Reports
______________________________________________________\n""")  # End of reports display.

    elif menu == "e":  # If the user selects 'e' they can log out of the program.

        print("You are successfully logged out.")

        break  # break statement ends the infinte while loop to exit the program. 
        

                    

                

                

           

                    
                

        

    




           





        

    

    




    





    

        

        

        


            

            
            

                    

                    

                

                

                

            



            






                       








