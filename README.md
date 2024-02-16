# superheroes

## Introduction

This project is a web application that allows users to manage superheroes, their powers, and hero-power associations. Users can perform CRUD (Create, Read, Update, Delete) operations on powers and hero-power associations through a user-friendly interface.

## Features

- Superheroes Management: Users can view a list of superheroes.
- Powers Management: Users can view a list of powers, add new powers, edit existing powers, and delete powers.
- Hero-Power Associations: Users can associate powers with superheroes, view existing associations, and create new associations.

## Technologies Used

# frontend:

- React: JavaScript library for building user interfaces.
- React Router: Declarative routing for React applications.
- HTML/CSS: Markup and styling for the frontend.

# Backend:

- Flask: Micro web framework for building Python web applications.
- Flask-Restful: Extension for building REST APIs with Flask.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- SQLite: Lightweight relational database management system.
Other Tools:
- Git: Version control system for tracking changes in the project.
- Postman: Tool for testing APIs and making HTTP requests.
- VS Code: Integrated development environment (IDE) for writing code.

## Setup Instructions

- Clone the Repository:  git clone <git@github.com:victor-muriuki/superheroes.git>

- Install Dependencies:
Navigate to the project directory: superheroes\python-code-challenge-superheroes\python-code-challenge-superheroes\code-challenge

- Install frontend dependencies:  cd client
                npm install

- Install backend dependencies: cd .. , cd app
    pipenv install flask
    pipenv install flask-migrate
    pipenv install flask-sqlalchemy 
    pipenv install flask-restful
    pipenv install flask-cors

- Run the Application:
    Start the backend server: python3 app.py

- Start the frontend development server: cd frontend
    npm start

- Access the Application:
Open your web browser and go to http://localhost:3000 to access the application.

## API Endpoints

- GET /heroes: Get a list of all superheroes.
- POST /heroes: Create a new superhero.
- GET /heroes/{hero_id}: Get details of a specific superhero.
- PATCH /heroes/{hero_id}: Update details of a specific superhero.
- GET /powers: Get a list of all powers.
- POST /powers: Create a new power.
- GET /powers/{power_id}: Get details of a specific power.
- PATCH /powers/{power_id}: Update details of a specific power.
- GET /hero_powers: Get a list of all hero-power associations.
- POST /hero_powers: Create a new hero-power association.

## License

This project is licensed under the Apache-2.0 license