# Manuel testing

| Test Case #| Scenario | Input | Expected Output | Actual Output|Pass/Fail |
| --- | --- | --- | --- | --- | --- |
| 1 | Valid option selection | Choose an option (1-5): 1 | Question: "Enter the task description" | Question: "Enter the task description" | Pass |
| 2 | Invalid option selection | Choose and option(1-5): cat| Error message: "Invalid option. Please choose a number between 1 and 5" | Error message: "Invalid option. Please choose a number between 1 and 5" | Pass |
| 3 | Empty option selection | Choose and option(1-5): "" | Error message: "Invalid option. Please choose a number between 1 and 5" | Error message: "Invalid option. Please choose a number between 1 and 5" | Pass |
| 4 | Valid task addition| Enter the task description: "Go grocery shopping" | Task added successfully: "Go grocery shopping" | Task added successfully: "Go grocery shopping"| Pass |
| 5 | Empty task input| Enter the task description: "" | Error message: "Task description can't be empty. Please try again!" | Error message: "Task description can't be empty. Please try again!"| Pass |
| 6 | Large task input string (exceeding. character limit of 80) | Enter the task description:"I am creating a very long string that serves the purpose of testing whether or not it gets rejected by the character limit constraints." |Error message:"Description limit is 80 characters. Please retry"| Error message:"Description limit is 80 characters. Please retry"| Pass |
| 7 | Empty remove input| Enter the task number to remove: 1 | Task "Go grocery shopping" removed successfully!| Task "Go grocery shopping" removed successfully!| Pass |
| 8 | Invalid remove input| Enter the task number to remove: cat | Error message: "Please enter a valid number."| Error message: "Please enter a valid number."| Pass |
| 9 | Valid mark as done input| Enter the task number to mark as done: 1 | Task "Go grocery shopping" marked as completed!| Task "Go grocery shopping" marked as completed!| Pass |
| 10 | Invalid mark as done input| Enter task number to mark as done: cat | Error message: "Please enter a valid number."| Error message: "Please enter a valid number."| Pass |
| 11 | Valid option selection for "4. Show all tasks" | Choose option (1-5): 4| Your to do list: 1. Go Grocery Shopping - Pending| Your to do list: 1. Go Grocery Shopping - Pending | Pass |
| 12 | Valid option selection for "5. Exit" | Choose option (1-5): 5| Exiting the to-do list| Exiting the to-do list | Pass |



