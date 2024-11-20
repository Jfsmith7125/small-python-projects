# Initialize the to-do list
todos = []

print("My ToDos")

# Start prompting for tasks
while True:
    task = input("Enter a task (or type 'exit' to quit): ")

    # Exit the loop if the user types 'exit'
    if task.lower() == "exit":
        break

    # Add the task to the to-do list
    todos.append(task)

    # Ask if the user wants to display the list
    display = input("Do you want to display your todos? (yes/no): ")

    # Display the to-do list with numerals if the user says 'yes'
    if display.lower() == "yes":
        print("My ToDos:")
        for index, todo in enumerate(todos, 1):  # Start enumeration from 1
            print(f"{index}. {todo}")

print("Goodbye!")
