
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

## Features & Permissions

Customers 
- Create an account and login.
- Change username, password, and email.
- Add review to products.
- Send picture of received product.
- Search for products and categories.
- Add product to your basket.
- Check your receipt and change the total number of orders.
- See your previous purchases and the total amount that has been spent.
- Add address with different titles. for example : Home - Office
- Enable to send text messages to the support team.

Owner
- Manage users and staff.
- Make a user to be staff or remove it.
- Check and manage reviews and active or deactivate them.
- Check and manage sent pictures of products and active or deactivate them.
- Enable to see different charts of purchases. (totally or just for a specific product)
- Have full permission.
- Have availabilities as much as staff.

Staff
- Add, edit, or delete a product.
- Add, edit, or delete an insurance.
- Add, edit, or delete a category.
- Have a control panel for ease of use.
- Assign picture to products or delete them.
- Able to answer users sent messages.

Website
- Connect a user to an admin.
- Calculate the total spent money in this website in the current year.
- Calculate the number of products that has been bought in this website in the current year.
- Unable users to send multiple messages in a row.
- Unable users to send multiple pictures for a product.
- Unable users to add multiple reviews for a product.

## Tech Stack

**Client:** HTML, CSS, JS

**Server:** Python, Django, PostgreSql


## Appendix

We are looking to add new options to this website. 


## Screenshots

![Image](https://github.com/user-attachments/assets/99ffbdab-3197-408c-97de-c8676e245c25)
![Image](https://github.com/user-attachments/assets/d4601e33-d849-4e99-a4df-c96218a8ed57)
![Image](https://github.com/user-attachments/assets/e10443a3-e2de-496d-800e-688056810b63)

## DEMO

Coming Soon...