# RobinhoodTrader

Python3 interface with the Robinhood API to trade stocks and cryptocurrencies.

## Installation

To install RobinhoodTrader, download or clone this repository.

In a terminal or command line console, navigate to the RobinhoodTrader root directory.
Create a Python3 virtual environment (this example uses virtualenvwrapper,
which you can install with ```pip install virtualenvwrapper``` on Unix systems
or ```pip install virtualenvwrapper-win``` on Windows):

```console
> cd path/to/RobinhoodTrader
> mkvirtualenv robinhood
```

Install the Python requirements:

```console
(robinhood)> pip install -r requirements.txt
```

Install RobinhoodTrader:

```console
(robinhood)> cd RobinhoodTrader
(robinhood)> pip install .
```

## Setup

Robinhood requires two factor authorization to use its private API.
You will need to enable Two-Factor Authentication in the Robinhood web application.
You can use either a QR code key or recieve a SMS text message with an authorization code.
Using the QR code is recommended because you can stay logged in indefinitely with it.
If you opt to use the SMS code, you will need to login to Robinhood with a new SMS code every 24 hours.

To use a QR code, log into the Robinhood web application.
Click on "Account" at the top right of the window.
Then click on "Settings" on the drop-down menu.
Click on "Security" in the left-hand sidebar or scroll down to the "Security" section.
Click on "Two-Factor Authentication".
Click the toggle switch labeled "Off".

You will be asked to choose an authentication method.
You can choose either "SMS" or "Authentication App".

- "SMS" will make you enter a code texted to you every time you log in with this module.
- "Authentication App" will give you a QR code that will be used to generate the authentication code.

Make your selection and click "Next".

If you selected "SMS", you will recieve a text on your phone.
Enter the code you recieved and click "Next".
No additional setup is required to use the SMS code.

If you selected "Authentication App", you will be shown a QR code to scan into an authentication app.
You can use Google Authenticator or your favorite authentication app to scan the QR code.
Setup the new authenticator in the app and make sure the app generates a 6-digit code every thirty seconds.
Then, click "Can't scan it?" and copy the 16 digit code into config.ini.
You can also write in your username and password into config.ini.

```ini
[login]
username = [Your username]
password = [Your password]
qrCode = [Your QR code]
```

Go back to Robinhood and click "Next".
Enter the code that is currently displayed in you authenticator app.
When RobinhoodTrader logs into Robinhood,
this code will generated from the QR code you copied above and the current time.

## Usage

RobinhoodTrader is a Python3 class that allows you to login to Robinhood and
trade stocks and cryptocurrencies.

### Login

To login, use the following code:

```python
# login.py
from RobinhoodTrader import RobinhoodTrader
trader = RobinhoodTrader()
trader.login()
```

```console
> workon robinhood
(robinhood)> python3 login.py
Username: {Type in username}
Password: {Type in password}
```

If you are using an SMS authentication code, you will need to type in the code you recieve:

```console
SMS Code: {Type in SMS code}
```

You are now logged in!
The ```RobinhoodTrader``` object will hold your session authentication information to keep you logged in.
