# django-insights-v1

## Install

```bash
create virtual envoirnment: python3 -m venv .venv
activate: source .venv/bin/activate
#for deactivate: deactivate
install django: python3 -m pip install Django

python3
import django
print(django.get_version());
#will show the version
quit()
#will quit the python
start projetc: django-admin startproject project_V1
cd project_V1
python3 manage.py runserver 9000
```

## Migration

```bash
#run migrations:
python3 manage.py migrate
#create migration:
python3 manage.py makemigrations

```

## ORM:

```bash
#initialise the shell
python3 manage.py shell
#import post model:
from customAppPosts.models import Post
p = Post() # will create new instance
p
#<Post: Post object (None)>
p.title = "My first post!"
p.save()
exit()
```

## Admin

```bash
python3 manage.py createsuperuser
User: Admin
Email: admin
Pass: standared

```
