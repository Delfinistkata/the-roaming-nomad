# The Roaming Nomad

[Back to the README.md file](https://github.com/Delfinistkata/the-roaming-nomad/blob/bbe106d7e2dbd8e1cc77cc84e4bd53b2be1462bb/README.md)  

[Back to the Testing section in the README.md file]()

[View the live website here]()  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)


***


## Testing User Stories

### User Stories 

User Story | PASS/FAIL
---|---
As a Site User I can view a list of posts so that I can choose which post I want to view. | PASS
As a Site User I can register and login with my account so that I can get the extended features of the website to comment/like and create my own posts. | PASS
As a Site User/Admin I can view likes on posts so that I can see which posts are popular. | PASS
As a Site User I can comment on a post so that I can feel part of the conversation. | PASS
As a Site User I can create my own user profile so that I can feel part of the community. | PASS
As a Site User I can edit and delete my own posts so that I can interact with the content.  | PASS
As a Site User /Admin I can view comments on an individual post so that I can read the conversation. | PASS
As a Site User I can like/unlike posts so that I can interact with the content. | PASS
As a Site User I can view a more detailed version of the post so that I can read the article in full. | PASS
As a Site User I can call up all blogs for a certain category so that I can filter the blogs to my needs. | PASS
As a Site User I can view a paginated list of posts so that I can easily select a post to view. | PASS
As a Site User I can update my profile so that other users can view my details | PASS
As a Site Admin I can create, read, update and delete posts so that I can manage my blog content. | PASS
As a Site Admin I can approve and disapprove comments so that I can filter out objectionable comments.| PASS
As a Site Admin I can access the admin from a link on the web page so that I have easier access. | PASS


## Code Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML code of the project in order to ensure there were no syntax errors.

As my project uses Jinja syntax, such as `{% for ... %}`, `{% url 'home' %}`, and `{{ ... }}`
it will not validate properly if I copy and paste into the HTML validator straight from my source files.

Usually in order to properly validate these types of files, it's recommended to
[validate by url](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, nearly all of the pages on this site require a user to be logged-in and authenticated,
and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to the pages.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| templates/index.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095354/Porject%204%20Travel%20Blog/index_ll5ocz.png)  |
| members/edit_profile.html  | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095354/Porject%204%20Travel%20Blog/edit_settings.html_wq8srg.png)  |
| members/login.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095354/Porject%204%20Travel%20Blog/login.html_ahdlgg.png)  |
| members/register.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095355/Porject%204%20Travel%20Blog/register.html_jihuwm.png)  |
| templates/post_detail.html  | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095355/Porject%204%20Travel%20Blog/post_detail_f6vstr.png)  |
| members/user_profile.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095355/Porject%204%20Travel%20Blog/user_profie.html_zsnyph.png)  |
| templates/add_category.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095356/Porject%204%20Travel%20Blog/add_category.html_e0dtgq.png)  |
| templates/add_comment.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095356/Porject%204%20Travel%20Blog/add_comment.html_ho5spk.png)  |
| templates/category_list.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095356/Porject%204%20Travel%20Blog/category_list.html_kvr6af.png)  |
| members/change-password.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095357/Porject%204%20Travel%20Blog/change_password.html_ng2ijw.png)  |
| templates/category.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095357/Porject%204%20Travel%20Blog/category.html_e6rstt.png)  |
| templates/create_post.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095358/Porject%204%20Travel%20Blog/create_post.html_r0el9y.png)  |
| members/create_user_profile_page.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095358/Porject%204%20Travel%20Blog/create_profile_page.html_shkdd1.png)  |
| templates/edit_category.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095358/Porject%204%20Travel%20Blog/edit_category.html_mka8q5.png)  |
| templates/edit_post.html  | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095359/Porject%204%20Travel%20Blog/edit_post.html_ebghbw.png)  |
| members/edit_profile_page.html | No errors / warnings | ![ reviewed image ](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696095359/Porject%204%20Travel%20Blog/edit_profile_page.html_jd4x6p.png)  |


### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the CSS code of the project in order to ensure there were no syntax errors. 

W3C CSS Validator found no errors or warnings on my CSS.

![CSS validation image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696013193/Porject%204%20Travel%20Blog/css_file_qyjymf.png)

### Pyhton

Pylint was used continuously during the development process to analyze the Python code for programming errors.

