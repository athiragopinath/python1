mkdir chat
cd chat
python -m venv myvenv
myvenv/Scripts/activate
pip install --upgrade pip
pip instal django~=1.11.0
django-admin.exe startproject mysite
cd mysite
django-admin startapp chatapp
cd ..
python manage.py migrate
python manage.py runserver
