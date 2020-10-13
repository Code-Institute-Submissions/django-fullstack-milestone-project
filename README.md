# Milestone Project 4 - Full Stack Frameworks with Django 

## Your Tale Jewellery

## Project Description
The requirements of this project was to build a full-stack site based around 
business logic used to control a centrally-owned dataset. Providing 
authentication functionality and a paid-for service is also necessary as
part of this project. The vision for this website was to design and create 
an e-commerce site where users can search, review and purchase items of jewellery, 
as well as create a profile to view their purchase history. All items of 
jewellery can be sorted by novel themes (such as science, art, nature, etc) 
and by metals (gold or silver). The store owner will also have the ability to
provide discounts to their customers, with assigned expiry dates.

## UX
### Colour Palette
Deep green, yellow and white are the primary colours of the site. The white 
and yellow are representative of gold and silver - the choices of metal in 
available in the store. The dark green provides contrast to balance the other
two colours.

### Images
For the jumbotron on the landing page, the jewellery-related image of a 
simple gold ring on a silver chain is used - with white text to the left.
All product images were sourced from www.amazon.co.uk and were resized via
css for the purpose of this project. As most of the images have a white 
background, a white background was used on the body of the website to avoid 
any inconsistencies with image ratios.

### Fonts
For legibility, the font Lato was used for most of the body, including some 
of the buttons. The cursive font of Tangerine was used for the headings add a
sense of elegence to the site.

### User Journey
The following user stories were identified:
1. "As a shopper, I'd like to view all available products and choose the ones I wish to purchase."
2. "As a shopper, I'd like to search and filter the products for a more efficient browsing experience."
3. "As a shopper, I'd like to be able to view the total amount of my shopping in a convenient way."
4. "As a site user, I'd like to register for an account, login and logout from the site easily."
5. "As a site user, I'd like to receive a confirmaiton email when registering."
6. "As a shopper, I'd like to select the size and quantity of the item I'm purchasing."
7. "As a shopper, I'd like to be able to view and adjust the quantities of items in my bag."
8. "As a shopper, I'd like to pay for my purchase easily and securely."
9. "As a shopper, I'd like to receive a confirmaiton email after an order."
10. "As a shopper, I'd like to be able to view my order history in one convenient place."
11. "As a shopper, I'd like to be able to review products to provide feedback on items."
12. "As a store owner, I'd like to be able to add, edit and delete products from the store."
13. "As a store owner, I'd like to be able to offer discounts to customers to increase sales."

To address these user needs, the features below were added.

## Features
### Current Features
1. Home - A landing page with a call-to-action jumbotron and "Shop Now" button directing the user to the products page.
2. Search bar - Allows the user to search for terms that appear in the title of the products or their descriptions and display all relevant results.
3. Navbar - Not logged in - Displays links to Register or Login which redirect to the associated pages.
4. Navbar - Logged in and not Store Owner - Displays option to view profile or to Logout.
5. Navbar - Logged in and is Store Owner - Displays link to Product Management redirects to an Add Product page.
6. Registering & Confirmation Email - User can register a account and will be sent a link to the provided email address, asking them to confirm thier registraiton.
7. Profile & Logging in - Once registered, a profile is created and the user is asked to login with their details. 
8. Products Page - Filtering Products - Able to view and filter list of products by Category (Rings, Necklaces, Bracelets, Earrings, Cufflinks, Tie Bars, Brooches), Metal (Gold or Silver), Theme (Nature, Science, Art, Music, People) and sort items by price.
9. Products Page - Logged in and not Store Owner - Have the ability to review products even if not in order history (allows customers who have purchased an item offline to still review).
10. Products Page - Logged in and is Store Owner - Able to Edit or Delete any product from Products page.
11. Product Details - Can view the details of each product individually and choose the sizes of some (in the case of rings) to add to bag. Displays all reviews for this product at bottom of page.
12. Bag - Can add products to a virtual bag, and from the Bag page, can edit or remove the item, or proceed to checkout.
13. Toasts - Displays four types of messages (info, success, error, warning) to provide the user with feedback on their activities. Also displays the items currently in bag.
14. Checkout - Can enter shipping details and pay for products via Stripe.
15. Order & Order Confirmation Email - The user's order is created and an email is sent to the email address they've provided, giving the details of the order.
16. Profile - A prefilled form for the user to update their address details as well as a history or the user's orders (links can redirect user to individual order details).
17. Reviewing - Reviews are added from Products page. User chooses a rating from a dropdown menu and provides feedback in a textbox provided. Username, time of creation, product ID and "visible" automatically added.
18. Editing & Deleting Review - If the logged in user matches the author of a review, the option to edit or delete the review is displayed to the top right of the review.
19. Adding a Product - If Logged in and Store Owner - Can add product via Product Management link. Redirected to Add Product page. Provide product name, description, price, choose theme, metal and category from dropdown menus and upload an image to the site.
20. Editing & Deleting a Product - If Logged in and Store Owner - Can edit or delete product from Products page. Editing redirects to Editing Product page where a form is prefilled with the product's current information. Can change info and submit form to update.
21. Adding Discounts - If Logged in and Store Owner - Can create a discount for users with the Bonus model (bag App) from django admin url. Details include: name, if currently active, expriy date, description of discount, amount of discount, date created.

