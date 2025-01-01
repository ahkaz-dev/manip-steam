
# Steam library-manipulator

A simple sheet of your games for personal use

## Getting Started

You will need to either clone or download this repository to your machine as below:

```bash
git clone https://github.com/ahkaz-dev/manip-steam
```

## Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv env
```
Activate the virtual environment:

- For Windows:
    ```bash
    .env\Scripts\activate
    ```
- For macOS/Linux:
    ```bash
    source .env/bin/activate
    ```
## Dependencies

Install all the requirements:

```bash
pip install -r requirements.txt
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`api_key`

- Use Steam Community to activate your API key. [Direct link](https://steamcommunity.com/dev/apikey)

`id_key`
- To find your Steam ID, visit the [following link](https://store.steampowered.com/account/)

## Running the App
Use for local data storage:
```bash
py manage.py migrate
```

Run the main script:
```bash
py manage.py runserver
```
## License
This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
