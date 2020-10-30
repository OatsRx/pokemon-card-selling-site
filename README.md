# Flamin Pidgey Trading Card Store 

[Project Demo](#) 
## Project Purpose
The purpose of this project is to allow the site manager (myself) to move away from 3rd party selling
websites to house my own store selling trading cards. 

## UX
The UX for this webapp uses Bootstrap, custom CSS and crispy_forms for overall styling and Structure

### Database Structure
The product and category fixtures were custom made for this project to reflect the stock of products that
I currently have in stock.

1. [Products](#)
2. [Categories](#)
3. [Models](#)

## Features

### Current Features
Current features of the app allow customers to purchase trading cards to delivery anywhere in the UK.

#### Products
As a user you have the ability to browse products by category, sort products by a variety of filters, search
for a specific product in the search bar and add them to a shopping basket.

#### Checkout
As a user you have the ability to add and remove products from your shopping bag and continue through to
as secure checkout powered by Stripe payment system. The user has the option to check out as a guest or
save their detail into a profile for future purcases.

#### User Profiles
Users have the option to save their details during a transaction to use in the future. Profile page also
shows a breakdown of previous purchases in an order history display. 

### Future Features
This webstore could benefit from an admin account. However I chose not to include this in this project 
as I will be the one managing the site. Given that I will be uploading products whole sets at a a time I 
will be implementing more fixtures and a diffrent database layout to accomodate for more variety of product 
categories. 

The store will also undergo styling changes before launch while keeping the current colour scheme.

## Technologies Used

### Languages
1. HTML
2. CSS
3. JavaScript
4. Python

### Libraries & Frameworks
1. Django
2. Stripe
3. Allauth
4. Bootstrap
5. Postgress

### Deployment
1. Heroku
2. AWS

#### Webhooks
The webhooks for this project were taken from the previous mini project and modified accordingly.

## Testing
The application has been tested by myself and friends to ensure that the core functions of the app work. These 
include; making an account, logging in, logging out, searching for products, filtering product searches, adding 
products to the shopping bag, removing products from the shopping back, completing a checkout form, accepting a Stripe
payment, order confirmation and review, saving customer details and orders. 

The custom CSS of the site will need a review soon as some elements are not aligned properly with each other and some
interfere with existing Boostrap styles. 

HTML, CSS, JavaScript and Python code have all been tested for formatting through their respective validators.

## Deployment
Source code for this application was sent to Github during development and linked to Heroku through a master branch
that automatically commits from GitHub with environment variables being added manually to Heroku. Through development the
app was deploying through GitPod on Opera and requires installation of the requirements.txt

## Credits
### Media
Images for majority of the store are from [Pokelletor](https://www.pokellector.com/)

### Special Thanks
Massive thanks to all of the CI tutors for all of there help. 


