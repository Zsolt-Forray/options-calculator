# options-calculator

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c0113772b1dc48b9865535ca3ac7daa0)](https://www.codacy.com/app/forray.zsolt/options-calculator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Zsolt-Forray/options-calculator&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/c0113772b1dc48b9865535ca3ac7daa0)](https://www.codacy.com/app/forray.zsolt/options-calculator?utm_source=github.com&utm_medium=referral&utm_content=Zsolt-Forray/options-calculator&utm_campaign=Badge_Coverage)
[![Build Status](https://travis-ci.com/Zsolt-Forray/options-calculator.svg?branch=master)](https://travis-ci.com/Zsolt-Forray/options-calculator)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Description
Calculates the value of Call/Put European options on non-dividend paying stocks and the Greeks.

## Usage
1.  Create a new directory somewhere.
2.  Open the Start Menu, type `cmd` in the search field, and then press Enter.
3.  Clone the project by running (make sure that you are in the newly created directory first!):
```txt
git clone https://github.com/Zsolt-Forray/options-calculator.git
```
4.  Tool is found in the `options-calculator` folder.

### Usage Example

**Parameters:**

* S: Stock Price
* K: Strike Price
* DTE: Days to Expiration
* IV: Implied Volatility (%)
* r: Risk-free Rate (%)

```python
#!/usr/bin/python3

import option_pricing_black_scholes as op

S = 65.0
K = 60.0
DTE = 30.0
IV = 35.0
r = 2.493

opsp = op.OptionPricing(S, K, DTE, IV, r)

print(opsp.call_price())
print(opsp.put_price())

opsg = op.OptionGreeks(S, K, DTE, IV, r)

print(opsg.call_theta())
print(opsg.put_gamma())
# etc...
```

### Output
Theoretical prices and the Greeks for European style Call and Put options.

## LICENSE
MIT

## Contributions
Contributions to this repository are always welcome.
This repo is maintained by Zsolt Forray (forray.zsolt@gmail.com).
