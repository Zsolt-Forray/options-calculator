# Options Calculator

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c0113772b1dc48b9865535ca3ac7daa0)](https://www.codacy.com/app/forray.zsolt/options-calculator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Zsolt-Forray/options-calculator&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/c0113772b1dc48b9865535ca3ac7daa0)](https://www.codacy.com/app/forray.zsolt/options-calculator?utm_source=github.com&utm_medium=referral&utm_content=Zsolt-Forray/options-calculator&utm_campaign=Badge_Coverage)
[![Build Status](https://travis-ci.com/Zsolt-Forray/options-calculator.svg?branch=master)](https://travis-ci.com/Zsolt-Forray/options-calculator)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Description
Calculates the value of Call/Put European options on non-dividend paying stocks and the Greeks.

## Usage

### Usage Example

**Parameters:**

* S: Stock Price
* K: Strike Price
* DTE: Days to Expiration
* IV: Implied Volatility (%)
* r: Risk-free Rate (%)

```python
#!/usr/bin/python3

import option_pricing_black_scholes as bs

S = 65.0
K = 60.0
DTE = 30.0
IV = 35.0
r = 1.6995

price = bs.OptionPrice(S, K, DTE, IV, r)

print(price.call_price())
print(price.put_price())

greeks = bs.OptionGreeks(S, K, DTE, IV, r)

print(greeks.call_theta())
print(greeks.put_gamma())
# etc...
```

### Output
Theoretical prices and the Greeks for European style Call and Put options.

## LICENSE
MIT

## Contributions
Contributions to this repository are always welcome.
This repo is maintained by Zsolt Forray (forray.zsolt@gmail.com).
