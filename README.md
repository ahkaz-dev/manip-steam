
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
    env\Scripts\activate
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
## Data storage and admin
Use the command:
```bash
py manage.py createsuperuser
```
Following the instructions, enter your data into the console

**Username**: `MyLogin` **Email address**:  `press enter for skip email`
**Password**:  `MyPassword` **Password (again)**:  `MyPassword`

You will see a message that the creation was successful

## Check data
Go to the admin page: `/admin`.
Use the login and password that you entered for the **createsuperuser** command.

Select Games, and you will see all the games associated with your account.
You can also click on a single row to edit the data.

Click on `View site` to go to the home page.

## Screens
| Dashboard | 
|-----------------|
| ![Dashboard](https://raw.githubusercontent.com/ahkaz-dev/manip-steam/main/static/screens/screencapture-dashboard.png) |

| Select game | 
|-----------------|
| ![Select game](https://raw.githubusercontent.com/ahkaz-dev/manip-steam/main/static/screens/screencapture-select-game.png) |

## License
This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