### Future Features
1. Engraving - In the Products Model, there is a "can_engrave" key which will be used in future versions to allow the user the option to submit a small piece of text to be engraved on the appropriate pieces.
2. Hiding Reviews - In the Review Model, a "visible" key will be used in future to enable the store owner to "hide" any unwanted or inappropriate reviews.

## Apps and Models
The developed apps for the current version of the store are as follows:
- your_tale_jewellery (primary app)
- home
- products
- bag
- checkout
- profiles

### Models in products App
#### Category
- name = models.CharField(max_length=254)
- friendly_name = models.CharField(max_length=254, null=True, blank=True)

#### Metal
- name = models.CharField(max_length=254)
- friendly_name = models.CharField(max_length=254, null=True, blank=True)

#### Theme
- name = models.CharField(max_length=254)
- friendly_name = models.CharField(max_length=254, null=True, blank=True)

#### Rating
- name = models.CharField(max_length=2, null=True)
- rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

#### Product
- category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
- metal = models.ForeignKey('Metal', null=True, blank=True, on_delete=models.SET_NULL)
- theme = models.ForeignKey('Theme', null=True, blank=True, on_delete=models.SET_NULL)
- sku = models.CharField(max_length=254, null=True, blank=True)
- name = models.CharField(max_length=254)
- description = models.TextField()
- has_sizes = models.BooleanField(default=False, null=True, blank=True)
- can_engrave = models.BooleanField(default=False, null=True, blank=True)
- price = models.DecimalField(max_digits=6, decimal_places=2)
- image = models.ImageField(null=True, blank=True)

#### Review
- review_number = models.CharField(max_length=32, null=True, editable=False)
- user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
- product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
- description = models.CharField(max_length=512)
- rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='reviews')
- created_at = models.DateTimeField(auto_now_add=True)
- visible = models.BooleanField(default=True, null=True, blank=True)


### Models in bag App
#### Bonus
- name = models.CharField(max_length=50)
- is_active = models.BooleanField(default=False)
- expires_on = models.DateField()
- description = models.CharField(help_text="Describes what the amount is for on a discount by discount basis.", max_length=256)
- amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
- created_at = models.DateTimeField(auto_now_add=True)


### Models in checkout App
#### Order
- order_number = models.CharField(max_length=32, null=False, editable=False)
- user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='orders')
- full_name = models.CharField(max_length=50, null=False, blank=False)
- email = models.EmailField(max_length=254, null=False, blank=False)
- phone_number = models.CharField(max_length=20, null=False, blank=False)
- country = CountryField(blank_label='Country *', null=False, blank=False)
- postcode = models.CharField(max_length=20, null=True, blank=True)
- town_or_city = models.CharField(max_length=40, null=False, blank=False)
- street_address1 = models.CharField(max_length=80, null=False, blank=False)
- street_address2 = models.CharField(max_length=80, null=True, blank=True)
- county = models.CharField(max_length=80, null=True, blank=True)
- date = models.DateTimeField(auto_now_add=True)
- delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
- order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
- grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
- original_bag = models.TextField(null=False, blank=False, default='')
- stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

#### OrderLineItem
- order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
- product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
- product_size = models.CharField(max_length=4, null=True, blank=True)
- quantity = models.IntegerField(null=False, blank=False, default=0)
- lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


