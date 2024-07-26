# BuzzerBoy Lab 2

In this lab, you demonstrate your ability to work with existing starter kits. 

<br>

# Quick start

> 👉 Download the code  

```bash
$ git clone https://github.com/alibacelonia/buzzerboy-lab2.git
$ cd buzzerboy-lab2
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ python3 -m  venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

# Tasks

* [Task 1](submission-lab2/Lab2-task1.md) - Clone any free starter kit from [Creative Tim](https://www.creative-tim.com).
* [Task 2](submission-lab2/Lab2-task2.md) - Setup that starter kit and make it run on your local server.
* [Task 3](submission-lab2/Lab2-task3.md) - In this starter kit, create **any two** of the following features:
  * Create a section for team, and ability for users to invite other users to this team. 
  * ✅ Create a small Project management LCRUD (list, create, read, update and delete) user interface.
  * Create a small Restaurant management LCRUD (list, create, read, update and delete) user interface.
  * ✅ Create a small Country management LCRUD (list, create, read, update and delete) user interface.
* [Task 4](submission-lab2/Lab2-task4.md) - Setup Django admin for Task 3 and the ability to add foreign key models from the parent model.
* [Task 5](submission-lab2/Lab2-task5.md) - Add an Owner field, and Owner Email Address in your Task 3, and make sure there is an email address field.
* [Task 6](submission-lab2/Lab2-task6.md) - Create validations for fields of your choosing in Task 3. There should be validations should be for email,
non-empty, and numeric.

