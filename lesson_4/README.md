# Demo App for Lesson 4 GeekBrains

## Install 
1. Create new virtual env
```shell
python3 -m venv ./venv
```
2. copy `example.env` to `.env` and set `SECRET_KEY`
3. activate virtual env
```shell
source venv/bin/activate
```
4. install dependencies
```shell
pip install -r requirements.txt
```
5. Run command for init db and create user
```shell
flask db upgrade
flask create-init-user
```
6. Run flask application
```shell
flask run
```