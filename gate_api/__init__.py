# coding: utf-8

# flake8: noqa

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "4.11.2"

# import apis into sdk package
from gate_api.api.futures_api import FuturesApi
from gate_api.api.margin_api import MarginApi
from gate_api.api.spot_api import SpotApi
from gate_api.api.wallet_api import WalletApi

# import ApiClient
from gate_api.api_client import ApiClient
from gate_api.configuration import Configuration
# import models into sdk package
from gate_api.models.batch_order import BatchOrder
from gate_api.models.cancel_order import CancelOrder
from gate_api.models.cancel_order_result import CancelOrderResult
from gate_api.models.contract import Contract
from gate_api.models.currency_pair import CurrencyPair
from gate_api.models.funding_account import FundingAccount
from gate_api.models.funding_book_item import FundingBookItem
from gate_api.models.funding_rate_record import FundingRateRecord
from gate_api.models.futures_account import FuturesAccount
from gate_api.models.futures_account_book import FuturesAccountBook
from gate_api.models.futures_candlestick import FuturesCandlestick
from gate_api.models.futures_initial_order import FuturesInitialOrder
from gate_api.models.futures_liquidate import FuturesLiquidate
from gate_api.models.futures_order import FuturesOrder
from gate_api.models.futures_order_book import FuturesOrderBook
from gate_api.models.futures_order_book_item import FuturesOrderBookItem
from gate_api.models.futures_price_trigger import FuturesPriceTrigger
from gate_api.models.futures_price_triggered_order import FuturesPriceTriggeredOrder
from gate_api.models.futures_ticker import FuturesTicker
from gate_api.models.futures_trade import FuturesTrade
from gate_api.models.insurance_record import InsuranceRecord
from gate_api.models.loan import Loan
from gate_api.models.loan_patch import LoanPatch
from gate_api.models.loan_record import LoanRecord
from gate_api.models.margin_account import MarginAccount
from gate_api.models.margin_account_currency import MarginAccountCurrency
from gate_api.models.margin_currency_pair import MarginCurrencyPair
from gate_api.models.my_futures_trade import MyFuturesTrade
from gate_api.models.order import Order
from gate_api.models.order_book import OrderBook
from gate_api.models.position import Position
from gate_api.models.position_close import PositionClose
from gate_api.models.position_close_order import PositionCloseOrder
from gate_api.models.repay_request import RepayRequest
from gate_api.models.repayment import Repayment
from gate_api.models.spot_account import SpotAccount
from gate_api.models.ticker import Ticker
from gate_api.models.trade import Trade
from gate_api.models.transfer import Transfer
from gate_api.models.trigger_order_response import TriggerOrderResponse
