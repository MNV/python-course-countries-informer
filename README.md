# Country Directory

Console application for getting up-to-date information about countries.

The application allows you to receive from open sources and save to the files information about countries and provide it to the user.

## Installation

Clone the repository to your computer:
```bash
git clone https://github.com/StinkyPeterson/python-course-countries-informer.git
```

### Requirements:

Install the appropriate software:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).

## Usage

1. To configure the application copy `.env.sample` into `.env` file:
    ```shell
    cp .env.sample .env
    ```
   
    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values. 
    So it can be configured depending on the environment.

    To access the API, visit the appropriate resources and obtain an access token:
    - APILayer – Geography API (https://apilayer.com/marketplace/geo-api)
    - OpenWeather – Weather Free Plan (https://openweathermap.org/price#weather)
    - NewsAPI - News API (https://newsapi.org/register)
   
    Set received access tokens as environment variable values (in `.env` file):
    - `API_KEY_APILAYER` – for APILayer access token
    - `API_KEY_OPENWEATHER` – for OpenWeather access token
    - `API_KEY_NEWSAPI` - for NewsAPI access token

2. Build the container using Docker Compose:
    ```shell
    docker compose build
    ```
    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.
   
3. To start the application run:
    ```shell
    docker compose up
    ```
    When containers are up server starts at http://0.0.0.0:8020. You can open it in your browser.
   
   

### Automation commands

The project contains a special `Makefile` that provides shortcuts for a set of commands:
1. Build the Docker container:
    ```shell
    make build
    ```

2. Generate Sphinx documentation run:
    ```shell
    make docs-html
    ```

3. Autoformat source code:
    ```shell
    make format
    ```

4. Static analysis (linters):
    ```shell
    make lint
    ```

5. Autotests:
    ```shell
    make test
    ```

    The test coverage report will be located at `src/htmlcov/index.html`. 
    So you can estimate the quality of automated test coverage.

6. Run autoformat, linters and tests in one command:
    ```shell
    make all
    ```

Run these commands from the source directory where `Makefile` is located.

## Documentation

The project integrated with the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation engine. 
It allows the creation of documentation from source code. 
So the source code should contain docstrings in [reStructuredText](https://docutils.sourceforge.io/rst.html) format.

To create HTML documentation run this command from the source directory where `Makefile` is located:
```shell
make docs-html
```

After generation documentation can be opened from a file `docs/build/html/index.html`.
