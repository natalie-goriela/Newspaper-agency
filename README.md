NEWSPAPER AGENT is a project designed to help a team of redactors to organize their work on creating 
articles for different newspapers.
Redactors are able to register on the site and have their own personal profile page, 
which is only accessible to authenticated users of the site. This personal page allows redactors 
to showcase their work and provide background information about themselves.

Redactors have exclusive access to create, update, and delete their own articles.
However, all users of the site, including non-registered users, are able to read the articles.

The website includes a variety of topics for articles, which are listed on a separate page for easy navigation. 
By clicking on a single topic, all relevant articles associated with that topic will be displayed.

To run this projects locally, use the following steps:

1. Clone repo from GIT:

`git clone git@github.com:natalie-goriela/to-do-list.git`

2. If you are using PyCharm - it may propose you to automatically create venv for your project 
and install requirements in it, but if not: 

```python
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
   
The secret key to this project is saved within .env file, which is hidden.
You can create your own `.env` file to store your `SECRET_KEY`, `DB_NAME` and other environment 
variables like it is shown in `.env_sample` file. 

After running migrations, use the following command to load prepared data from fixture:
  
`python manage.py loaddata newspaper_agency_db_data.json`

Upon loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.admin`
  - Password: `1qazcde3`

Feel free to add more data using admin panel, if needed.
