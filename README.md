<center> <h1> BugHound </h1>

Bughound is a web-based bug recording and tracking software product

</center>

## Key Features

---

- Using web browser, create, edit and update “bug” reports on multiple products
- Store error report content in relational tables
- Access error report content via SQL•Search for bugs on multiple fields
- Facilities to add, delete or update information on program, releases, functional areas, employee

## Requirements

---

- [Django 3](https://docs.djangoproject.com/en/3.0/intro/install/)

### To use django in virtualenv

- Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
- Create a virtualenv:

```{.python}
conda create --name [environment name] --file requirements_conda.yml
```

- To start virtualenv:

```{.python}
conda activate [environment name]
```

- To start server
  - Navigate to project folder
  - Run

```{.python}
python manage.py runserver
```

- To exit from virtualenv

```{.python}
conda deactivate
```
