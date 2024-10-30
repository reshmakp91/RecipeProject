# Recipe Project

## Description
This project is designed to manage and showcase various recipes. It utilizes Django REST Framework to provide a robust API for recipe management.

## Features
- Add new recipes
- View recipes
- Edit and delete recipes
- RESTful API for integration with frontend applications

## Technologies Used
- Python
- Django
- Django REST Framework
- HTML/CSS
- Bootstrap

## Installation
1. Clone the repository: git clone https://github.com/reshmakp91/RecipeProject.git
2. Navigate into the project directory: cd RecipeProject
3. Install the required packages: pip install -r requirements.txt
4. Run the application:python manage.py runserver
   
## API Endpoints
- http://localhost:8000/create/: Create a new recipe
- http://localhost:8000/detail/<int:pk>/: Retrieve a recipe by ID
- http://localhost:8000/update/<int:pk>/: Update a recipe by ID
- http://localhost:8000/delete/<int:pk>/: Delete a recipe by ID
- http://localhost:8000/search/<str:Name>/: Search for recipes by name

### Additional Views
- http://localhost:8000/: Render the index page

## Usage
You can use tools like Postman or cURL to interact with the API endpoints.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
