py -3 -m pip install --upgrade pip
py -3 -m venv venv1
call venv1\Scripts\activate
pip install -r requirements.txt
py -3 ftl_site/manage.py check
py -3 ftl_site/manage.py makemigrations ftl_app
py -3 ftl_site/manage.py sqlmigrate ftl_app 0001
py -3 ftl_site/manage.py migrate
py -3 ftl_site/manage.py runserver