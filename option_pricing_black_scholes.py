#!/usr/bin/python3
"""
---------------------------------------------------------------------------------
                            OPTIONS CALCULATOR
---------------------------------------------------------------------------------

The Black-Scholes model for European-style Options on non-dividend paying stocks.

|
| Input parameter(s):   S, K, DTE, IV, r
|                       eg. 65.0, 60.0, 30.0, 35.0, 2.493
|

Options Pricing Parameters
--------------------------
S: Stock Price
K: Strike Price
DTE: Days to Expiration
IV: Implied Volatility (%)
r: Risk-free Rate (%)

Remark: Input parameters must be separated by comma(s).

---------------------------------------------------------------------------------
"""

import math as m
from scipy.stats import norm as nd


class InvalidDataError(Exception):
    pass
    

class OptionPricing(object):
    def __init__(self, stock_price, strike_price, time_to_exp_days, \
                annual_vol_pc, risk_free_rate_pc):

        self.S = stock_price
        self.K = strike_price
        self.t = time_to_exp_days
        self.v = annual_vol_pc
        self.r = risk_free_rate_pc

        # check input
        CONDITIONS = [
                        self.S <= 0.0,
                        self.K <= 0.0,
                        self.t <= 0.0,
                        self.v <= 0.0,
                        self.r < 0.0
                    ]
        if any(CONDITIONS):
            raise InvalidDataError("[Error] Input parameter(s) out of range")

        self.t_yrs = time_to_exp_days / 365
        self.v_dec = annual_vol_pc / 100
        self.r_dec = risk_free_rate_pc / 100

        self.d = (m.log(self.S / self.K) + (self.r_dec + self.v_dec ** 2 / 2) * \
                self.t_yrs) / (self.v_dec * m.sqrt(self.t_yrs))

        self.X1 = self.K * m.exp(-self.r_dec * self.t_yrs)
        self.X2c = nd.cdf(self.d - self.v_dec * m.sqrt(self.t_yrs))
        self.X2p = nd.cdf(self.v_dec * m.sqrt(self.t_yrs) - self.d)

    def call_price(self):
        X0c = self.S * nd.cdf(self.d)
        callprice = round(X0c - self.X1 * self.X2c, 2)
        return callprice

    def put_price(self):
        X0p = -self.S * nd.cdf(-self.d)
        putprice = round(X0p + self.X1 * self.X2p, 2)
        return putprice


class OptionGreeks(OptionPricing):
    """The sensitivities of the Black-Scholes Model"""

    def __init__(self, stock_price, strike_price, time_to_exp_days, \
                annual_vol_pc, risk_free_rate_pc):
        OptionPricing.__init__(self, stock_price, strike_price, time_to_exp_days, \
                                annual_vol_pc, risk_free_rate_pc)

        self.Xt0 = -self.S * self.v_dec * nd.pdf(self.d) / (2 * m.sqrt(self.t_yrs))
        self.Xt1 = self.r_dec * self.K * m.exp(-self.r_dec * self.t_yrs)
        self.Xr0 = self.t_yrs * self.K * m.exp(-self.r_dec * self.t_yrs)

    def call_delta(self):
        calldelta = round(nd.cdf(self.d), 4)
        return calldelta

    def put_delta(self):
        putdelta = round(-nd.cdf(-self.d), 4)
        return putdelta

    def call_gamma(self):
        callgamma = round(nd.pdf(self.d) / (self.S * self.v_dec * m.sqrt(self.t_yrs)), 4)
        return callgamma

    def put_gamma(self):
        putgamma = self.call_gamma()
        return putgamma

    def call_theta(self):
        calltheta = round((self.Xt0 - self.Xt1 * self.X2c) / 365, 4)
        return calltheta

    def put_theta(self):
        puttheta = round((self.Xt0 + self.Xt1 * self.X2p) / 365, 4)
        return puttheta

    def call_vega(self):
        callvega = round((self.S * m.sqrt(self.t_yrs) * nd.pdf(self.d)) / 100, 4)
        return callvega

    def put_vega(self):
        putvega = self.call_vega()
        return putvega

    def call_rho(self):
        callrho = round(self.Xr0 * self.X2c / 100, 4)
        return callrho

    def put_rho(self):
        putrho = round(-self.Xr0 * self.X2p / 100, 4)
        return putrho
