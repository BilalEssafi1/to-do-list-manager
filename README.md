# To-Do List Manager
[View the live project here](https://to-do-list-manager-8ccfde7e2228.herokuapp.com/)

The To-Do List Manager is a simple command-line based To-Do List application written in Python that helps you manage your tasks efficiently. This program allows you to add, remove, mark tasks as done, and view your task list.

![Responsive Design](images/responsive-design.png)

## Target Audience

The tool is designed for individuals, students, and professionals who need a simple yet effective way to manage their personal and work-related tasks. 

## Use Case
A student uses this to-do list manager to keep track of assignments and exam preparations. The tool allows them to add tasks and mark them as complete once they have finalized them, ensuring that no important coursework is overlooked. Additionally, it helps them manage personal commitments and extracurricular activities, ensuring they stay organized and maintain a balanced schedule throughout the semester.

## Rules of the Application

The To-Do-List Manager operates on a straightforward premise:
1. Users can add tasks to a list, each represented with description and a completion status (Pending or Done)
2. Tasks can be removed from the list by selecting their corresponding index. 
3. Users can mark tasks as complete, updating their status. 
The application continuously prompts users until they choose to exit. 

## Features
- Initial instructions: When starting the application, users receive clear instructions on how to interact with the system.
- Add Task: Users can input task descriptions to add them to their to-do list.
- Remove Task: The current list of tasks is displayed, allowing users to choose which task to remove. 
- Mark Task as Done: Users can mark specific tasks as completed. 
- Show All Tasks: View all tasks along with their current status. 
-Exit Option: Users can easily exit the application when easily when finished. 

## How to use the To-Do List Manager

1. Interact with the Menu:
- A menu will display options for managing your tasks

![Features](images/features.png)

2. Choose an Option
- Enter the number corresponding to your desired action, such as adding or removing tasks. 

![Input](images/add-task.png)

3. Error Handling
- The application includes input validation, providing error messages for invalid selections or actions to ensure a smooth user experience.

![Error](images/error.png)

## Testing

I have tested my Python code through various means:

- PEP8 Validation: The code was validated using PEP8 style guide without any errors. 

![Validation](images/validation.png)

- Manual Testing of Functions: Inputs were tested against expected outputs to confirm functionality. Please refer to the[TESTING.md](TESTING.md) file for all testing carried out. 

- Gameplay Testing: The application was run with both normal and edge case inputs to ensure it handles errors appropriately.

## Bugs
## Solved Bugs

- Indexing Error when Removing Tasks: Initially, when attempting to remove tasks from the to-do list, I mistakenly deleted the wrong items because I had overlooked that lists in Python are zero-indexed. To fix this, I adjusted the indexing by adding -1 where necessary, ensuring that the correct tasks are removed or marked as done.
- Empty Task Submissions: While testing the "Add Task" functionality, I discovered that the application accepted empty submissions. I addressed this by using the strip() method to check for empty spaces. Now, an error message is displayed when a user attempts to add an empty task.
- Task Description Length Validation: During testing, I found that the application did not enforce a maximum character limit for task descriptions, allowing users to input excessively long texts. To resolve this issue, I implemented a character limit validation, ensuring that task descriptions do not exceed 80 characters. If a user attempts to enter a longer description, an error message is now displayed, prompting them to revise their input. 

## Known Bugs
Invalid Input Handling for Task Number: During testing, I found that the application correctly handles invalid task numbers when removing or marking tasks as done. However, there's a minor issue: after showing the error message for an invalid task number, the user is automatically navigated back to the main menu instead of being allowed to retry entering a valid number. This prevents users from immediately correcting their input without returning to the main menu. While this bug is not critical, it slightly affects the user flow.

## Technologies Used
Python
PEP8 validator

## Development Tools
### Am I Responsive
- [Am I Responsive](https://ui.dev/amiresponsive) was used to see how the command line application looks on different screen sizes.
### GitPod
- [GitPod](https://www.gitpod.io/) was used to write the code for this application and to commit and push the code to Github.
### GitHub
- [GitHub](https://github.com/) was used to store this application.
### Heroku
- [Heroku](https://www.heroku.com) was used to deploy the application. 

## Deployment
The application was developed using [GitPod](https://www.gitpod.io/) and pushed to GitHub through a GitPod terminal. This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    1. Login to [Heroku](https://www.heroku.com)
    2. Create a new Heroku app:
    - Click on "New" in the top-right corner and select "Create new app."
    - Provide a unique app name.
    - Select the appropriate region.
    - Click on "Create app."
    3. Navigate to the Settings tab:
    - Under "Buildpacks," click "Add buildpack" and select Python, then NodeJS (in that order).
    4. Navigate to the Deploy tab:
    - Under "Deployment method," choose GitHub.
    - Search for the appropriate repository and click "Connect" to link the Heroku app to the repository.

- How to Fork this Project:
    1. Login to [GitHub](https://github.com/).
    2. Navigate to the repository: https://github.com/BilalEssafi1/to-do-list-manager.
    3. Click on the Fork button in the top-right corner.  
    4. Select Create a new fork.

- How to Clone this Project:
    1. Login to [GitHub](https://github.com/).
    2. Go to the repository: Login to https://github.com/BilalEssafi1/to-do-list-manager.
    3. Click the green Code button.
    4. Under the Clone section, choose the method to clone the repository (HTTPS, SSH, or GitHub CLI).
    5. Open the terminal in your code editor
    - Use the cd command to navigate to the directory where you want to clone the repository.
    6. Run the git clone command followed by the repository URL you copied, and press Enter. 


## Credits
- Code Institute for the deployment terminal and the [Python template](https://github.com/Code-Institute-Org/p3-template).
- The code and idea of the to-do list manager came originally from [Projects Explained](https://www.youtube.com/watch?v=bfHAeWZ7oAY). In addition, the code to check for empty spaces came from [w3school](https://www.w3schools.com/python/ref_string_strip.asp) and the code to limit the characters came from [stackoverflow](https://stackoverflow.com/questions/28465779/how-do-i-limit-the-amount-of-letters-in-a-string)  However, all the code has been modified to suit the specific needs of this application and it is no longer in its original form.
