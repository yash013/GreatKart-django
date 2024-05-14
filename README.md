# Setup Instructions

1. Clone the repository `git clone https://github.com/yash013/GreatKart-django.git`
2. Navigrate to the working directory `cd GreatKart-django`
3. Open the project from the code editor `code .` or `atom .`
4. Create virtual environment `python -m venv env`
5. Activate the virtual environment `source env/Scripts/activate`
6. Install required packages to run the project `pip install -r requirements.txt`
7. Fill up the environment variables:
    _Generate your own Secret key using this tool [https://djecrety.ir/](https://djecrety.ir/), copy and paste the secret key in the SECRET_KEY field._

    _Your configuration should look something like this:_
    ```sh
    SECRET_KEY=47d)n05#ei0rg4#)*@fuhc%$5+0n(t%jgxg$)!1pkegsi*l4c%
    DEBUG=True
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=youremailaddress@gmail.com
    EMAIL_HOST_PASSWORD=yourStrongPassword
    EMAIL_USE_TLS=True
    ```
    _Note: If you are using gmail account, make sure to [use app password](https://support.google.com/accounts/answer/185833)_
8. Create database tables
    ```sh
    python manage.py migrate
    ```
9. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
10. Run server
    ```sh
    python manage.py runserver
    ```
