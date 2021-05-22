# budget
Family Budget App

## Requirements

* Python >= 3.8
* Django >= 3.2
* API via DRF
* Line length = 100
* Language: Eng
* Tests using pytest and django-pytest
* Docker support

## How to Run

1. Clone git repository:

    git clone https://github.com/zybex86/pics.git

1. Run the docker command from the base directory:

    docker-compose up --build

## Login

Create user using the `api/user/create/` endpoint by providing a username and password.

The API is available after authentication. The endpoints include:

`/budgets/`
`/incomes/`
`/expenses/`
`/categories/`
