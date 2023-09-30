# The Roaming Nomad


![The Roaming Nomad images](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696091635/Porject%204%20Travel%20Blog/am_i_responsive_g8srvw.png)

Welcome to "The Roaming Nomad," your passport to a world of adventure, discovery, and wanderlust. Our travel blog is more than just a website; it's a vibrant and inclusive community where passionate globetrotters come together to celebrate the art of exploration.

At "The Roaming Nomad," we believe that travel is not just a hobby; it's a way of life. Whether you're an intrepid explorer, a seasoned backpacker, or someone with a burning desire to see the world, this is your digital sanctuary.
This is the place where your travel tales come to life. Share your journeys, your escapades, and your most cherished memories from the farthest corners of the Earth. Our platform is a canvas for your stories and a gallery for your photos.
Discover hidden gems tucked away in remote villages, uncover the secrets of bustling metropolises, and find yourself amidst the serene beauty of nature's wonders. "The Roaming Nomad" is your source for travel inspiration, tips, and recommendations that will make your next adventure unforgettable.

Whether you're a solo traveler embarking on a soul-searching expedition or a family seeking new horizons, "The Roaming Nomad" welcomes you with open arms. Connect with fellow wanderers, exchange travel tips, and become a part of our global tribe of explorers.
Your adventure begins here.

