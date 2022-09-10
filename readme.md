# Django-userauthenticaion-CRUD-RESTAPI

Basic create, read, update and delete for bookdetails and total is here with super cool User Interface. MongoDB, inbulit sqlite3 database is used to store data.
A Restful web service for accessing the book details is created

<!-- ## Run application in docker container
1. Install Docker Desktop [here](https://www.docker.com/get-started)
2. Go to the project root folder and run the following commands  
    - `docker-compose build`
    - `docker-compose up`
3. Go to [127.0.0.1:8000](http://127.0.0.1:8000) to view the output -->

## Dependencies
- Django `pip install django`  
- Django `pip install django` 
-  
-  
- Django Rest Framework `pip install djangorestfamework`  
-  Django Rest Framework `pip install djangorestfameworksimplejwt`
- 

## Start the MongoDB server
First we need to create Bookapi folder in which create a virtual environment 'venv' install django dependencies and in settings.py file import following as seen below
<img src="C:/Users/VIVEK/Bookapi/images/image1" width=360 /><br> and import REST_FRAMEWORK AND SIMPLE_JWT in settings.py file as seen below
<img src="C:/Users/VIVEK/Bookapi/images/image2"/>
<img src="C:/Users/VIVEK/Bookapi/images/image3"/>
<img src="C:/Users/VIVEK/Bookapi/images/image4"/>



## Run
Go to the project directory and run `python manage.py runserver`

## Access REST API
` ` retrieves all bookdetails
`/bookcreate/` to create new book details 
`/book/<id>/` to retrive,update and delete a specific book 
`/registration/` to register new user in api for authentication
`/api/token` to obtain new token 
`/api/token/refresh/` to refresh new token 

## Screenshots 
<img src="C:/Users/VIVEK/Bookapi/images/image5"/> to retrive,delete and update bookdetail 
<img src="C:/Users/VIVEK/Bookapi/images/image6"/> to register new user 






