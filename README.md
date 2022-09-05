# Loan Management App

### API endpoints for loan management app.

### Technologies used:
1. Django
2. Django REST framework
3. SQLite

### Steps to run the projects:

**Pre-requites:**
1. python3.8 or greater


**Steps:**


1. Open cmd in your directory and run below commands for initial setup

```sh
mkdir loanApp
cd loanApp
git clone https://github.com/sumedhbhaskar/loan-management-app .
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```
2. Before deploying the local development server, migration is required.

```sh
python manage.py makemigrations
python manage.py migrate
```

3. To run the project, enter below command in cmd

```sh
python manage.py runserver
```

#### Key features of the API:
1. There are two roles in the app- user and superuser
2. Token based authentication is used for accessing authenticated endpoints.
3. Users can apply for loan and check status of the loan.
4. Super users can check the loan applications and change status as per the application.


## Functionality(endpoints)
Endpoint | Functionality| Access
------------ | ------------- | ------------- 
POST /user/register-user | Registers a user | PUBLIC
POST /user/register-admin | Register a super user | PUBLIC
POST /auth-user-token | Create or fetch Token | PUBLIC
POST /loan/loan-type | Create loan category | PRIVATE
GET /loan/loan-type | Lists all loan types | PRIVATE
PUT /loan/loan-type/{id:int} | Update loan category | PRIVATE
POST /loan/loan-apply | Apply for new loan | PRIVATE
PUT /loan/loan-apply/{id:int} | Update loan application | PRIVATE
GET /loan/loan-validate | Lists all loan applications to admins | PRIVATE
PUT /loan/loan-type/{id:int} | Update loan application status | PRIVATE





