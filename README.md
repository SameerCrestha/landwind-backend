## Setup

The first thing to do is to clone the repository:

```sh {"id":"01HXZX0XCFN1DVAD016BD2NKZT"}
$ git clone https://github.com/SameerCrestha/tailwind-backend.git
$ cd tailwind-backend

```

Create a virtual environment to install dependencies in and activate it:

```sh {"id":"01HXZX0XCG1PQ0W4ECPXYRESRE"}
$ virtualenv venv
$ source venv/bin/activate

```

Then install the dependencies:

```sh {"id":"01HXZX0XCG1PQ0W4ECQ0R0Y1ZG"}
(env)$ pip install -r requirements.txt

```

Once `pip` has finished downloading the dependencies:

```sh {"id":"01HXZX0XCG1PQ0W4ECQ2RHT83Y"}
(env)$ cd project
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver

```

Server will be available at: `http://127.0.0.1:8000/`.
Get packages data at: `http://127.0.0.1:8000/api/packages`.

Go to `http://127.0.0.1:8000/admin` to add packages.