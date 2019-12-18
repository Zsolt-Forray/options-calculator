#!/usr/bin/python3


"""
Test for the options calculator
"""


__author__  = 'Zsolt Forray'
__license__ = 'MIT'
__version__ = '0.0.1'
__date__    = '18/12/2019'
__status__  = 'Development'


import unittest
import option_pricing_black_scholes as bs
from option_pricing_black_scholes import InvalidDataError


class TestOptionPrice(unittest.TestCase):
    def test_call_price(self):
        data = (65.0, 60.0, 30.0, 35.0, 2.493)
        price = bs.OptionPrice(*data)
        result = price.call_price()
        self.assertEqual(5.85, result)

    def test_put_price(self):
        data = (62.0, 60.0, 30.0, 25.0, 1.62)
        price = bs.OptionPrice(*data)
        result = price.put_price()
        self.assertEqual(0.9, result)

    def test_invalid_param(self):
        data = (65.0, 60.0, 30.0, 0.0, 2.493)
        with self.assertRaises(InvalidDataError):
            bs.OptionPrice(*data)

    def test_missing_param(self):
        data = (65.0, 60.0, 30.0, 25.0)
        with self.assertRaises(TypeError):
            bs.OptionPrice(*data)

class TestOptionGreeks(unittest.TestCase):
    def test_call_delta(self):
        data = (150.0, 180.0, 350.0, 20.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_delta()
        self.assertEqual(0.2386, result)

    def test_put_delta(self):
        data = (20.0, 20.0, 50.0, 70.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_delta()
        self.assertEqual(-0.4433, result)

    def test_call_gamma(self):
        data = (15.0, 30.0, 35.0, 100.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_gamma()
        self.assertEqual(0.01, result)

    def test_put_gamma(self):
        data = (220.0, 200.0, 50.0, 110.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_gamma()
        self.assertEqual(0.004, result)

    def test_call_vega(self):
        data = (30.0, 30.0, 5.0, 40.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_vega()
        self.assertEqual(0.014, result)

    def test_put_vega(self):
        data = (1000.0, 1050.0, 50.0, 110.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_vega()
        self.assertEqual(1.4703, result)

    def test_call_theta(self):
        data = (29.0, 30.0, 5.0, 10.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_theta()
        self.assertEqual(-0.0002, result)

    def test_put_theta(self):
        data = (100.0, 150.0, 350.0, 110.0, 2.493)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_theta()
        self.assertEqual(-0.0522, result)

    def test_call_rho(self):
        data = (25.0, 30.0, 5.0, 10.0, 0.0)
        greeks = bs.OptionGreeks(*data)
        result = greeks.call_rho()
        self.assertEqual(0.0, result)

    def test_put_rho(self):
        data = (100.0, 150.0, 350.0, 110.0, 5.0)
        greeks = bs.OptionGreeks(*data)
        result = greeks.put_rho()
        self.assertEqual(-1.1078, result)

    def test_invalid_param(self):
        data = (65.0, 60.0, -30.0, 40.0, 2.493)
        with self.assertRaises(InvalidDataError):
            bs.OptionGreeks(*data)

    def test_missing_param(self):
        data = (65.0, 60.0, 30.0, 25.0)
        with self.assertRaises(TypeError):
            bs.OptionGreeks(*data)


if __name__ == "__main__":
    unittest.main()
