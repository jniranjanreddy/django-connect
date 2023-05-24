## Working with uwsgi
```
yum groupinstall "Development Tools"
sudo yum install python3-devel
yum install gcc
pip install uwsgi

(django-connect) [root@chop-rh8-01 first_project]# pwd
/tmp/django-connect/first_project

(django-connect) [root@chop-rh8-01 first_project]# ls
db.sqlite3  django_connect  first_project  manage.py  test.py

(django-connect) [root@chop-rh8-01 first_project]# cat test.py
def application(env,start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

(django-connect) [root@chop-rh8-01 first_project]# uwsgi --http :8000 --wsgi-file test.py
*** Starting uWSGI 2.0.21 (64bit) on [Wed May 24 17:24:41 2023] ***
compiled with version: 8.5.0 20210514 (Red Hat 8.5.0-4) on 24 May 2023 11:41:00
os: Linux-4.18.0-348.7.1.el8_5.x86_64 #1 SMP Wed Dec 22 13:25:12 UTC 2021
nodename: chop-rh8-01.jnrit.com
machine: x86_64
clock source: unix ...
```
