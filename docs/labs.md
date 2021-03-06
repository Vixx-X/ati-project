# Ati Project

Information to understand challenges of ITA course

## Table of contents

- [Lab 27](#lab-27)
- [Challenge 31](#lab-31)
- [Lab 32](#lab-32)
- [Lab 34](#lab-34)
- [Lab 37](#lab-37)
- [Challenge 38](#lab-38)
- [Lab 40](#lab-40)
- [Challenge 41](#lab-41)
- [Challenge 42](#lab-42)
- [Lab 43](#lab-43)

## Lab 27 <a name="lab-27"></a>

We have two Workflows. First with pull request to develop branch and the second one that comes from any merge to master.

In the first, the branches are created from develop, the dependencies associated with yarn and python pip are installed and then when we done work on the branch, run_pylint and run_pytest are execute and the branch is pushed to the remote repository and then create pull request.

In the second it is quite similar but with the difference that in the end it ends up performing a content deployment.

File of Workflow can be found [here](/.github/workflows/dev.yaml)

## Challenge 31 <a name="lab-31"></a>

The html files are divided into two sections, one for components and the other for templates that can be found [here](/src/templates)

For its part, both the Javascript and Css files are located in this [link](/src/frontend/static_src), dividing internally also with a section for views and another for components

Both javascript and CSS components are imported [here](/src/templates/user/auth/base.html)

To see all the views and components live and which person did each one, enter the following [link](https://ati.vittorioadesso.com/showroom/)

## Lab 32 <a name="lab-32"></a>

  - In this lab, what was mentioned in challenge 21 was used. Our design not only required one "Base.html" template because some views have modifications in the header and footer (colors, mobile and desktop version, etc). But these "bases" were extended from others bases. Main Base.html template can found [here](/src/templates/user/auth/base.html). This was used for the basis of all auth views. Another one can be found [here](/src/templates/base.html). Most of the other views extend from this template. By the other hand, the base template that refers to the profile pages and their related ones are found [here](/src/templates/user/base.html). All the other html templates are located [here](/src/templates) from all bases templates mentioned above.
  
  - All the other html templates are located [here](/src/templates) from bases templates mentioned above.
  
  - Each of the main modules of the application has its own routes file associated with it, and this is associated with its controller (which are defined in the views.py and utils.py files)
    - For the templates of Chat, we have [routes](/src/backend/apps/chat/urls.py) and [controller](/src/backend/apps/chat)
    - For the templates of Media, we have [routes](/src/backend/apps/media/urls.py) and [controller](/src/backend/apps/media)
    - For the templates of Post, we have [routes](/src/backend/apps/posts/urls.py) and [controller](/src/backend/apps/posts)
    - For the templates of User, we have [routes](/src/backend/apps/user/urls.py) and [controller](/src/backend/apps/user)
    
  - With internationalization, we use Flask-Babel. First, the translations are generated by scanning translatable strings of the files as in the case like [this file](https://docs.ati.vittorioadesso.com/_modules/backend.html#init_app). It's important to note that all HTML files are kept with the corresponding string translation format. Then files with extension .po are generated in [this directory](/src/translations) with the available languages, for now Spanish (es) and English (en)

## Lab 34 <a name="lab-34"></a>

We make capture of mongo when we had the images (after flask-load) and we uploaded it to Docker hub. This link can be found [here](https://hub.docker.com/repository/docker/danielviei/mongo_with_images). However, we decided not to save the images but rather to save the data in the server's filesystem so as not to have to send static content.

By the other hand, instead of using that image, could use same data through loaddata command, executing it in this way:
```bash
FLASK_APP=$(pwd)/src/wsgi.py FLASK_ENV=development flask loaddata fixtures
```

## Lab 37 <a name="lab-37"></a>
  
  We had to implement the funcionality of the authentication, this functionality was implemented in the respective forms modules
  - To find user module, click [here](https://docs.ati.vittorioadesso.com/backend.apps.user.html). In this documentation we can find form implementation that we use in our app.
  - To find user manager, click [here](https://docs.ati.vittorioadesso.com/config.html). 

We can config User URL like show [this file](https://docs.ati.vittorioadesso.com/backend.html?highlight=user_mana#module-backend.user_manager).

Some URLs are modified through the config file and by the other hand, forms are overwritten through User Manager

## Challenge 38 <a name="lab-38"></a>

  - In user manager, the forms that Flask User has inside, are overwritten and we choose user model that we developed. This implementation is located [here](/src/backend/user_manager.py).
  - Models of User in the Data Base can be view [here](/src/backend/apps/user/models.py).
  - For handling forms we use FlaskWTForms. Information about implementation of this functionality is located [here](/src/backend/apps/user/forms.py).
  - FlaskUser, FlaskLogIn were used for the User Log In In and Session Management.

  In this case, all team work over all mentioned functionalities.

## Lab 40 <a name="lab-40"></a>

For this challenge we have to implemet the button for the login in the social medias [Facebook and Twitter](https://docs.ati.vittorioadesso.com/backend.html?highlight=backend%20blueprints#module-backend.blueprints)

We use Python Social Auth in implementation of authentication. To view more documentation about this library click [here](https://python-social-auth.readthedocs.io/en/latest/)

## Challenge 41 <a name="lab-41"></a>

The function we consider the most important for Unit Test are:

- Forgot Password
- Customize the Page
- Sing up and Log in
- User Profile
- Responsive Design

All unit tests were performed by all team together.
We can find these tests inside [this directory](/src/tests)

## Challenge 42 <a name="lab-42"></a>

Test Matrix can be found [here](https://docs.google.com/spreadsheets/d/1Ermx7M64E05hreIxlhLd61TE2-j0jpRK/edit#gid=1492136221). 

## Lab 43 <a name="lab-43"></a>

We have to implement the interface test and run it [here](https://docs.ati.vittorioadesso.com/tests.html?highlight=selenium#module-tests.test_selenium). We can see its documentation.