### Models in profiles App
#### UserProfile
- user = models.OneToOneField(User, on_delete=models.CASCADE)
- default_phone_number = models.CharField(max_length=20, null=True, blank=True)
- default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
- default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
- default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
- default_county = models.CharField(max_length=80, null=True, blank=True)
- default_postcode = models.CharField(max_length=20, null=True, blank=True)
- default_country = CountryField(blank_label='Country', null=True, blank=True)


## Testing
### Validation
The html files were validated using https://validator.w3.org/.
The only errors displayed were due to the lines containing Jinja syntax. All other code was valid.

Css files were validated using https://jigsaw.w3.org/css-validator/#validate_by_input.



### Manual Testing
Manual testing was carried out on:
- Home page Shop Now button - Products page successfully loaded
- Sorting Products by price - both High to Low and Low to High working
- Filtering products by metals, categories and themes - all filtering successful
- Search term in search bar - searched for "ring" - results were of 8 products, including earrings (proved term was also being searched for within words)
- Registered for account - successfully loaded all pages and email with confirmation link was sent to inbox
- Confirming account - the link in the email was clicked on and the confirmation link successfully loaded and email was marked as confirmed in database
- Logging in and out - both logging in and out of an account work successfully
- Reviewing a product - Review page loads successfully and submitting the form successfully adds a review to the database and shows when the product detail page reloads.
- Editing product review -  Previous information successfuly populates the editing form and submitting the form overwrites the original information - confirmed on product details page and the admin url
- Deleting product review - Successfully removes review from database and product detail page
- Removing the discount from the database - All pages still load and the bag and checkout totals function as expected.
- Testing Stripe payment using test card details - Checkout success page loaded and order displayed in order history section on profile
- Testing Stripe payment using test card details and commenting out form submission - Checkout success page still loaded and order displayed in order history section on profile
- Webhooks - testing webhooks for https://your-tale-jewellery.herokuapp.com/checkout/wh/ was successful
- Adding products - Adding with/without product image, successfully adds the product details to the database and displays in the product page.
- Editing products - Previous information successfuly populates the editing form and submitting the form overwrites the original information - confirmed on product details page and the admin url
- Deleting product - Successfully removes product from database and product page


### Automatic Testing
Automatic testing was not carried out prior to deployment due to time constraints. But preferrably many of the tests above would be carried out automatically.

## Deployment of Website
This webiste was developed using gitpod and stored in a repository on Github. Gitpod was installed as an extension tool on google Chrome, which was accessed then via the project's repository page on Github. This allowed for regular version control updates:

1. git add . was entered into the command line interface to add files to the staging area.
2. git commit -m "" committed the files to the repository.
3. git push -u origin master pushed the master branch.

The website was deployed using Heroku. To do this, a Procfile was created 
with the content "web: python app.py". A requirements.txt file was created 
and "$ pip freeze > requirements.txt" was used to populate the file. The 
app was set to automatic delpoyment, whereby the github repository was 
linked to the heroku app. Environment variables (
AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS,
EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, USE_AWS) 
were set in Heroku Settings.

Amazon Web Services was used to host the static files for the website.

The following is the link to the deployed app:
https://your-tale-jewellery.herokuapp.com/

## Technology
1. GitHub repositories were used to store the files.
2. Gitpod was the editing environment used to create and edit files.
3. Bootstrap 4.4.1 was used for th grid system and other styling features.
4. Font Awesome was used for icons.
5. The photo on the home page was taken using a Oneplus 6T phone and edited using the phone's build-in photo software.
6. Google Fonts was used to provide the fonts.
7. Colors was used to generate a color palette.
8. W3C CSS Validator was used to validate all css files.
9. W3C Markup Validator was used to validate all html files.
10. HTML Formatter was used to format the following files: base.html, create.html, edit_work.html, favourites.html, login.html, profile.html, register.html, view_work.html and works.html.
11. JQuery was used.
12. The fullstack frame used was Django.
13. The website was deployed using Heroku and the static files were stored on Amazon Web Services.
14. Stripe was used for the payment function on the site.


## Credit
- Thanks to Reuben Ferrante for advising as mentor on this project.
- Much of the code in this project was obtained from Code Institute's "Boutique Ado Project" tutorials.
- Product images borrowed from amazon.co.uk (for education purposes)
