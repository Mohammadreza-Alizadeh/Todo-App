# Todo-App

This is a simple Todo app built with Django and Bootstrap 5. It allows users to create tasks, set priorities, update tasks, and mark tasks as completed.

## Installation

To run the app, follow these steps:

1- Clone the repository to your local machine

```bash
  git clone https://github.com/Mohammadreza-Alizadeh/Todo-App.git
```

2- Create the database tables:
```bash
  python manage.py migrate
```

3- Run the server:
```bash
  python manage.py runserver
```

4- Open the app in your browser at `http://localhost:8000`


## Usage

### Creating a User
To create a user, click on the "Sign Up" link on login form and fill out the registration form.
Be aware that to create a new account, you must log out first.

### Logging In and Logging Out
To log out of the app, you can click on the logout button on the home page. By doing this, you will be redirected to the login form
and you can use that form to login again


### Adding a Task
To add a task, click on the "Add Task" button on the home page and fill out the task form. You can set a priority for the task by selecting a priority level from the drop-down menu.

### Viewing Task Details
To view the details of a task, click on the `details` button of any task on the home page. This will open a window containing the details of the task

### Updating a Task
To update a task, click on the "update" button of any task and update the task form.

### Marking a Task as Completed
To mark a task as completed, click on little blue button of any  . This will change the status of the task to "Completed" and draws a line on the name of the task.

## Credits
This app was built with Django and Bootstrap 5.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
