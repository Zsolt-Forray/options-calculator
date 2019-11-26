#!/usr/bin/python3


"""
Test for the options calculator
"""


__author__  = 'Zsolt Forray'
__license__ = 'MIT'
__version__ = '0.0.1'
__date__    = '26/11/2019'
__status__  = 'Development'


import unittest
import option_pricing_black_scholes as bs
from option_pricing_black_scholes import InvalidDataError


class TestOptionPricing(unittest.TestCase):
    def test_call_price(self):
        data = (65.0, 60.0, 30.0, 35.0, 2.493)
        price = bs.OptionPrice(*data)
        result = price.call_price()
        self.assertAlmostEqual(first=5.8523, second=result, places=2)

    def test_put_price(self):
        data = (65.0, 60.0, 30.0, 35.0, 2.493)
        price = bs.OptionPrice(*data)
        result = price.put_price()
        self.assertAlmostEqual(first=0.7279, second=result, places=2)

    def test_invalid_param(self):
        data = (65.0, 60.0, 30.0, 0.0, 2.493)
        with self.assertRaises(InvalidDataError):
            bs.OptionPrice(*data)


class TestOptionGreeks(unittest.TestCase):
    def test_call_delta(self):
        data = (150.0, 180.0, 350.0, 20.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_delta()
        self.assertAlmostEqual(first=0.2386, second=result, delta=0.0002)

    def test_put_delta(self):
        data = (20.0, 20.0, 50.0, 70.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_delta()
        self.assertAlmostEqual(first=-0.4432, second=result, delta=0.0002)

    def test_call_gamma(self):
        data = (15.0, 30.0, 35.0, 100.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_gamma()
        self.assertAlmostEqual(first=0.01, second=result, delta=0.0002)

    def test_put_gamma(self):
        data = (220.0, 200.0, 5.0, 110.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_gamma()
        self.assertAlmostEqual(first=0.0102, second=result, delta=0.0002)

    def test_call_vega(self):
        data = (25.0, 30.0, 5.0, 10.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_vega()
        self.assertAlmostEqual(first=0.0, second=result, delta=0.0002)

    def test_put_vega(self):
        data = (1000.0, 1050.0, 50.0, 110.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_vega()
        self.assertAlmostEqual(first=1.4703, second=result, delta=0.0002)

    def test_call_theta(self):
        data = (25.0, 30.0, 5.0, 10.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_theta()
        self.assertAlmostEqual(first=0.0, second=result, delta=0.0002)

    def test_put_theta(self):
        data = (100.0, 150.0, 350.0, 110.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_theta()
        self.assertAlmostEqual(first=-0.0522, second=result, delta=0.0002)

    def test_call_rho(self):
        data = (25.0, 30.0, 5.0, 10.0, 0.0)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_rho()
        self.assertAlmostEqual(first=0.0, second=result, delta=0.001)

    def test_put_rho(self):
        data = (100.0, 150.0, 350.0, 110.0, 5.0)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_rho()
        self.assertAlmostEqual(first=-1.1085, second=result, delta=0.001)


if __name__ == "__main__":
    unittest.main()
