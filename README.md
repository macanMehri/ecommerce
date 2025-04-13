
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
- Enable to see charts of purchases.
- Have full permission.
- Have availability as much as staff.

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

![Image](https://github.com/user-attachments/assets/76f57b47-192a-42b0-804f-83db8fe9916a)

![Image](https://github.com/user-attachments/assets/b0b720e9-1d3b-4701-8625-61146a28c8a9)

## DEMO

![Demo video](https://github.com/user-attachments/assets/b929b78d-e6c5-40eb-90ff-0fb73a7a78e5)
