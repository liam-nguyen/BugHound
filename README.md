<center> <h1> BugHound </h1>

Bughound is a web-based bug recording and tracking software product

</center>

## Key Features

---

- Using web browser, create, edit and update “bug” reports on multiple products
- Store error report content in relational tables
- Access error report content via SQL
- Search for bugs on multiple fields
- Facilities to add, delete or update information on program, releases, functional areas, employee

## Requirements

---

- [Django 3](https://docs.djangoproject.com/en/3.0/intro/install/)

### To use django in virtualenv

- Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
- Create a virtualenv:
  - Add conda-forge as a source for dependency

```{.python}
conda config --add channels conda-forge
conda config --set channel_priority flexible

```

- Create environment from yaml file

```{.python}
conda create --name [environment name] --file requirements_conda.yml
```

- Start virtualenv:

```{.python}
conda activate [environment name]
```

- Run this shell script to get initial database with dummy data

```
./DEMO_PART_2.sh
```

- To start server (in conda environment)
  - Navigate to project folder
  - Run

```{.python}

python manage.py runserver
```

- To exit from conda environment

```{.python}
conda deactivate
```