Visit the deployed website [here](.....link....).


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Goals](#strategy-goals)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
    4. [Skeleton](#skeleton)
    5. [Surface](#surface)
2. [Features](#features)
    1. [Registration Page](#registration-page)
    2. [Home Page](#home-page)
    3. [Login Page](#login-page)
    4. [Categories Page](#categories-page)
    5. [Edit Categories Page](#edit-categories-page)
    6. [Delete Categories Page](#ask-question-page)
    7. [Create Post Page](#leave-reply-page)
    8. [Edit Post Page](#edit-question-page)
    9. [Delete Post Page](#delete-question-page)
    10. [Edit User Profile Settings Page](#edit-reply-page)
    11. [User Profile Page](#delete-reply-page)
    12. [Edit User Profile Page](#authentication-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](link...)
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)

[Back to top ⇧](#the-roaming-nomad)

## User Experience (UX)
### Strategy
#### Project Goals

* The website contains simple colors for a modern design and also to not draw attention from the content.

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly.

* Site users are able to comment on a post of another user.

* Site users are able to register an account in order to interact with the content.

* Site users are able to personalise their own profile once they register.

* Site users are able to like and dislike a post of another user.

[Back to top ⇧](#the-roaming-nomad)
#### User Goals

* As a Site User, I want register an account so that I can interact with the contents available.

* As a Site User, I want to be able to Login to my own account.

* As a Site User, I want to be able to read full text when I open a post.

* As a Site User, I want to select one post from the list with all posts.

* As a Site User, I want to view a paginated list of posts so that I can easily select a post to view.

* As a Site User, I want to update my profile so that other users can view my profile details.

* As a Site User, I want the information to be readable and easy to find.

* As a Site User, I want to create, edit and delete my own posts.

* As a Site User, I want to manage my contents in my profile.

* As a Site User, I want to be able to upload photos to my posts.

* As a Site User I can leave comments on a post so that I can be involved in the conversation.

* As a Site User I can like or unlike a post so that I can interact with the content.

* As a Site Admin I can register a superuser account so that I can manage and interact with site content.

* As a Site Admin I can create, read, update and delete posts so that I can manage all blog content.

* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

*  As a Site Admin I can create draft posts so that I can finish writing the content later.

* As a Site Admin I can create, read, update and delete categories so that all posts are in order.

* As a User/Admin I can read a post and a comment on an individual post.

* As a User/Admin I can  view the number of likes and dislikes on an individual post.

*  As a Site User/Admin I can view comments on an individual post so that I can read the conversation.

[Back to top ⇧](#the-roaming-nomad)
#### Strategy Goals 

"The Roaming Nomad" strategy revolves around building a platform that fosters a sense of community and celebrates the love of travel. This platform is designed to resonate with:

1. Seasoned Travelers:

    For those who've already journeyed far and wide, "The Roaming Nomad" provides a canvas to reminisce about past adventures and share their invaluable experiences. Also, to reflect on your travel history and offer guidance to those seeking their next great escape.

2. Aspiring Adventurers:

    It extends a warm welcome to those who are yet to embark on their voyages but are filled with wanderlust. "The Roaming Nomad" is a repository of inspiration and practical tips, helping dreamers transform their travel aspirations into meticulously planned itineraries.

3. Wanderlust:

    Beyond those actively planning or recalling trips, our community embraces anyone who simply loves the idea of travel. Even if you're currently grounded, your passion for exploring the world is a treasure, and we encourage you to immerse yourself in the diverse narratives and captivating images shared by our members.

4. Core Values:

 - Inclusivity: "The Roaming Nomad" is a platform that transcends boundaries. We believe that travel knows no age, gender, or background. We embrace diversity and strive to make our community accessible to all.

 - Sharing: At the heart of our strategy is the act of sharing. We encourage members to share their travel stories, from epic adventures to everyday explorations. This collective sharing of experiences enriches our community and inspires others to embark on their journeys.

 - Inspiration and Information: We understand that travel is not just about the destination but the entire journey. Our strategy revolves around providing a wealth of information, including destination guides, travel tips, and cultural insights, to empower and inform our users.

 #### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Account registration | 5 | 5
Ability to fill in user profile | 5 | 5
Create, edit and delete post | 5 | 4
Create, edit and delete categories | 5 | 4
Ability to filter posts by its category | 4 | 5
Add categories to posts | 4 | 5
Likes and dislikes on posts | 4 | 4
**Total** | **37** | **37**

[Back to top ⇧](#the-roaming-nomad)
### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product.

First Phase:

* Create, edit and delete all posts

* Approve/Disapprove comments

* Create draft posts

Second Phase:

* Add pagination to posts

* A list of all posts

* The number of likes/dislikes on a post

Third Phase:

* Create, edit and delete my own posts

Fourth Phase:

* Account registration

* Upload a photo to a post

Fifth Phase:

* Create, edit, and delete all categories

* Filter posts by their category

Sixth Phase:

* Like/Dislike a post

* Fill in User profile

Seventh Phase:

* Create and View comments on a post

[Back to top ⇧](#the-roaming-nomad)

#### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Week 1**
<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 1](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071414/Porject%204%20Travel%20Blog/Iteration_1_qf2lsj.png)

<br>

  ![Iteration 1](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071418/Porject%204%20Travel%20Blog/Iteration1_proefr.png)

<br>

  ![Iteration 1](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071412/Porject%204%20Travel%20Blog/iteratio_1_tdl1cd.png)
</details>

<br>

**Week 2**

<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 2](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071413/Porject%204%20Travel%20Blog/iteratio_2_lglj6r.png)

<br>

  ![Iteration 2](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071413/Porject%204%20Travel%20Blog/iteration_2_btz0c6.png)

<br>

  ![Iteration 2](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071423/Porject%204%20Travel%20Blog/iteration2_p8ukhz.png)
</details>

<br>

**Week 3**

<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 3](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071420/Porject%204%20Travel%20Blog/iteration3_wsbi1v.png)

<br>

</details>

<br>

**Week 4**

<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 4](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071420/Porject%204%20Travel%20Blog/iteraton_4_jtxxr4.png)

<br>

  ![Iteration 4](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071418/Porject%204%20Travel%20Blog/iteration_4_fjdf2b.png)

<br>

</details>

<br>

**Week 5**

<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 5](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071413/Porject%204%20Travel%20Blog/Iteration_5_fgpzt9.png)

<br>

  ![Iteration 5](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071412/Porject%204%20Travel%20Blog/itaration_5_ys0zcs.png)

<br>

</details>

<br>

**Week 6**

<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 6](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071420/Porject%204%20Travel%20Blog/iteration_6_yhc8tf.png)

<br>

  ![Iteration 6](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071413/Porject%204%20Travel%20Blog/iteratio6_hcl1dk.png)

<br>

</details>

<br>

**Week 7**

<details>
    <summary>Click to View</summary>
<br>

  ![Iteration 7](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696071420/Porject%204%20Travel%20Blog/iteration_7_lieufd.png)

<br>

</details>

<br>

**Finish**

<details>
    <summary>Click to View</summary>
<br>

  ![Finished Kanban Board](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696072852/Porject%204%20Travel%20Blog/kanban_board_t0zvau.png)

<br>

</details>

<br>

[Back to top ⇧](#the-roaming-nomad)
### Structure

<br>

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively.

* Header, footer and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* The opportunity to add additional content to the website is provided for the site user once they register an account.

* A 404-error page is available.

* A 403-error page is available.

* A 500-error page is available.

<br>

[Back to top ⇧](#the-roaming-nomad)
#### Database Model

The type of database being used for the is relational database being managed using [PostgreSQL](https://www.postgresql.org/).

![Plan ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696073828/Porject%204%20Travel%20Blog/models_icfdxo.png)

<br>

[Back to top ⇧](#the-roaming-nomad)
### Skeleton
#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Index/ Logged out | ![Desktop index wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075864/Porject%204%20Travel%20Blog/home_page_wkkav4.png) | ![Mobile index wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075863/Porject%204%20Travel%20Blog/home_page_1_wsxbeh.png)
Sign Up | ![Desktop sign up wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075860/Porject%204%20Travel%20Blog/register_wyyimq.png) | ![Mobile sign up wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075860/Porject%204%20Travel%20Blog/resgiter1_u1mee6.png)
Log In | ![Desktop log in wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075865/Porject%204%20Travel%20Blog/login_dpx5va.png) | ![Mobile log in wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075865/Porject%204%20Travel%20Blog/login1_lxulzf.png)
Index / User Logged In | ![Desktop index / user logged in wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075864/Porject%204%20Travel%20Blog/logged_in_wswc8t.png) | ![Mobile index / user logged out wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075864/Porject%204%20Travel%20Blog/logged_in_1_dqgjhk.png)
Create Post | ![Desktop create post wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075861/Porject%204%20Travel%20Blog/create_post_bfci9l.png) | ![Mobile create post wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075861/Porject%204%20Travel%20Blog/create_post1_vtksjc.png)
Edit Post | ![Desktop edit post wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075862/Porject%204%20Travel%20Blog/edit_post_vvaid6.png) | ![Mobile edit post wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075863/Porject%204%20Travel%20Blog/edit_post_1_pl8mu6.png)
Delete Post | ![Desktop delete post wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075861/Porject%204%20Travel%20Blog/delete_post_e0eygt.png) | ![Mobile delete post wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075862/Porject%204%20Travel%20Blog/delete_post1_uzal9m.png)
User Profile | ![Desktop User Profile wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075860/Porject%204%20Travel%20Blog/Profile_Page_xjkrlw.png) | ![Mobile User Profile wireframe image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696075860/Porject%204%20Travel%20Blog/profile_page_1_tsxloj.png)

[Back to top ⇧](#the-roaming-nomad)
### Surface

#### Color Scheme


The colors used in the website are ... for secondary buttons, navbar links, as well as for main buttons and links transitions. ..... is used for the main text, footer background, main buttons and secondary buttons and links transitions.

..... for the navigation bar and card footers background, footer and buttons content. ...... is also used in the main background and cards footer as well as for input fields.

The colors were chosen keeping in mind simplicity but also providing the website a modern design. This in order to keep the focus on the content but also appealing for the users.


#### Typography

The main font being used in the site is ..., with sans-serif as a fallback in case .... doesn't get imported correctly. Roboto, with sans-serif as a fallback is used mainly for headings.

Nunito and Roboto were chosen after some research on fonts that are better for reading. Specially Nunito which has been used as main font. Quicksand was used for the logo for design purposes.

[Back to top ⇧](#the-roaming-nomad)

## Features

### General

........
[Back to top ⇧](#the-roaming-nomad)
### Home Page

.....

[Back to top ⇧](#the-roaming-nomad)

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

[Back to top ⇧](#the-roaming-nomad)
### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.

* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com)  
    * Google fonts was used to import the fonts into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 

* [jQuery 3.6.0](https://jquery.com/)  
    * jQuery was used as a JavaScript library to help writing less JavaScript code.  

[Back to top ⇧](#the-roaming-nomad)
### Packages / Dependecies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

[Back to top ⇧](#the-roaming-nomad)
### Database Management
* [Heroku Postgres](https://www.heroku.com/postgres)   
    * Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.

[Back to top ⇧](#the-roaming-nomad)

### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
   * GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Am I Responsive](ami.responsivedesign.is)  
    * Am I Responsive was used to preview the website across a variety of popular devices.

* [Balsamiq](https://balsamiq.com/)
     * Balsamiq was used to create the wireframes during the design phase of the project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Favicon.cc](https://www.favicon.cc/) 
    * Favicon.cc was used to create the site favicon.

[Back to top ⇧](#the-roaming-nomad)

## Testing

The testing documentation can be found [here](https://github.com/Delfinistkata/the-roaming-nomad/blob/d5dcbfdd4db4d4e7e22343b45443c6d109bdb13c/TESTING.md).

[Back to top ⇧](#the-roaming-nomad)

## Deployment

This project was developed using a [GitPod](https://gitpod.io/) workspace. The code was commited to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    * In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    * In your GitPod workspace, create an env.py file in the main directory. 
    * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    * Add the SECRET_KEY value to the Config Vars in Heroku.
    * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    * Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    * In settings.py add the following sections:
        * Cloudinary to the INSTALLED_APPS list
        * STATICFILE_STORAGE
        * STATICFILES_DIRS
        * STATIC_ROOT
        * MEDIA_URL
        * DEFAULT_FILE_STORAGE
        * TEMPLATES_DIR
        * Update DIRS in TEMPLATES with TEMPLATES_DIR
        * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

[Back to top ⇧](#the-roaming-nomad)

### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/Delfinistkata/the-roaming-nomad).
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

[Back to top ⇧](#the-roaming-nomad)

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/Delfinistkata/the-roaming-nomad).
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/Delfinistkata/the-roaming-nomad).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.

    ```
    git clone https://github.com/Delfinistkata/the-roaming-nomad
    ```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

[Back to top ⇧](#the-roaming-nomad)

## Finished Product

.......

[Back to top ⇧](#the-roaming-nomad)

## Credits

Throughout the building process I found many helpful tutorials online.
I sometimes applied principles within them to the site, after fully understanding their code and modifying to fit the site's needs.

<br>

### Content

* Website content was written by the developer.
* 

[Back to top ⇧](#the-roaming-nomad)
### Media

* [Pexels](https://www.pexels.com/)

    * 

* [Unsplash](https://unsplash.com/)

    * 
[Back to top ⇧](#the-roaming-nomad)
### Code

[W3Schools](https://www.w3schools.com/) - was consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - This repository was created using the template provided by Code Institute.

[Django Documentation](https://docs.djangoproject.com/en/4.0/) - Django step-by-step document to ensure everything is set up correctly. 

[Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/faq.html) - referenced during development.

[Cloudinary Documentation](https://cloudinary.com) - referenced during development.

[Summernote Documentation](https://summernote.org/) and [Git](https://github.com/summernote/django-summernote) - referenced during development.

[Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/) - referenced during development.

[John Elder - Django](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy) - YouTube series that help me through project.

[Stackoverflow](https://stackoverflow.com/) -Used to search issues I had.

[Slack](https://slack.com/intl/en-ie/) - I used Slack when I had issues.

<br>

[Back to top ⇧](#the-roaming-nomad)

## Known Bugs

..............

[Back to top ⇧](#the-roaming-nomad)

## Acknowledgements

<hr>
<br>

This project was developed and designed as a Portfolio 4 Project for Full Stack Software Developer Diploma course at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor Marcel Mulders for his invaluable feedback and guidance, our facilitator Chris Quinn, the Slack community, and all at the Code Institute for their help and support. I really enjoyed working on this project.

<br>
<br>

[Back to top ⇧](#the-roaming-nomad)