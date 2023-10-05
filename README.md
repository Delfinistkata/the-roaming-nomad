# The Roaming Nomad


![The Roaming Nomad image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696458133/Porject%204%20Travel%20Blog/finished%20product%20P4/amiresponsive1_tzprkz.png)

Welcome to "The Roaming Nomad," your passport to a world of adventure, discovery, and wanderlust. Our travel blog is more than just a website; it's a vibrant and inclusive community where passionate globetrotters come together to celebrate the art of exploration.

At "The Roaming Nomad," we believe that travel is not just a hobby; it's a way of life. Whether you're an intrepid explorer, a seasoned backpacker, or someone with a burning desire to see the world, this is your digital sanctuary.
This is the place where your travel tales come to life. Share your journeys, your escapades, and your most cherished memories from the farthest corners of the Earth. Our platform is a canvas for your stories and a gallery for your photos.
Discover hidden gems tucked away in remote villages, uncover the secrets of bustling metropolises, and find yourself amidst the serene beauty of nature's wonders. "The Roaming Nomad" is your source for travel inspiration, tips, and recommendations that will make your next adventure unforgettable.

Whether you're a solo traveler embarking on a soul-searching expedition or a family seeking new horizons, "The Roaming Nomad" welcomes you with open arms. Connect with fellow wanderers, exchange travel tips, and become a part of our global tribe of explorers.
Your adventure begins here.

