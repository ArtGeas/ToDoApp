
# ToDoApp
Todo App is a user-friendly web-app that helps you stay organized and manage your tasks effectively. Create an account or log in to access your personalized dashboard. From there, you can easily create tasks, set due dates, and assign priorities.

## Web-app Task Scheduler

__Stack__: Python,Django,Postgres

## Requirements

* Docker version 24.0.2
* PostgreSQL 15.1-alpine
* Django 4.2.2

## Build

```bash
sudo docker-compose up --build
```

## Testing

To run the tests, ensure that you have pytest installed in your virtual environment. If you don't have it, you can install it using:
`pip install pytest pytest-django`

Next, navigate to the root directory of your django project and execute: `pytest`
