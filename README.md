# django-rest-api
A REST api written in Django

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ gh repo clone haridharushanSV/SRMS-Connect-Backend
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd srmsconnect
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python -m venv env
            $ env\Scripts\activate
        ```
   
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/
    ```
![image](https://github.com/user-attachments/assets/4252a34d-3f08-4d6e-86c3-995c46cbe2f8)
