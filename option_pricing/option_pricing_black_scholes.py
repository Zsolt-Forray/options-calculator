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

        self.t_yrs = time_to_exp_days / 365
        self.v_dec = annual_vol_pc / 100
        self.r_dec = risk_free_rate_pc / 100

        self.d = (m.log(self.S / self.K) + (self.r_dec + self.v_dec ** 2 / 2) * \
                self.t_yrs) / (self.v_dec * m.sqrt(self.t_yrs))

    def call_price(self):
        call_price = self.S * nd.cdf(self.d) - \
                     self.K * m.exp(-1 * self.r_dec * self.t_yrs) * \
                     nd.cdf(self.d - self.v_dec * m.sqrt(self.t_yrs))
        return call_price

    def put_price(self):
        put_price = -self.S * nd.cdf(-self.d) + \
                    self.K * m.exp(-self.r_dec * self.t_yrs) * \
                    nd.cdf(self.v_dec * m.sqrt(self.t_yrs) - self.d)
        return put_price

    # The sensitivities of the Black-Scholes Model
    def call_delta(self):
        call_delta = nd.cdf(self.d)
        return call_delta

    def put_delta(self):
        put_delta = -nd.cdf(-self.d)
        return put_delta

    def call_gamma(self):
        call_gamma = nd.pdf(self.d) / (self.S * self.v_dec * m.sqrt(self.t_yrs))
        return call_gamma

    def put_gamma(self):
        put_gamma = nd.pdf(self.d) / (self.S * self.v_dec * m.sqrt(self.t_yrs))
        return put_gamma

    def call_theta(self):
        call_theta = -self.S * self.v_dec * nd.pdf(self.d) / (2 * m.sqrt(self.t_yrs)) - \
                     self.r_dec * self.K * m.exp(-self.r_dec * self.t_yrs) * \
                     nd.cdf(self.d - self.v_dec * m.sqrt(self.t_yrs))

        call_theta = call_theta / 365
        return call_theta

    def put_theta(self):
        put_theta = -self.S * self.v_dec * nd.pdf(self.d) / (2 * m.sqrt(self.t_yrs)) + \
                    self.r_dec * self.K * m.exp(-self.r_dec * self.t_yrs) * \
                    nd.cdf(self.v_dec * m.sqrt(self.t_yrs) - self.d)

        put_theta = put_theta / 365
        return put_theta

    def call_vega(self):
        call_vega = self.S * m.sqrt(self.t_yrs) * nd.pdf(self.d)
        call_vega = call_vega / 100
        return call_vega

    def put_vega(self):
        put_vega = self.S * m.sqrt(self.t_yrs) * nd.pdf(self.d)
        put_vega = put_vega / 100
        return put_vega

    def call_rho(self):
        call_rho = self.t_yrs * self.K * m.exp(-self.r_dec * self.t_yrs) * \
                    nd.cdf(self.d - self.v_dec * m.sqrt(self.t_yrs))

        call_rho = call_rho / 100
        return call_rho

    def put_rho(self):
        put_rho = -self.t_yrs * self.K * m.exp(-self.r_dec * self.t_yrs) * \
                    nd.cdf(self.v_dec * m.sqrt(self.t_yrs) - self.d)

        put_rho = put_rho / 100
        return put_rho

def check_input(S, K, DTE, IV, r):
    check = False
    try:
        if 0.0 < S  and 0.0 < K and 0.0 < DTE and 0.0 < IV and 0.0 <= r:
            check = True
        else:
            raise InvalidDataError()
    except InvalidDataError:
        print("[Error] Input parameter(s) out of range")
    except TypeError:
        print("[Error] Invalid input parameter(s)")
    return check

def run(S, K, DTE, IV, r):
    if check_input(S, K, DTE, IV, r) == True:
        op = OptionPricing(S, K, DTE, IV, r)
        res_dict = {
                    "call": {
                            "value": round(op.call_price(),2),
                            "delta": round(op.call_delta(),4),
                            "gamma": round(op.call_gamma(),4),
                            "theta": round(op.call_theta(),4),
                            "vega": round(op.call_vega(),4),
                            "rho": round(op.call_rho(),4),
                            },
                    "put": {
                            "value": round(op.put_price(),2),
                            "delta": round(op.put_delta(),4),
                            "gamma": round(op.put_gamma(),4),
                            "theta": round(op.put_theta(),4),
                            "vega": round(op.put_vega(),4),
                            "rho": round(op.put_rho(),4),
                            },
                    }
        return res_dict


if __name__ == "__main__":
    res = run(65.0, 60.0, 30.0, 35.0, 2.493)
