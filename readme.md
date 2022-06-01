**Sync dependencies** <br>
`pip install pip-tools` <br>
For prod use <br>
`pip-compile --output-file requirements.txt requirements.in` <br>
For dev use <br>
`pip-compile --output-file requirements-dev.txt requirements-dev.in` <br>

<br>

**DB setup**

**Ubuntu/Fedora**

`sudo [apt/yum] install postgresql postgresql-contrib python3-psycopg2` <br>

[Fedora start] <br>
`sudo yum install -y postgresql-server postgresql-contrib` <br>
`sudo postgresql-setup initdb` <br>
`sudo systemctl start postgresql` <br>
`sudo systemctl enable postgresql` <br>
[Fedora ends]

`sudo -iu postgres` <br>
`psql` <br>
`create user django with encrypted password 'django';` <br>
`create database django;` <br>
`grant all privileges on database django to django;` <br>
`alter user django createdb;` <br>

<br>

**For macOS**

`brew install postgres`
`brew services start postgres`
`createdb `whoami``
`createuser -s postgres`

https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3

<br>

**Pre commit setup** <br>
`pip install pre-commit` <br>
`pre-commit install` <br>


**Compile static** <br>
`./manage.py collectstatic --noinput`
