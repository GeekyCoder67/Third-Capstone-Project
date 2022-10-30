from datetime import datetime

user_pass_Dict = {}
task_list = []


def gen_task_reportline(tasks):
    # this is dual use for task_overview.txt where it gets the whole task_list
    # and in gen_user_overview where tasks have been filtered by user

    # the return is always:
    # total num tasks,
    # total num of completed,
    # total num of uncompleted,
    # total num of uncompleted and overdue
    # the percentages for all that in the same order

    now = datetime.now()
    num_tasks = len(tasks)
    if num_tasks == 0:
        # this should not be reached
        print("no tasks here!")
        return 0, 0, 0, 0, 0, 0, 0
    completed = 0
    uncompleted = 0
    un_over = 0
    for task in tasks:
        if task[-1]:
            completed += 1
        elif task[3] > now:
            un_over += 1
            uncompleted += 1
        else:
            uncompleted += 1
    return num_tasks, completed, uncompleted, un_over, completed * 100 / num_tasks, uncompleted * 100 / num_tasks, un_over * 100 / num_tasks


def gen_task_overview(do_print=False):
    if len(task_list) ==0:
        report = "No tasks in this category!"
    else:
        num_tasks, completed, uncompleted, un_over, comp_pct, uncomp_pct, un_over_pct = gen_task_reportline(task_list)
        report = "Total number of tasks generated:\t" + str(num_tasks) + "\n"
        report += "Total number of completed tasks:\t" + str(completed) + "\n"
        report += "Total number of uncompleted tasks:\t" + str(uncompleted) + "\n"
        report += "Total number of tardy tasks: \t" + str(un_over) + "\n"
        report += "Percentage of tasks incomplete:\t{:.2f}\n".format(uncomp_pct)
        report += "Percentage of tasks overdue:\t{:.2f}\n".format(un_over_pct)

    f = open("task_overview.txt", "w")  # always overwrite this one!
    f.write(report)
    f.close()
    if do_print:
        print(report)


def gen_user_overview(do_print=False):
    num_users = len(user_pass_Dict.keys())
    num_tasks = len(task_list)
    report = "The number of users registered is:\t" + str(num_users) + "\n"
    report += "The number of tasks generated is:\t" + str(num_tasks) + "\n"
    report += "Now follows a statistic for each user.\n"
    report += "user\tnumber of tasks \tpercentage of total tasks assigned \tpercentage complete \tpercentage incomplete \tpercentage tardy\n"
    users = list(user_pass_Dict.keys())
    tasks_per_user = [[] for x in range(0, len(users))]
    for task in task_list:
        tasks_per_user[users.index(task[0])].append(task)

    for i in range(0, len(users)):
        num_tasks_user, _, _, _, pct_comp, pct_un, pct_un_ov = gen_task_reportline(tasks_per_user[i])
        pct_total_asg = num_tasks_user * 100 / num_tasks
        report += users[i] + "\t"
        report += str(len(tasks_per_user[i])) + "\t\t\t"
        report += "{:.2f}\t\t\t\t\t".format(pct_total_asg)
        report += "{:.2f}\t\t\t".format(pct_comp)
        report += "{:.2f}\t\t\t".format(pct_un)
        report += "{:.2f}\n".format(pct_un_ov)
    # now every user has his list of tasks -> now generate the report lines from that

    f = open("user_overview.txt", "w")  # always overwrite this one!
    f.write(report)
    f.close()
    if do_print:
        print(report)


def reg_user():
    # Username must be followed by a comma and space.
    while True:
        new_username = input("Enter a new username: ").lower()
        if new_username in user_pass_Dict.keys():
            print("\"" + new_username + "\" is already registered. Try a different username please! ")
        else:
            break
    new_password = input("Enter a new password: ")
    confirmation_password = input("Confirm password: ")
    # A file is open and a condition is met to verify the password.
    with open('user.txt', 'r+') as user_document:
        checklist = user_document.readlines()
        if new_password == confirmation_password:
            # seems like convetion to not end on an empty line.
            user_document.write("\n" + new_username + ", " + new_password)
        else:
            print("Incorrect confirmation password: ", confirmation_password)
    user_document.close()
    # and add it to the library to keep it up to date.
    user_pass_Dict[new_username] = new_password


def add_task():
    # This bit of code requests user tasks and must be written followed by a comma and space.
    task_username = input("Username of the person whom the task is assigned to: ").lower()
    task_title = input("Title of the task: ")
    task_description = input("Description of the task: ")
    task_due_date = input("Task due date: (please format it like \"25 Oct 2019\")")
    # put current time using datetime library:
    task_current_date = datetime.now().strftime("%d %b %Y")
    # A file is opened and writes the task information.
    with open('tasks.txt', 'a') as task_document:
        task_document.write(
            "\n" + task_username + ", " + task_title + ", " + task_description + ", " + task_due_date + ", " + task_current_date + ", " + "No")
        task_document.close()
    task_list.append([task_username, task_title, task_description, datetime.strptime(task_due_date, "%d %b %Y"),
                      datetime.strptime(task_current_date, "%d %b %Y"), False])


def view_all():
    # This bit of code opens a file for read and creates list variables.
    file = open('tasks.txt', 'r+', encoding='utf-8')
    username_register = []
    title_register = []
    description_register = []
    due_date_register = []
    current_date_register = []
    task_status_register = []
    task = []
    # This bit of code loops over lines inside a file.
    for line in file:
        chop = line.split(",")
        task.append(chop)

    for title in task:
        print("Task: \t\t", "  ", title[1])
        print("Assigned to: \t", title[0])
        print("Date assigned: ", title[3])
        print("Due date: \t", "  ", title[4])
        print("Task complete? ", title[5])
        print("Task description: \n", title[2])
    file.close()


