**Testing**

The testing process below includes:

- Testing user stories
- Validating HTML, CSS, JavaScript and Python
- Checking responsiveness of design on all screen sizes
- Manually testing the functionality of all links

To return to the previous document, please click [here](https://github.com/asplesa/cheers-ms3/blob/master/README.md).

**Table of contents**

- [**Testing User Stories**](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Testing-User-Stories)
  - [Project Stakeholder](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Project-stakeholder)
  - [New users](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#New-users)
  - [Returning Users](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Returning-Users)
  - [Frequent User](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Frequent-User)
- [**Validating the project code**](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Validating-the-project-code)
  - [HTML](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#HTML)
  - [CSS](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#CSS)
  - [JavaScript](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#JavaScript)
  - [Python](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Python)
- [**Compatibility tests**](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Compatibility-tests)
  - [Using different browsers](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Using-different-browsers)
  - [Using different screen sizes](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Using-different-screen-sizes)
- [**Manual tests**](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Manual-tests)
  - [Navigation](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Navigation)
  - [Home](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Home)
  - [Recipes](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#All-Cocktails)
  - [Recipe](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Cocktail)
  - [Login](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Login)
  - [Register](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Register)
  - [Profile](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Profile)
  - [Edit profile](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Edit-profile)
  - [Add recipe](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Add-New-Cocktail)
  - [Edit recipe](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Edit-cocktail)
- [**Bugs**](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md#Bugs)

**Testing user stories**

**Registered User**

- The registered user wants to be able to add new cocktail recipes for people to try out and wants to be able to see what recipes they added. They can log back in into the website, go to their profile page and check among the shared recipes which was the desired one.
- This returning user saw a different and better way to make a recipe they previously uploaded, so they return to the website, login and decide or to search for the recipe directly in the searchbox in the recipes page or in their shared recipes section of the profile page.
- The registered user wants to be able to log in and edit, improve or delete any recipes they uploaded.

**Guest Users**

- The guest user is looking for an online resource which has a variety of cocktail recipes from around the world that are available to them to try out. This category of user will be happy with the site as it enables them to view and try the recipes quickly and easily without having to create an account.

**Site Owner**

- As the site owner I wanted to make sure that users of the website found valuable information that would entice them to return to the site. I created a project easy to navigate and to use, there is a full access cocktail recipes as a guest user and, if the user is logged in they can easily add new cocktails.

**Validating the project code**

**HTML**

Ny HTML code passed through the [W3C Markup Validation Service](https://validator.w3.org/).

There were also errors related to the creation of the HTML files through Jinja templates.

1. _Non-space characters found without seeing a doctype first. Expected ._
2. _Element is missing a required instance of child element &#39;title&#39;._
3. _Bad value: for attribute &#39;x&#39; on element &#39;y&#39; illegal character_ As each HTML base.html, the individual documents do not declare the doctype, set the language or include a head element. These errors were therefore present on each file I tested, except for base.html that fulfilled the requirements. This error was expected and did not lead to any changes.
4. _Bad value: &#39;url for&#39;_ As with the first error, this was common across all HTML template files. It was also to be expected, as the validator was not anticipating to find href=&quot;...url\_for...&quot;

**CSS**

I checked my CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). This test passed without any errors.

**JavaScript**

I used [JSHint](https://jshint.com/) to check my JavaScript code. The test passed without any errors.

**Python**

I used [PEP8](http://pep8online.com/) to check my Python code. No errors noted.

**Compatibility tests**

**Using different browsers**

I manually tested the project on the following web browsers, checking that all aspects worked as planned:

- Google Chrome
- Mozilla Firefox
- Ecosia
- Microsoft Edge

This did not lead to any errors or problems.

**Using different screen sizes**

I manually tested the design of the live project by doing the following:

- Using Google Developer Tools to view the project on devices with different screen sizes.
- Asking for feedback from friends and family who opened and interacted with the project on their devices.

**Manual tests**

**Navigation Links &amp; Buttons**

When All Navigation links were manually checked and work. All footer social links checked and work.

**Home**

- _All Cocktails_ button - Passed, directs the user to the All Cocktails page
- _Cocktails_ button - Passed, directs the user to the All Cocktails page
- _Log In_ button - Passed, directs the user to the Log In page
- _Register_ button - Passed, directs the user to the Register page

**All Cocktails**

- Shows the user all the shared Cocktails which the user can search through.
- _Searcbox_ - Passed, when digited the name of a cocktail the searchbox shows it either we press enter or the _Search_ button.
- _Reset_ / _All_ button - Passed, when clicked they reload the page showing all the cocktails uploaded.
- _Cocktail Category Buttons_ - Passed, all 7 buttons checked and when clicked loads all the respective cocktails
- Clicking the cocktail name - Passed, the user is directed to the individual cocktail page
- _MAKE IT..._ button - Passed, the user is directed to the individual cocktail page
- _Edit_ button - Passed, the user is directed to the edit cocktail page
- _Delete_ button - Passed, the user gets the modal question back, to ask if they really want to delete the cocktail
- _Delete_ modal button - Passed, the user gets the modal message back

**Cocktail**

- The user see all the data from the cocktail page and if the user is equal to the creator of the recipe or the admin, the user can see two extra buttons.
- _Edit_ button - Passed, the user is directed to the edit cocktail page
- _Delete_ button - Passed, the user gets the modal question back, to ask if they really want to delete the cocktail
- _Go Back_ modal button - Passed, the user is directed to the cocktail page
- _Delete_ modal button - Passed, the user gets the modal message back
- &quot;Back to Cocktails &quot; button, Every user can see it - Passed, the user is directed to the cocktails page

**Login**

- When a user enters their correct username and password they are redirected to their profile page.
- Users are unable to log in if they enter an incorrect username or password.
- With the correct username and password, a user successfully gets redirected to their &#39;Profile&#39; page
- The Register Link at the bottom of the page directs users to register page

**Register**

- Username, Password and Email must be completed before a user can register. Warning red invalid text will appear as a helper to users if they don&#39;t complete
- If a user trys to use a username that is already taken they are shown the following message: &quot;Username already exists&quot;
- The Log In Link at the bottom of the page directs users to login page

**Profile**

- _Edit_ button - Passed, the user is directed to the edit profile page
- _Delete_ button - Passed, the user gets the modal question back, to ask if they really want to delete the profile
- _Go Back_ modal button - Passed, the user is directed to the profile page
- _Delete_ modal button - Passed, the user gets the modal message back
- _Add Cocktail_ button - Passed, the user is directed to the add recipe page

**Edit profile**

- The user gets a form in which they can change the username, email or password. The inputs cannot be empty, every field is required.

**Add New Cocktail**

- All section on the form must be completed, if not the user is shown a new error message under each line with the text telling them to complete.
- _Add Recipe_ button - Passed, the user uploads the recipe and gets the flash message: &#39;Cocktail Added!&#39;
- _Back to Cocktails_ button - Passed, the user is directed to the cocktails page

**Edit cocktail**

- All fields are pre-populated so the user so the user can change what fields are needed.
- _Save Changes_ button - Passed, the user uploads the recipe and gets the flash message: &#39;Cocktail!&#39;
- _Cancel_ button - Passed, the user is directed to the cocktails page

**Bugs**

- The ingredients on the Edit Cocktail page are displaying as arrays. NOT FIXED CURRENTLY.

I didn&#39;t find any other bugs.

**Usability Testing**

Tested on the following:

- https://contrast-ratio.com/ Used to assess the color scheme contrast
- https://developers.google.com/web/tools/lighthouse
- https://wave.webaim.org/
- Screen Reader for Google Chrome

**Performance Testing**

- **Tested on Developer Tools Lighthouse.**
