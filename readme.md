**Sync dependencies** <br>
`pip install pip-tools` <br>
`pip-compile --output-file requirements.txt requirements.in` <br>

<br>

**DB setup** <br>
`sudo apt install postgresql postgresql-contrib python3-psycopg2` <br>
`sudo -iu postgres` <br>
`psql` <br>
`create user django with encrypted password 'django';` <br>
`create database django;` <br>
`grant all privileges on database django to django;` <br>
`alter user django createdb;` <br>

<br>

**Pre commit setup** <br>
`pip install pre-commit` <br>
`pre-commit install` <br>


**Compile static** <br>
`./manage.py collectstatic --noinput`