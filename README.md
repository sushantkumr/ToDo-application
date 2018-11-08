# ToDo-application
Task generator and reminder application using Django

A simple app to create tasks with due dates and alerts.

### To install the app:
* Clone the repo
* Run `pip3 install -r requirements.txt` inside the repo root
* Run the following commands
	` python3 manage.py makemigrations
	  python3 manage.py migrate`
* To start the server, run `python3 manage.py runserver`

### Directions to use the app
* Home page displays the tasks created by the user.
* To create a new task, click on `New Task`
* Enter the details. Title, Due date and alert time are mandatory.
* If task is created successfully then user will be redirected to home page
* To view the task details click on the task card
* Options available in the task details page are to
	* Delete the task
	* Toggle task status between `Complete` and `Pending`
	* Create sub tasks for the task
* To search for tasks based on `title` enter the title in the search bar in the Home page
* To search for tasks based on `period` select the period from the dropdown in the Home page