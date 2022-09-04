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

#### Key features of the API:
1. There are two roles in the app- user and superuser
2. Token based authentication is used for accessing authenticated endpoints.
3. Users can apply for loan and check status of the loan.
4. Super users can check the loan applications and change status as per the application.