Visit the deployed website [here](https://the-roaming-nomad-travel-blog-f5d807b27cbd.herokuapp.com/).


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
    1. [General](#general)
    2. [Authentication Pages](#authentication-pages)
    3. [Home Page](#home-page)
    4. [Logged out Page](#logged-out-page)
    5. [Post Detail Page](#post-detail-page)
    6. [Create Post Page](#create-post-page)
    7. [Update Post Modal](#update-post-modal)
    8. [Add Comment Page](#add-comment-page)
    9. [Add Category Page](#add-category-page)
    10. [Edit Category Page](#edit-category-page)
    11. [Delete Category Button](#delete-category-button)
    12. [Category List Page](#category-list-page)
    13. [Category Page](#category-page)
    14. [Edit Settings Page](#edit-settings-page)
    15. [Password Page](#password-page)
    16. [User Profile Page](#user-profile-page)
    17. [Edit User Profile Page](#edit-user-profile-page)
    18. [Modal for User Profile](#modal-for-user-profile)
    19. [Complete User Profile](#complete-user-profile)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/Delfinistkata/the-roaming-nomad/blob/main/TESTING.md)
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
The database model has been designed using [dbdiagram](https://dbdiagram.io/home). The type of database being used for the is relational database being managed using [PostgreSQL](https://www.postgresql.org/).

![website map](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696458644/Porject%204%20Travel%20Blog/finished%20product%20P4/database_diagram_srryvs.png)

<br>
<br>

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


The color scheme used in the website is designed to create a clean and modern design that aligns with the website's travel blog theme. The color choices are as follows:

Primary Color (Bootstrap Primary): This color is used for all buttons throughout the website, providing a consistent and visually appealing look for interactive elements.

Secondary Color (Bootstrap Secondary): Similar to the primary color, the secondary color is also used for buttons, contributing to the website's visual coherence.

Footer Color: The footer is styled in black, creating a distinct separation between the main content and the footer area.

Warning Messages: To draw attention to warning messages and alerts, a vivid red color is employed. This color choice effectively signals important information to users.

#### Typography

The website uses the default system fonts with a fallback to "sans-serif" and "Arial." This approach allows the website to adapt to the user's system font settings while ensuring readability and compatibility. "Sans-serif" is a generic sans-serif font family, and "Arial" serves as an additional fallback option to provide consistency in case "sans-serif" is not available.

[Back to top ⇧](#the-roaming-nomad)

## Features

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.

* Navigation Bar
![Navigation Bar image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400357/Porject%204%20Travel%20Blog/header_for_admin_uju6at.png)

    *  Contains the main logo and section links.

    * The navigation bar contains links to all sections to facilitate navigation across the site. It also has a hover effect that changes color to provide feedback to the Site User for a better user experience.

    * The user will does not have the 'add category' option on their navigation bar. This is only available for the admin.

* Footer
  ![Footer image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400356/Porject%204%20Travel%20Blog/footer_qfkytp.png)

    * The footer includes link to social media channels.

<br>

[Back to top ⇧](#the-roaming-nomad)

### Authentication Pages

Page | Purpose | Image |
--- | --- | --- |
Register | Allow the Site User to sign up an account for the website. | ![Sign Up Page](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400359/Porject%204%20Travel%20Blog/sign_up_jstu6h.png) |
Login | Allow the Site User to sign in with their account. | ![Sign In Page](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400358/Porject%204%20Travel%20Blog/log_in_page_loffzk.png) |
Logout | Allow the Site User to sign out from their account. | ![Sign Out Page](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400358/Porject%204%20Travel%20Blog/home_page-logged_out_do2h0p.png) |

[Back to top ⇧](#the-roaming-nomad)

<br>

### Home Page

* Post list
![Post List image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400357/Porject%204%20Travel%20Blog/home_page_logged_in_u7y5ct.png)

    * Display a paginated list of all the posts and its relevant information for the user to identify.

    * Provide the Site User with a link to the detailed question.

    * Post likes/dislikes as well as voting possibilities for registered users is provided next to the post.

    * For users who has filled in their profile page, an add post link is provided to allow the user to access the page to create new post. If they haven't filled in their profile, they won't be able to create posts.

    * Comment button is provided, once its clicked all comments show under the post, along with the name of the user, the time it was commented at and the comment itself.

    * Filter for posts by a category is provided to users to make their search easier.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Logged out Page

![Logged out Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400358/Porject%204%20Travel%20Blog/home_page-logged_out_do2h0p.png)

* Provide relevant information about the website's objective.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Post Detail Page
![Post Detail Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400358/Porject%204%20Travel%20Blog/post_detail_page_y9gebv.png)

* Display the full post as well as a list of its comments.

* Comments, likes/dislikes scores as well as voting possibilities for registered users is provided.

* Edit, delete and back buttons are provided for the user for their own posts. A back button is only availabe when the user is looking at another user's post.

<br>

![Delete button image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400355/Porject%204%20Travel%20Blog/delete_post_pop_up_eg7ga2.png)

<br>

![Edit button image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400352/Porject%204%20Travel%20Blog/update_post_pop_up_vfrlv6.png)

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Create Post Page
![Create Post Page](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400354/Porject%204%20Travel%20Blog/create_post_page_oktucn.png)

* Provide a form to allow registered Site Users to create a new post.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Update Post Modal
![Update modal](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400352/Porject%204%20Travel%20Blog/update_post_pop_up_vfrlv6.png)

* Asks the user if they want to update their post.

### Add Comment Page
![Add comment Page](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400353/Porject%204%20Travel%20Blog/add_comment_page_kbqshm.png)

* Provide a form to allow registered Site Users to create a new comment.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Add Category Page
![Add category image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400353/Porject%204%20Travel%20Blog/add_category_page_vt9l04.png)

* Only available to the admin. Users don't have access to this page.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Edit Category Page
![edit category image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400355/Porject%204%20Travel%20Blog/edit_category_page_s08eav.png)

* Only available to the admin. Users don't have access to this page.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Delete Category Button
![delete category image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400354/Porject%204%20Travel%20Blog/delete_pop_up_for_category_rg3svc.png)

* Only available to the admin. Users don't have access to this button.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Category List Page
![Category list image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400353/Porject%204%20Travel%20Blog/category_list_page_cxraa9.png
)

* Available to all users to see all of the available categories.

* A link is available on the category, which lists all the posts associated with that category.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Category Page
![Category image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696441802/Porject%204%20Travel%20Blog/category_page_iveuej.png)

* Available to all users to see all posts associated with the category they have selected. 

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Edit Settings Page
![Settings image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400356/Porject%204%20Travel%20Blog/edit_settings_page_lubpoo.png)

* Available to all users to see their current settings and update them. 

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Password Page
![Password image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696400353/Porject%204%20Travel%20Blog/chnage_password_page_nw344c.png)

* Available to all users to update their password. 

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### User Profile Page
![User Profile image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696443451/Porject%204%20Travel%20Blog/user_profile_rvfo7d.png)

* Available to all users to see their information and their posts related to their profile. 

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Edit User Profile Page
![User Profile image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696443451/Porject%204%20Travel%20Blog/edit_profile_page_ahnlwd.png)

* Available to all users to update their information about their profile. 

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Modal for User Profile 
![Modal image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696443451/Porject%204%20Travel%20Blog/modal_for_complete_profile_r2zkbb.png)

* Available to all users after log in, they see this message warning them that if they want to create posts they need to fill in their profile, otherwise they can not create posts, like or/and dislike posts.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

### Complete User Profile 
![fill in profile image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696443450/Porject%204%20Travel%20Blog/Complete_profile_page_l15hqx.png)

* Available to all registered users after log in, they can fill in the form and complete their profile, which will be visible to all registered users.

<br>

[Back to top ⇧](#the-roaming-nomad)

<br>

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

The testing documentation can be found [here](https://github.com/Delfinistkata/the-roaming-nomad/blob/main/TESTING.md).

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

Page | Desktop |
--- | --- |
| Login/Home | ![Desktop Login/Home Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449906/Porject%204%20Travel%20Blog/finished%20product%20P4/home_logged_in_1_e7mvae.png) 
| Logout/Home | ![Desktop Logout/ Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449793/Porject%204%20Travel%20Blog/finished%20product%20P4/loggedout_home_znbvpg.png) 
| Post Detail | ![Desktop Post Detail Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449793/Porject%204%20Travel%20Blog/finished%20product%20P4/post_detail_vtjsx8.png) 
| Create Post | ![Desktop Create Post Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449791/Porject%204%20Travel%20Blog/finished%20product%20P4/add_post_an2gwy.png) 
| Edit Post | ![Desktop Edit Post Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449793/Porject%204%20Travel%20Blog/finished%20product%20P4/edit_post_page_fu4qfi.png) 
| Category | ![Desktop category Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449792/Porject%204%20Travel%20Blog/finished%20product%20P4/category_page_kieir0.png)
| Category List | ![Desktop category List Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449791/Porject%204%20Travel%20Blog/finished%20product%20P4/category_list_s6rwan.png)
| Create Category | ![Desktop Create category Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449791/Porject%204%20Travel%20Blog/finished%20product%20P4/add_category_gkjs8y.png) 
| Edit Category | ![Desktop Edit Category Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449791/Porject%204%20Travel%20Blog/finished%20product%20P4/edit_category_zqu54j.png) 
| Sign Up | ![Desktop Sign Up Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449791/Porject%204%20Travel%20Blog/finished%20product%20P4/signup_xocwq2.png) 
| Sign In | ![Desktop Sing In Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449793/Porject%204%20Travel%20Blog/finished%20product%20P4/login_w24twg.png)
| Edit Settings | ![Desktop Edit Settings Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449792/Porject%204%20Travel%20Blog/finished%20product%20P4/edit_settings_profile_j1zpa4.png)
| Edit Profile | ![Desktop Edit Profile Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449792/Porject%204%20Travel%20Blog/finished%20product%20P4/edit_profile_page_oemgob.png)
| Edit Password | ![Desktop Edit Settings Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449792/Porject%204%20Travel%20Blog/finished%20product%20P4/change_password_page_segr93.png)
| User Profile | ![Desktop Edit Category Page image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696449802/Porject%204%20Travel%20Blog/finished%20product%20P4/profile_page_bhjglk.png)

[Back to top ⇧](#the-roaming-nomad)

## Credits

Throughout the building process I found many helpful tutorials online.
I sometimes applied principles within them to the site, after fully understanding their code and modifying to fit the site's needs.

<br>

### Media

* [Pexels](https://www.pexels.com/)

* [Unsplash](https://unsplash.com/)

* [Pixabay](https://pixabay.com/)

* [YoMeanimo!](https://www.yomeanimo.com/)

[Back to top ⇧](#the-roaming-nomad)
### Code

[W3Schools](https://www.w3schools.com/) - was consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - This repository was created using the template provided by Code Institute.

[Code Institute Videos](https://codeinstitute.net/) - The video series that help me throughout project for P4.

[Django Documentation](https://docs.djangoproject.com/en/4.0/) - Django step-by-step document to ensure everything is set up correctly. 

[Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/faq.html) - referenced during development.

[Cloudinary Documentation](https://cloudinary.com) - referenced during development.

[CKeditor Documentation](https://ckeditor.com/) - referenced during development.

[Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/) - used for information.

[John Elder - Django](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy) - YouTube series that help me throughout the project.

[Stackoverflow](https://stackoverflow.com/) -Used to search issues I had.

[Slack](https://slack.com/intl/en-ie/) - I used Slack when I had issues.

<br>

[Back to top ⇧](#the-roaming-nomad)

## Known Bugs

No bugs found after testing.

[Back to top ⇧](#the-roaming-nomad)

## Acknowledgements

<hr>
<br>

This project was developed and designed as a Portfolio 4 Project for Full Stack Software Developer Diploma course at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor Marcel Mulders for his invaluable feedback and guidance, our facilitator Chris Quinn, the Slack community, and all at the Code Institute for their help and support. I really enjoyed working on this project.

<br>
<br>

[Back to top ⇧](#the-roaming-nomad)