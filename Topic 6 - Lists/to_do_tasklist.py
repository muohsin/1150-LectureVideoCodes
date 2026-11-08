
# Create an empty list to store the user's tasks.
todo_list = []

# Keep asking for tasks until the user presses Enter without typing anything.
while True:
    task = input('Enter your task, or press enter to stop: ')

    # If the user enters a task, add it to the list.
    if task:
        if task in todo_list:
            print('You have already done this task')
        else:
            todo_list.append(task)
        todo_list.append(task)

    # If the user enters nothing, stop asking for more tasks.
    else:
        break

# Thank the user after they finish entering their tasks.
print('Thank you, your tasks are:')

# # Display the complete list of tasks.
# print(todo_list)
#
# # Go through the list and display each task on its own line.
# for task in todo_list:
#     print(task)
#
# # Count how many tasks the user entered.
# number_of_tasks = len(todo_list)

# Go through the list and get both the index and the task.
for index, task in enumerate(todo_list):
    # Display each task with its index number.
    print(f'Task {index+1} is {task}')

# Tell the user how many tasks they have to do.
print(f'You have {len(todo_list)} tasks to do.')
