# Homework Lab 6 - Lists

# Create two empty lists to store unfinished and completed tasks.
todo_list = []
completed_list = []

# Keep asking for tasks until the user presses Enter without typing anything.
while True:
    task = input('Enter your task, or press enter to stop: ')

    # If the user enters nothing, stop asking for more tasks.
    if not task:
        break

    # Ask the user if they have completed the task.
    completed = input('Have you completed this task? (yes/no): ').lower()

    # If the task is not completed, add it to the to-do list.
    if completed == 'no':

        # Check if the task is already in the to-do list.
        if task in todo_list:
            print('You already have this task in your to-do list.')
        else:
            todo_list.append(task)
            print('Task added to your to-do list.')

    # If the task is completed, add it to the completed list.
    elif completed == 'yes':

        # Check if the task is already in the completed list.
        if task in completed_list:
            print('You have already completed this task.')
        else:
            completed_list.append(task)
            print('Task added to your completed list.')

    # If the user enters something other than yes or no.
    else:
        print('Please enter yes or no.')

# Thank the user after they finish entering tasks.
print('Thank you! Here are your tasks:')

# Display all unfinished tasks.
print('\nYour To-Do Tasks:')

# Go through the list and display each task with a number.
for index, task in enumerate(todo_list):
    print(f'Task {index + 1} is {task}')

# Count how many unfinished tasks there are.
print(f'You have {len(todo_list)} tasks to do.')

# Display all completed tasks.
print('\nYour Completed Tasks:')

# Go through the completed list and display each task with a number.
for index, task in enumerate(completed_list):
    print(f'Task {index + 1} is {task}')

# Count how many tasks have been completed.
print(f'You have completed {len(completed_list)} tasks.')
