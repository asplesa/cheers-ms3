# **Cheers**

1. Overview
2. UX
3. Features
4. Technologies Used
5. Testing
6. Deployment
7. Credits
8. Acknowledgements
9. Disclaimer

# **Overview**

Cheers is a community platform for registered and non-registered users to share their cocktail knowledge and discover new cocktails. Registered users can add and share cocktails all over the world. Non-registered users to view the recipes so they can try them out themselves.

The project is developed primarily using  **HTML** ,  **CSS, Python+Flask, MongoDB** and,  **JavaScript** for additional functionality.

[View the live project here.](https://cheersms3.herokuapp.com/)

![Homepage](/static/images/readme/responsive.JPG)

![](RackMultipart20210523-4-53ytne_html_892bc76665002c1a.gif)

# **UX**

**Strategy**

**User Interview**

**What are some of your considerations when using the web to search cocktails.**

&quot;_I want one place where I can access all my favourite cocktail recipes&quot;._

&quot;_I want to learn about new cocktails from different parts of the world that I&#39;m not aware of&quot;._

**Business Strategy**

**Psychological Factors**

- Evoke a fun, colourful response from the imagery and branding used.
  - Bright colours used to immediately draw and eye and enticing imagery to tempt users to try them out.
  - Minimalist design used so as not to overwhelm the user.
  - Consistent use of branding throughout the site.

**Content Strategy**

- Clear and concise information with simple instructions and methods to prepare the cocktails.
- The visual imagery is really important to encourage users to try them out. Fun, colourful imagery is used.
- Every page footer contains social links to encourage further engagement and brand building.

**User Stories**

1. As a **registered user** , I want to be able to create an account with a username and password which will allow me to login and logout as I wish.
2. As a **registered user** , I want to have full control of my account so I can edit or delete my account.
3. As a **registered user,** I want to be able to add, edit and delete my own recipes so that others can try them out.
4. As a **guest user** , I want to be able to easily search for cocktails that I can try out.
5. As a **guest user** , I want the ingredients and method to prepare for cocktails to be available so I can try them out.
6. As a **site owner,** I also want to be able to have full control over recipes that have been uploaded by users .
7. As a **site owner,** I want to be able to be able to delete users if necessary.
8.  As a **site owner** , I want to be able to create, edit and delete cocktail categories.

**Scope**

**Requirements**

**Encourage and Allow User Engagement**

- To ensure that the site immediately showcases what it is about.
- There are clear call to actions for the user to enable user interaction and engagement.
- Simple but effective search features will enable this interaction.

**User Confidence**

- Strong and consistent branding will be used across all pages.
- Easy to use site but a minimalistic design to ensure only relevant information is shown so as not to overwhelm the user with features.
- Design and colour palate will instil a feeling of fun.

**Skeleton**

**Wireframes**

Balsamiq was used to create wireframes of the site. These are be found ![here](/static/images/Cheers-web-wireframe.pdf)

The initial wireframes consisted of 9 pages and wireframes were created from desktop, mobile and tablet.

We created a simple homepage with minimal content. We used images and headers to show the user what the site is about on first entry.

The wireframe was amended during development to replace the featured cocktails section with a more visually appealing carousel of cocktail images. A button linking to all cocktails was also added to the text box overlay on the main image for easy access to the cocktail recipes.

**Surface**

The site&#39;s aesthetic design is aligned with the values and branding; simple, fun and colourful.

**Logo**

The project&#39;s &#39;surface&#39; design commenced with the logo design. Work was carried out to ensure Colours, Fonts, and Imagery were all created using Canva. A cocktail icon was used as the favicon for the site.

**Colour Scheme**

A bright green colour was chosen as the primary site colour. Green is the color most commonly associated with freshness, and life. The simple colour scheme is visually effiective.

**Typography**

Segoe UI was chosen as the font for the page&#39;s sub-headings and body text. The font is clean, modern and is easy to read. Work Sans was used for the logo.

**Images**

The images used in this project were selected from [Canva](https://www.canva.com/). The pictures were specifically selected due to their contextual relevance and colour schemes. Cocktails that have been uploaded by users are uploaded by entering the URL. Users also have to input the source of the images for credit purposes.

# **Features**

**Existing Features**

This project consists of twelve pages in total.

**Database structure**

The data of this project are stored in my MongoDB database within three collections:

- _Categories_ - This collection stores the different categories of the recipes, of which there are six: stirred, sour, fizz, frozen, highballs and non-alcoholic.
- _Cocktails_ - When a user uploads a cocktail the data is sent to this collection with the following information: The cocktail name, the category, description, an array with its ingredients, the preparation steps and finally the recipe picture, the credits for the image and the user profile who created the recipe.
- _Users_ - This collection stores the user&#39;s username, encrypted password, and email.

- **Navbar:** The navbar is visible and responsive in every page, and is consistent on every page due to the use of the jinga templating language. It displays the logo of the website and the options &quot;Home&quot;, &quot;All Cocktails&quot;, &quot;Log In&quot; and &quot;Register&quot; when the user is not logged in. Materializecss was used on the front end.

![Navbar](/static/images/readme/navbar.JPG)

- **Carousel:** A carousel of scrolling images was used for a more visually engaging user experience. ![cocktail-time](/static/images/readme/cocktail-time.JPG)
- **Social Media Links:** are on the footer of every page so easy access.
- **Cocktail Recipes:** The recipes are displayed on responsive cards and include the name, category, an image (or a default image if none is available) and a link to try the cocktail.
- **Search Feature:** Allows users to search by cocktail name or by category. When no results match the search, the text &quot;No Cocktails Found&quot; is displayed.

![search-cocktails](/static/images/readme/search-cocktails.jpg)

- **Register:** The registration form takes the following inforkmation of the user to create an account :

  - the user&#39;s email address,
  - The user&#39;s username,
  - The user&#39;s password,

The passwords are hashed and protected using the import &quot;generate\_password\_hash, check\_password\_hash&quot; from werkzeug security. All that data is stored in the collection &quot;users&quot; on MongoDB Atlas database.

- **Log In:** Once registered a user can log in using the log in form to access their account. The user needs their password and username to log in.
- **Profile:** Once logged in a user has all the CRUD functionality available to them allowing them to update, edit and delete their profiles.
- **Add Cocktail:** Once logged in, a user also has the full CRUD functionality available to them to add, edit, update and delete cocktails.
- **Admin:** In addition I created an Admin or super user who the ability add, edit or delete categories, cocktails and users.

**Responsive Layout and design**

The site is designed to be fluid, dynamic, and responsive to all screen sizes andresolutions. The homepage is split into clear sections which expand or shrink to equal

sizes responsively to a device&#39;s height and width.

**Future Feature Considerations**

**Creation of a mailing list database**

The addition of a mailing list which would be linked and stored in a database should be considered. This will allow for future communication and engagement with users.

**Enhanced User Authentication**

This would enhance the overall security and data protection on the site.

![](RackMultipart20210523-4-53ytne_html_892bc76665002c1a.gif)

# **Technologies Used**

- The front end of the project was primarily written in [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [Javascript](https://www.javascript.com/) and the [Materialise](https://materializecss.com/) framework. Small snippets of JavaScript were used to enhance user experience.
- The Back end used [Flask](https://flask.palletsprojects.com/en/1.1.x/), [MongoDB](https://www.mongodb.com/1), [Jinja](https://jinja.palletsprojects.com/en/2.11.x/), [Python](https://www.python.org/) and [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- [Gitpod](https://gitpod.io/) IDE - the project was written and tested using Gitpod. It was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) for hosting source code, for utilising git version control, and for hosting the site on GitHub pages.
- [Code Institute&#39;s Gitpod Template](https://github.com/Code-Institute-Org/gitpod-full-template) – the project template was generated from this.
- [Heroku](https://www.heroku.com/) was used to deploy the platform.
- [FontAwesome](https://fontawesome.com/) v5.13.1, was used for icons for aesthetic and UX purposes..
- [Balsamiq](https://balsamiq.com/) was used to create the ![wireframes](/static/images/Cheers-web-wireframe.pdf) during the design process.
- [jQuery](https://jquery.com/) v3.6.0
- [Google Chrome](https://www.google.com/intl/en_uk/chrome/) [Dev Tools](https://developers.google.com/web/tools/chrome-devtools) was used for debugging throughout the development process.
- [Google Fonts](https://fonts.google.com/) was used to import the Work Sans font into the style.css file which is used for the logo.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) and [W.A.V.E](https://wave.webaim.org/)  were used to assess the site&#39;s accessibility.
- [W3C HTML Markup Validator](https://validator.w3.org/) was used to validate the HTML.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
- [HTML Formatter](https://www.webformatter.com/html)  html formatter to help keep things tidy
- [Am I Responsive](http://ami.responsivedesign.is/) –was used to create responsive image for readme.MD
- [Canva](https://www.canva.com/) was was used to create the logo, resizing images and editing photos for the website.

![](RackMultipart20210523-4-53ytne_html_892bc76665002c1a.gif)

# **Testing**

Please view the complete testing process in [this separate document](https://github.com/asplesa/cheers-ms3/blob/master/readme/testing.md).

# **Deployment**

**How this Project was Deployed**

This project was deployed to Heroku via the following steps:

- Create a requirements.txt file using the command  **pip3 freeze --local \&gt; requirements.txt**  in your CLI.
- Create a Procfile (always with an uppercase P) through the command  **echo web: python app.py \&gt; Procfile**. Commit and Push.
- Create an account on [**Heroku**](https://www.heroku.com/home).
- Create a new app with  **unique name**.
- Select your  **nearest region**.
- Create a  **new python project**  within the project.
- Link that project through your  **Github repository**  in the  **deployment**  section.
- Navigate to Heroku Settings and set up the following in  **Config Vars**

**Local Deployment**

- Open browser of choice.
- Copy/Paste the address of **[Cheers! repository](https://github.com/asplesa/cheers-ms3)** in your search box.
- When on the page, click on the &quot;Code&quot; button.
- Copy the the [**HTTPS link**](https://github.com/asplesa/cheers-ms3).
- Open your IDE and in your terminal, create a virtual environement supporting python and flask and activate it.
- Type &quot;git clone&quot; and paste the **[HTTPS Link](https://github.com/asplesa/cheers-ms3.git)**.
- Create an environment file called &quot;env.py&quot; and add :
  - MONGO\_URI=mongodb+srv://...
  - SECRET\_KEY= [Your Secret key]
- Add your env.py to .gitignore. to avoid it being uploaded.
- In app.py, switch  **debug=False**  to  **debug=True**
- Upgrade pip locally with the command &quot;pip install -U pip&quot;.
- Install the modules used to run the application using &quot;pip freeze \&gt; requirements.txt&quot; in your terminal.
- In parallel, create a MongoDB account and create a database called  **&quot;cocktail_recipes\_project&quot;**.
- These are the following collections in the database: categories, cocktails, users.

# **Credits**

**Content**

- All cocktail recipes were sourced from the [TheCocktailDB](https://www.thecocktaildb.com/) database.

- All business ideas and general development concepts were devised by me.

**Media**

- All Photographs excluding the cocktail recipes images were sourced from [Canva.com](https://www.canva.com/).
- The logo was created in [Canva.com](https://www.canva.com/)
- All cocktail image were sourced from the [TheCocktailDB](https://www.thecocktaildb.com/) database.

**Many thanks to:**

- My mentor  **Seun Owonikoko**  for her advice.
- **Code Institute Slack community**  for the technical and emotional support.