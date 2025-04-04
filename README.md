
# Ecommerce Website

This is a demo website for an online shop with a wild variaty of abilities for owner, staff, and customers. We will publish the demo link that you can see it via the link in demo section. For now, checkout the screenshots section for some views. 


## Authors

- [@Macan Mehri](https://www.github.com/macanMehri)


## Run Locally

Clone the project

```bash
  git clone https://github.com/macanMehri/ecommerce.git
```

Go to the project directory

```bash
  cd ecommerce
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the program

```bash
  python manage.py runserver
```


## Environment Variables

To run this project, you will need to add the following environment variables to your sample_settings.py and rename it to local_settings.py

`SECRET_KEY = ''`

`ALLOWED_HOSTS = [*]`

`DATABASE = {
    'NAME': 'db name',
    'USER': 'db user',
    'PASSWORD': 'db pass',
    'HOST': 'db host',
    'PORT': db port,
}`

`ADMIN_PATH = 'Your admin url path'`

## Features

Customers 
- Create an account and login.
- Change username, password, and email.
- Add review to products.
- Search for products and categories.
- Add product to your basket.
- Check your receipt and change the total number of orders.
- See your previous purchases and the total amount spent.
- Add address with different titles. for example : Home - Office

Owner
- Manage users and staff.
- Make a user to be staff or remove it.
- Check and manage reviews and active or deactivate them.
- Have full permission

Staff
- Add, edit, or delete a product.
- Add, edit, or delete an insurance.
- Add, edit, or delete a category.
- Have a control panel for ease of use.
- Assign picture to products or delete them.
## Tech Stack

**Client:** HTML, CSS, JS

**Server:** Python, Django, PostgreSql


## Appendix

We are looking to add new options to this website. 


## Screenshots

![Screenshot (8)](https://github.com/user-attachments/assets/a228264c-18f1-492c-bd25-a2a191ac331a)

![Screenshot (9)](https://github.com/user-attachments/assets/dd657ee7-8473-4654-98b0-63224e0f032d)

## DEMO

[![Watch the video](https://github.com/user-attachments/assets/b929b78d-e6c5-40eb-90ff-0fb73a7a78e5)
