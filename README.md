# Mates_Search
Simple dating website

## Requirements
python 3.8.**

Refer requirements.txt

## Installation

fork this repo


### 1.Create python virtual env

1.If your python version is already 3.8.**

```python3 -m env Venv```  

2.If you have multiple versions
 
 ```virtualenv Venv --python=python3.8```

### 2.Clone this repo

```cd Venv```

clone this repo

### 3.Activating virtual env

```source bin/activate```

### 4.Installing requirements

```cd Mates_Seacrh```

```pip install -r requirements.txt```

### 5.Installing requirements
```python manage.py makemigrations```

```python manage.py makemigrations mates```

```python manage.py migrate```


### 6.Start Django

```python manage.py runserver```

### 7.Open your browser on

```http://127.0.0.1:8000```

### As per assignment we are using Xampp

Make sure mysqlclient is installed

Note these changes on your settings.py 

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'Mates_Search',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5433', }
}
```
NB: If you are setting up the second time with new model CustomUser Delete All migrations first then run the commands on step 5
