# Phase-3-Project-TGIF

A one sentence description of your CLI:
TGIF is an app where users take a quiz to reflect on their mood, receiving personalized activity suggestions based on how they feel.

A description / diagram of your database including relationships, constraints, intended CRUD actions. This should not be code. It needs to be something visual:

<img width="890" alt="Screenshot 2024-08-19 at 9 43 06 AM" src="https://github.com/user-attachments/assets/c662f596-a2fb-44fe-8ea4-3d0a5b4c9020">


CRUD: 

![Screenshot 2024-08-18 at 4 43 49 PM](https://github.com/user-attachments/assets/e4950a12-3146-4978-8718-d4ff9294a0a7)

Step 1: Fork the Repository

Go to the Repository: Navigate to the GitHub page of the repository you want to fork.

Fork the Repository: Click the "Fork" button at the top right of the page. This will create a copy of the repository in your GitHub account.

Step 2: Clone the Repository

Open Your Terminal: Use any terminal application of your choice.

Clone the Repository: Copy the URL of the forked repository from your GitHub account and run the following command in the terminal:

git clone <your-forked-repository-URL>

Step 3: Open the Project in VS Code

Navigate to the Project Directory: Change into the directory of your cloned repository by running:

cd <your-repository-name>

Open VS Code: Run the following command to open the project in Visual Studio Code:

code .

Step 4: Install Dependencies

Install pipenv: Ensure you have pipenv installed by running:

pip install pipenv

Install Project Dependencies: Run the following command to install all necessary dependencies for the project:

pipenv install

Step 5: Access the Quiz Game

Activate the Virtual Environment: Enter the pipenv shell by running:

pipenv shell

Navigate to the CLI Folder: Access the cli.py file by navigating to the appropriate directory:

cd lib

Run the Quiz Game: Start the quiz game by running:

python cli.py




A decision tree of the flow of your CLI. Preferably a screenshot of a drawio diagram:

![Screenshot 2024-08-19 at 9 00 37 AM](https://github.com/user-attachments/assets/b4a8249f-6d6f-486d-990c-f0e73d9a2fef)




An example of your data:

![Screenshot 2024-08-18 at 3 58 01 PM](https://github.com/user-attachments/assets/e242387e-b685-4e6e-af0c-7ffa39783740)



Three stretch goals in case you finish your MVP by the due date:

 Colored Text: Enhance the user interface by adding options for users to select or customize text colors.

 Add Emojis: Integrate emoji support to allow users to insert emojis into their content, adding fun and expressiveness.

 Background Styling: Offer background styling options to personalize the look and feel of the application with custom colors, gradients, or images.


A kanban board showing how you will be dividing tasks among partners:

<img width="1452" alt="Screenshot 2024-08-16 at 2 59 04 PM" src="https://github.com/user-attachments/assets/26804f0a-4b71-4114-b275-d58135351fb4">

https://trello.com/b/nfNKEOZm/phase-3-project

