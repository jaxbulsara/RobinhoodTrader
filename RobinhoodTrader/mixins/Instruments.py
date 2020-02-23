from __future__ import absolute_import
from ..endpoints import api
from ..RobinhoodSession import RobinhoodSession
from .PageSupport import PageSupport


class Instruments(PageSupport):
    session: RobinhoodSession

    def getFirstInstrumentPage(self):
        """
        Example Response Data:
        {   'next': 'https://api.robinhood.com/instruments/?cursor=cD0xNDgyNQ%3D%3D',
            'previous': None,
            'results': [   {   'bloomberg_unique': 'EQ0000000081810122',
                            'country': 'US',
                            'day_trade_ratio': '1.0000',
                            'default_collar_fraction': '0.05',
                            'fractional_tradability': 'untradable',
                            'fundamentals': 'https://api.robinhood.com/fundamentals/DMYTU/',
                            'id': '27c70cdf-4787-4577-91f0-27d0a5313182',
                            'list_date': '2020-02-21',
                            'maintenance_ratio': '1.0000',
                            'margin_initial_ratio': '1.0000',
                            'market': 'https://api.robinhood.com/markets/XNYS/',
                            'min_tick_size': None,
                            'name': 'DMY TECHNOLOGY GROUP INC',
                            'quote': 'https://api.robinhood.com/quotes/DMYTU/',
                            'rhs_tradability': 'untradable',
                            'simple_name': 'DMY Technology Units',
                            'splits': 'https://api.robinhood.com/instruments/27c70cdf-4787-4577-91f0-27d0a5313182/splits/',
                            'state': 'active',
                            'symbol': 'DMYTU',
                            'tradability': 'untradable',
                            'tradable_chain_id': None,
                            'tradeable': False,
                            'type': 'unit',
                            'url': 'https://api.robinhood.com/instruments/27c70cdf-4787-4577-91f0-27d0a5313182/'},
                                ...
                                ...
                                ...
                            {   'bloomberg_unique': 'EQ0000000080116435',
                            'country': 'US',
                            'day_trade_ratio': '0.2500',
                            'default_collar_fraction': '0.05',
                            'fractional_tradability': 'tradable',
                            'fundamentals': 'https://api.robinhood.com/fundamentals/REYN/',
                            'id': '4d3320d7-5ab7-4219-b051-a6808e032fd4',
                            'list_date': '2020-01-31',
                            'maintenance_ratio': '1.0000',
                            'margin_initial_ratio': '1.0000',
                            'market': 'https://api.robinhood.com/markets/XNAS/',
                            'min_tick_size': None,
                            'name': 'Reynolds Consumer Products Inc. Common Stock',
                            'quote': 'https://api.robinhood.com/quotes/REYN/',
                            'rhs_tradability': 'tradable',
                            'simple_name': 'Reynolds Consumer Products',
                            'splits': 'https://api.robinhood.com/instruments/4d3320d7-5ab7-4219-b051-a6808e032fd4/splits/',
                            'state': 'active',
                            'symbol': 'REYN',
                            'tradability': 'tradable',
                            'tradable_chain_id': '567bd37e-8a9a-40b7-9fd8-e30dc1e3ecbb',
                            'tradeable': True,
                            'type': 'stock',
                            'url': 'https://api.robinhood.com/instruments/4d3320d7-5ab7-4219-b051-a6808e032fd4/'}]}

        """

        response = self.session.get(api.instruments(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getInstrumentBySymbol(self, instrumentSymbol):
        """
        Example Response Data

        """

        response = self.session.get(
            api.instrumentBySymbol(instrumentSymbol), timeout=15
        )
        response.raise_for_status()
        data = response.json()

        return data

    def getInstrumentById(self, instrumentId):
        """
        Example Response Data

        """

        response = self.session.get(
            api.instrumentById(instrumentId), timeout=15
        )
        response.raise_for_status()
        data = response.json()

        return data

    def getInstrumentByUrl(self, instrumentUrl):
        """
        Example Response Data

        """

        response = self.session.get(instrumentUrl, timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