def view_mine():
    idx = 0
    at_least_once = False
    for title in task_list:
        if username_login == title[0]:
            at_least_once = True
            idx += 1
            print("[" + str(idx) + "] Task: \t\t", "  ", title[1])
            print("Assigned to: \t", title[0])
            print("Date assigned: ", title[3])
            print("Due date: \t", "  ", title[4])
            print("Task complete? ", title[5])
            print("Task description: \n", title[2])

    if not at_least_once:
        print("You have no tasks")
        return

    while True:
        try:
            selected = int(input('Choose index of a task or -1 to return: '))
            if selected == -1:
                return
            elif selected <= idx:
                break
            print("That's not a valid option!")
        except:
            print("That's not a valid option!")
    idx = 0
    for t_idx in range(0, len(task_list)):
        if username_login == task_list[t_idx][0]:
            idx += 1
            if idx == selected:
                idx = t_idx  # now you can refer to it directly in the record
                break

    if task_list[idx][-1]:
        print("Task is complete. Editing no longer possible. Returning.")
        return
    print("Options:\n - c: mark task as completed\n - e: edit the task")
    while True:
        s = input(":")

        # convert s into lower case
        s = s.lower()

        if s == "c":
            task_list[idx][-1] = True
            break
        if s == "e":
            n_date_str = input("Input new due date (empty equals no change):")

            n_user = input("Input user to reassign task. (if invalid no change is made)")

            # i am not doing another loop of "please input it correctly again!"...
            # date is of the form "25 Oct 2019"
            task_list[idx][4] = datetime.strptime(n_date_str, "%d %b %Y") if n_date_str != "" else task_list[idx][4]
            if n_user in user_pass_Dict.keys():
                task_list[idx][0] = n_user
            f = open("tasks.txt", "w")  # too much work to find the right spot, so just write it all
            first = True
            for t in task_list:

                # task_list.append([task_username, task_title, task_description, datetime.strptime(task_due_date, "%d %b %Y"), datetime.strptime(task_current_date, "%d %b %Y"), False]
                if t[-1]:
                    line = "\n" + t[0] + ", " + t[1] + ", " + t[2] + ", " \
                           + t[3].strftime("%d %b %Y") + ", " \
                           + t[4].strftime("%d %b %Y") + ", Yes"
                else:
                    line = "\n" + t[0] + ", " + t[1] \
                           + ", " + t[2] + ", " + t[3].strftime("%d %b %Y") + ", " \
                           + t[4].strftime("%d %b %Y") + ", No"
                if first:
                    first = False
                    line = line[1:]
                f.write(line)
            f.close()
            break


# This bit of code opens a file for reading and creates a dictionary.
credentials_file = open('user.txt', 'r')
checklist = credentials_file.readlines()
credentials_file.close()

# This bit of code loops through the file.
for line in checklist:
    chop = line.split(",")
    clear = chop[1].strip().lower()
    username = chop[0]
    password = clear
    user_pass_Dict[username] = password

# now the same song and dance for the tasks:
tasks_file = open('tasks.txt', 'r')
tasklist = tasks_file.readlines()
tasks_file.close()
for line in tasklist:
    chop = line.split(",")
    if len(chop) == 6:
        task_username = chop[0]
        task_title = chop[1]
        task_description = chop[2]
        task_due_date = chop[3]
        task_current_date = chop[4]
        completed = False
        if chop[5] != " No\n":
            completed = True
        # print(chop)# for debug
        task_list.append([task_username, task_title, task_description, datetime.strptime(task_due_date[1:], "%d %b %Y"),
                          datetime.strptime(task_current_date[1:], "%d %b %Y"), completed])

# This bit of code validates username and password in the file.
while True:
    username_login = input("Please enter your username:")
    password_login = input("Please enter your password:")

    if username_login in user_pass_Dict:
        if user_pass_Dict[username_login] == password_login:
            break

        else:
            print("Incorrect password. Try again.")

    else:
        print("Incorrect username. Try again.")
if username_login == "admin":
    admin_menu_str = str('''Select one of the following Options below:\n''' +
                         '''r - Registering a user\n''' +
                         '''a - Adding a task\n''' +
                         '''va - View all tasks\n''' +
                         '''vm - view my task\n''' +
                         '''gr - generate reports\n''' +
                         '''ds - display statistics\n''' +
                         '''e - Exit\n''' +
                         ''': ''')
else:
    admin_menu_str = str('''Select one of the following Options below:\n''' +
                         '''a - Adding a task\n''' +
                         '''vm - view my task\n''' +
                         '''e - Exit\n''' +
                         ''': ''')
while True:

    menu = input(admin_menu_str).lower()

    if menu == 'r' and username_login == "admin":
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va' and username_login == "admin":
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr' and username_login == "admin":
        gen_task_overview()
        gen_user_overview()

    elif menu == 'ds' and username_login == "admin":
        # if i am super literal then i should just read out the files. instead they are created anew
        # because anything in RAM is bound to be more up-to-date
        print("Now showing statistics for the tasks:\n")
        gen_user_overview(True)
        print("\n\nNow showing statistics for the users:\n")
        gen_task_overview(True)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
# Code ends here.
