Sync dependencies with <br>
`pip install pip-tools` <br>
`pip-compile --output-file requirements.txt requirements.in` <br>


DB setup <br>
`sudo apt install postgresql postgresql-contrib` <br>
`sudo -iu postgres` <br>
`psql` <br>
`create user django with encrypted password 'django';` <br>
`create database django;` <br>
`grant all privileges on database django to django;` <br>
`alter user django createdb;` <br>