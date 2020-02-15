# RobinhoodTrader

Python3 interface with the Robinhood API to trade stocks and cryptocurrencies.

## Installation

To install RobinhoodTrader, download or clone this repository.

### Create virtual environment

In a terminal or command line, navigate to the RobinhoodTrader directory.
Create a Python3 virtual environment (this example uses virtualenvwrapper,
which you can install with ```pip install virtualenvwrapper``` on Unix systems
or ```pip install virtualenvwrapper-win``` on Windows):

```console
cd path/to/RobinhoodTrader
mkvirtualenv robinhood
```

Then install the Python requirements:

```console
pip install -r requirements.txt
```

Finally, install RobinhoodTrader:

```console
cd RobinhoodTrader
pip install .
```

## Related

This module is based on:

* [LichAmnesia's Robinhood module](https://github.com/LichAmnesia/Robinhood) that was based on [Jamonek's original version](https://github.com/Jamonek/Robinhood).
* [wang-ye's robinhood-crypto](https://github.com/wang-ye/robinhood-crypto) module.
