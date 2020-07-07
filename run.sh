sudo python3 -m pip install --upgrade pip
python3 -m venv ../venv1
source ../venv1/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
python3 ftl_app/manage.py check
python3 ftl_app/manage.py makemigrations ftl_app
python3 ftl_app/manage.py sqlmigrate ftl_app 0001
python3 ftl_app/manage.py migrate
python3 ftl_app/manage.py runserver