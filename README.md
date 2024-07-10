## Project Introduction

The management panel for **Ghatre Charity**

## Development Guide

-   Python virtual environment (Optional)

    -   Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

    -   Activate the venv:

    ```bash
    source venv/bin/activate
    ```

    -   Deactivate the venv:

    ```bash
    deactivate
    ```

    -   Remove the venv:

    ```bash
    rm -rf venv
    ```

-   Install project requirements:

    ```bash
    pip install -r requirements.txt
    ```

-   Run app server:

    ```bash
    python manage.py runserver
    ```

-   Django migrations:

    -   Create migrations:

    ```bash
    python manage.py makemigrations
    ```

    -   Apply migrations to the database:

    ```bash
    python manage.py migrate
    ```

-   Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

-   Compiling message files:

    ```bash
    django-admin compilemessages
    ```
