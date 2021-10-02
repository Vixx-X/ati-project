# Ati Project

Information to understand challenges of ITA course

## Table of contents

- [Challenge 27](#lab-27)
- [Challenge 38](#lab-38)

## Challenge 27 <a name="lab-27"></a>

We have two Workflows. First with pull request to develop branch and the second one that comes from any merge to master.

In the first, the branches are created from develop, the dependencies associated with yarn and python pip are installed and then when we done work on the branch, run_pylint and run_pytest are execute and the branch is pushed to the remote repository and then create pull request.

In the second it is quite similar but with the difference that in the end it ends up performing a content deployment.

File of Workflow can be found [here](/.github/workflows/dev.yaml)

## Lab 37

  For the lab we have to use Flask (like Flask-Login y flask-wtf), we can see the use of:
  - FlaskUser [here](/src/backend/user_manager.py)
  - FlaskForm [here](/src/backend/apps/user/forms.py)

## Challenge 38 <a name="lab-38"></a>

- For the User manage we use the Users from Flask and adding new features, this implementation can be found [here](/src/backend/user_manager.py).
- The models for User in the Data base can be view [here](/src/backend/apps/user/models.py).
- For the form manage we use FlaskWTForms, this can be found [here](/src/backend/apps/user/forms.py).
- FlaskUser, FlaskLogIn were used for the User Log In and the Session Management.
