import json
import os
import re

import requests

STOCK_CODE_PATH = 'stock_codes.conf'

scopeandfile = {'all': 'stock_codes_all.conf',
              'index': 'stock_codes_idx.conf',
              'fund': 'stock_codes_fund.conf',
              'astock': 'stock_codes_astock.conf',
              'bstock': 'stock_codes_bstock.conf',
              'defulat': 'stock_codes.conf',
              'self': 'stock_codes_self.conf',
              'yahoo': 'stock_codes_yahoo.conf'
              }
def update_stock_codes():
    """获取所有股票 ID 到 all_stock_code 目录下"""
    all_stock_codes_url = 'http://www.shdjt.com/js/lib/astock.js'
    grep_stock_codes = re.compile('~((?:sh|sz|of)?\d+)`')
    response = requests.get(all_stock_codes_url)
    stock_codes0 = grep_stock_codes.findall(response.text)

    stock_codes = list(
        map(lambda stock_code: ('%s' if stock_code.startswith(('s','o')) else(
        'sh%s' if stock_code.startswith(('5', '6', '9'))  else 'sz%s')) % stock_code,
            stock_codes0))

    for sf in scopeandfile :
        if sf != 'self':
            with open(stock_code_path(sf), 'w') as f:
                scope_codes = [x for x in stock_codes if code_type(x) == sf]
                f.write(json.dumps(dict(stock=scope_codes)))

    with open(stock_code_path('all'), 'w') as f:
        f.write(json.dumps(dict(stock=stock_codes)))


    with open(stock_code_path('default'), 'w') as f:
        f.write(json.dumps(dict(stock=stock_codes)))


def set_default_scope(scope ):
    stock_codes = get_stock_codes(scope)
    with open(stock_code_path('default'), 'w') as f:
        f.write(json.dumps(dict(stock=stock_codes)))



def get_stock_codes(scope = ['default'], refresh=False):
    """获取所有股票 ID 到 all_stock_code 目录下"""
    if refresh:
        update_stock_codes()

    if 'all' in scope:

        with open(stock_code_path('all')) as f:
                return json.load(f)['stock']


    result = []
    for s in scope:
        with open(stock_code_path(s)) as f:
            data = json.load(f)['stock']
        result = result + data
    return result

def stock_code_path(scope='default'):
    if scope == 'default':
        return os.path.join(os.path.dirname(__file__), STOCK_CODE_PATH)
    else:
        return os.path.join(os.path.dirname(__file__), scopeandfile[scope] )


def code_type(stock_code):
    if stock_code.startswith(('sh00', 'sz39')):
        return 'index'
    elif stock_code.startswith(('sh5','sz15','sz16','sz18')) :
        return 'fund' #基金，包含封基、etf、lof等
    elif stock_code.startswith(('sh01','sh02', 'sh10','sh12','sh13', 'sz10','sz11')):
        return 'bond' #债券
    elif stock_code.startswith(('sh11', 'sz12')):
        return 'cb' #可转债
    elif stock_code.startswith(('sh132', 'sz12')):
        return 'eb' #可交换债
    elif stock_code.startswith(('sh20','sz13')):
        return 'repo'  #逆回购
    elif stock_code.startswith('o'):
        return 'fundnav'
    elif stock_code.startswith(('sh9','sz2')):
        return 'bstock'
    elif stock_code.startswith(('sh6', 'sz0','sz3')):
        return 'astock'
    else:
        return 'other'

def get_stock_type(stock_code):
    """判断股票ID对应的证券市场
    :param stock_code:股票ID
    :return 'sh' or 'sz'"""

    return stock_code[:2].lower() if str(stock_code).lower().startswith(('s', 'o')) else ('sh' if str(stock_code).startswith(('5', '6', '9')) else 'sz')


def get_full_code(stock_code):
    """
    :param stock_code:  股票 ID
    :return:  'sh000001' or 'sz000001'
    """

    return stock_code.lower() if str(stock_code).lower().startswith(('s', 'o')) else get_stock_type(stock_code) + stock_code

#if __name__ == 'main':
# update_stock_codes()

def get_yahoo_stock_codes(scope = ['yahoo'], refresh=False):
    if refresh:
        update_stock_codes()


    result = []
    for s in scope:
        with open(stock_code_path(s)) as f:
            data = json.load(f)['stock']
        result = result + data
    return result