[PEP8 online](http://pep8online.com/) was further used to validate the Python code to validate the Python code for PEP8 requirements. See below the validation results and the reviewed results. 


| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| travelblog/admin.py | No errors / warnings |![admin.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012288/Porject%204%20Travel%20Blog/travelblog_admin.py_x7bhdx.png) |
| trvelblog/forms.py | No errors / warnings | ![forms.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012288/Porject%204%20Travel%20Blog/travelblog_forms.py_dwjuxv.png) |
| travelblog/models.py  | No errors / warnings | ![models.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012288/Porject%204%20Travel%20Blog/travelblog_model.py_hu8jah.png) |
| travelblog/urls.py | No errors / warnings | ![urls.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012289/Porject%204%20Travel%20Blog/travelblog_urls.py_f2pzer.png) |
| travelblog/views.py | No errors / warnings | ![views.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012289/Porject%204%20Travel%20Blog/travelblog_views.py_l9efvs.png) |
| theroamingnomad/urls.py | No errors / warnings | ![urls.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012288/Porject%204%20Travel%20Blog/the_roaming_nomad_urls.py_tsgcym.png) |
| theroamingnomad/settings.py | No errors / warnings | ![settings.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012287/Porject%204%20Travel%20Blog/the_roaming_nomad_settings.py_t5wlma.png) |
| members/views.py | No errors / warnings | ![views.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012287/Porject%204%20Travel%20Blog/members_views.py_parsmq.png) |
| members/urls.py | No errors / warnings | ![urls.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012287/Porject%204%20Travel%20Blog/members_urls.py_ybpuy6.png) |
| members/forms.py | No errors / warnings | ![forms.py code reviewed image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696012287/Porject%204%20Travel%20Blog/members_forms.py_crr8rb.png) |


### JavaScript

[JSHints JavaScript Code Quality Tool](https://jshint.com/) was used to validate the site's JavaScript code. 

![JS validation image](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696091355/Porject%204%20Travel%20Blog/js_hint_zkdj3x.png)


## Accessibility

Lighthouse in Chrome DevTools has been used to confirm that the colors and fonts being used throughout the website are easy to read and accessible. See reports in the table below:

### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Index Log In | ![Index Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087860/Porject%204%20Travel%20Blog/index_logged_in_pbmemy.png) |
| Category | ![Category Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087860/Porject%204%20Travel%20Blog/category_list_snznec.png) |
| Register | ![Register Lighthouse Report]() |
| Login | ![Login Lighthouse Report]() |
| Index Logout | ![Logout Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087860/Porject%204%20Travel%20Blog/index_page_logged_out_fr2us6.png) |
| Post Detail | ![Post Detail Lighthouse Report]() |
| User Profile  | ![User Profile Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696088569/Porject%204%20Travel%20Blog/profile_page_kc6fqw.png) |
| Add Comment | ![Add Comment Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696088647/Porject%204%20Travel%20Blog/add_comment_plmcvh.png) |
| Create Post | ![Create Post Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087860/Porject%204%20Travel%20Blog/create_post_n83i8z.png) |
| Edit Post | ![Edit Post Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087860/Porject%204%20Travel%20Blog/edit_post_n3mxff.png) |
| Create Category | ![Create Category Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696088217/Porject%204%20Travel%20Blog/add_category_cjmve1.png) |
| Edit Category | ![Edit Category Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087860/Porject%204%20Travel%20Blog/edit_category_w6zkc2.png) |
| Fill in User Profile | ![Fill in User Profile Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696088446/Porject%204%20Travel%20Blog/fill_in_profile_divnti.png) |
| Edit User Profile | ![Edit User Profile Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696091102/Porject%204%20Travel%20Blog/edit_profile_page_xyabmn.png) |
| Edit User Profile Settings | ![Edit User Profile Settings Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696087861/Porject%204%20Travel%20Blog/edit_settings_profile_page_tebmd2.png) |
| Change Password | ![Change Password Lighthouse Report](https://res.cloudinary.com/doyc0uqcs/image/upload/v1696090866/Porject%204%20Travel%20Blog/change_password_ukzf6c.png) |


## Tools Testing

### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* [Am I Responsive?](http://ami.responsivedesign.is/#) was used to check responsiveness of the site pages across different devices.

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No issues | Pass|
Safari | No issues | Pass |
Mozilla Firefox | No issues | Pass |
Microsoft Edge | No issues | Pass |


### Device Compatibility

Device | Outcome | Pass/Fail
--- | --- | --- |
Laptop | No issues. | Pass |
iPad  | No issues. | Pass |
Samsung Galaxy S20 | No issues. | Pass |
iPhone 12 Pro | No issues. | Pass |
iPhone XR | No issues. | Pass |
iPhone SE | No issues. | Pass |
iPhone 4 | No issues. | Pass |

### Test Results

#### General
