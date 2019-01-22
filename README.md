# Django Rest Framework Nested URL parameters dispatcher sample
This is a small sample how I use the nested parameters with URL dispatcher with Django Rest Framwork

## Setup 
Please, create your _virtualenv_ and install the packages:

```shell
$ virtualenv -p `which python3` [your_env_name]
... some command output ...
$ source [your_env_path]/bin/activate
(env) $ cd [your_project_folder]
(env) $ git clone git@github.com:PatrickMello/sample_drf_nested_url.git
(env) $ cd sample_drf_nested_url
(env) $ pip install -r requirements
.. some command output ...
```


If you does not have any errors, let's run the project:
```shell
(env) $ ./manage.py migrate
.. some command output ... 
(env) $ ./manage.py createsuperuser
... provide the requested information ...
(env) $ ./manage.py runserver
```


## Some tests

To create a new blog entry, just run:
```shell
$ curl -X POST \
    -H 'Content-type: application/json' \
    -d '{
        "title": "My first blog entry",
        "content": "Hoorray!! That's work!"
    }' \
    http://localhost:8000/core/entries | jq

... more command output ...

$ curl -X POST \
    -H 'Content-type: application/json' \
    -d '{
        "title": "Oh! That's a second simple entry",
        "content": "Hoorray!! That's work too!"
    }' \
    http://localhost:8000/core/entries | jq
```


To create a comment with nested URL, just run:
```shell
curl -X POST \
    -H 'Content-type: application/json' \
    -d '{
        "comment": "Oh great! My first comment!"
    }' \
    http://localhost:8000/core/entry/2/comments | jq

... more some command output ... 
```

Also, you can update a comment as same way:

```shell
$ curl -X PUT \
    -H 'Content-type: application/json' \
    -d '{
        "comment": "Oh great! My first comment was edited!!"
    }' \
    http://localhost:8000/core/entry/2/comment/1 | jq

... more some command output ... 

```

:scream:

Enjoy!




