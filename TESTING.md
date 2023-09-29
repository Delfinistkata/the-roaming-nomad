# The Roaming Nomad

[Back to the README.md file]()  

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

W3C Markup Validator found the following errors concerning index.html.

![index.html]()

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

![JS validation image]()


## Accessibility

Lighthouse in Chrome DevTools has been used to confirm that the colors and fonts being used throughout the website are easy to read and accessible. See reports in the table below:

### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Index | ![Index Lighthouse Report]() |
| Category | ![Category Lighthouse Report]() |
| Register | ![Register Lighthouse Report]() |
| Login | ![Login Lighthouse Report]() |
| Logout | ![Logout Lighthouse Report]() |
| Post Detail | ![Post Detail Lighthouse Report]() |
| User Profile  | ![User Profile Lighthouse Report]() |
| Add Comment | ![Add Comment Lighthouse Report]() |
| Create Post | ![Create Post Lighthouse Report]() |
| Edit Post | ![Edit Post Lighthouse Report]() |
| Delete Post | ![Delete Post Lighthouse Report]() |
| Create Category | ![Create Category Lighthouse Report]() |
| Edit Category | ![Edit Category Lighthouse Report]() |
| Delete Category | ![Delete Category Lighthouse Report]() |
| Fill in User Profile | ![Fill in User Profile Lighthouse Report]() |
| Edit User Profile | ![Edit User Profile Lighthouse Report]() |
| Edit User Profile Settings | ![Edit User Profile Settings Lighthouse Report]() |
| Change Password | ![Change Password Lighthouse Report]() |


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

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
Laptop | Windows 10 | No issues. | Pass |
iPad Pro | iOS 15 |No issues. | Pass |
iPhone XR | iOS 15 |No issues. | Pass |
iPhone 7 | iOS 15 |No issues. | Pass |

### Test Results

#### General
