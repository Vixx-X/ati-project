# Ati Project

Information to understand challenges of ITA course

## Table of contents

- [Challenge 27](#lab-27)
- [Challenge 31](#lab-31)
- [Lab 32](#lab-32)
- [Lab 37](#lab-37)
- [Challenge 38](#lab-38)

## Challenge 27 <a name="lab-27"></a>

We have two Workflows. First with pull request to develop branch and the second one that comes from any merge to master.

In the first, the branches are created from develop, the dependencies associated with yarn and python pip are installed and then when we done work on the branch, run_pylint and run_pytest are execute and the branch is pushed to the remote repository and then create pull request.

In the second it is quite similar but with the difference that in the end it ends up performing a content deployment.

File of Workflow can be found [here](/.github/workflows/dev.yaml)

## Challenge 31 <a name="lab-31"></a>

The html files are divided into two sections, one for components and the other for templates that can be found [here](src/templates)

For its part, both the Javascript and Css files are located in this [link](/src/frontend/static_src), dividing internally also with a section for views and another for components

Both javascript and CSS components are imported [here](/src/templates/user/auth/base.html)

To see all the views and components live and which person did each one, enter the following [link](https://ati.vittorioadesso.com/showroom/)

## Lab 32 <a name="lab-32"></a>
  - In this Lab we have to use the view from Challenge 31 and define who is gonna be the Base.html [link](https://ati.vittorioadesso.com/showroom/)
  - Build a templates for every page who are extend from  Base.html [link](https://ati.vittorioadesso.com/showroom/)
  - Create routes for the templates created in the previous step [link]
  - - For the templates to Chat [routes](https://docs.ati.vittorioadesso.com/backend.apps.chat.html?highlight=url#module-backend.apps.chat.urls) and [controles](https://docs.ati.vittorioadesso.com/backend.apps.chat.html?highlight=views#module-backend.apps.chat.views)
  - - For the templates to Media [routes](https://docs.ati.vittorioadesso.com/backend.apps.media.html?highlight=url#module-backend.apps.media.urls) and [controles](https://docs.ati.vittorioadesso.com/backend.apps.chat.html?highlight=url#module-backend.apps.media.views)
  - - For the templates to Post [routes](https://docs.ati.vittorioadesso.com/backend.apps.posts.html?highlight=url#module-backend.apps.posts.urls) and [controles](https://docs.ati.vittorioadesso.com/backend.apps.chat.html?highlight=url#module-backend.apps.posts.views)
  - - For the templates to User [routes](https://docs.ati.vittorioadesso.com/backend.apps.user.html?highlight=url#module-backend.apps.user.urls) and [controles](https://docs.ati.vittorioadesso.com/backend.apps.chat.html?highlight=url#module-backend.apps.user.views)
  - For the internasionalization we implement [here](https://docs.ati.vittorioadesso.com/_modules/backend/core.html#init_app)

## Lab 37 <a name="lab-37"></a>
  
  We had to implement the funcionality of the authentication, this functionality was implemented in the respective forms module (User and Post)
  - For the Post module [here](https://docs.ati.vittorioadesso.com/backend.apps.posts.html) Where we can find the form implementation, we are using for the Post in our app.
  - For the User module [here](https://docs.ati.vittorioadesso.com/backend.apps.user.html) Where we can find the form implementation, we are using for the Post in our app.
  - For User manager [here](https://docs.ati.vittorioadesso.com/config.html) where we config the User URL, [here](https://docs.ati.vittorioadesso.com/backend.html?highlight=user_mana#module-backend.user_manager) where we custom the flask_user Manager and configurate custom forms
  

## Challenge 38 <a name="lab-38"></a>

- For the User manage we use the Users from Flask and adding new features, this implementation can be found [here](/src/backend/user_manager.py).
- The models for User in the Data base can be view [here](/src/backend/apps/user/models.py).
- For the form manage we use FlaskWTForms, this can be found [here](/src/backend/apps/user/forms.py).
- FlaskUser, FlaskLogIn were used for the User Log In and the Session Management.
