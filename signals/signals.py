class SigItem:
    sig = []

    def __init__(self, code, oper, amount, trade_method, price, limitprice, shedule_time):
        self.sig = [code, oper, amount, trade_method, price, limitprice, shedule_time]

    '''
            {'code': code,
                    'oper': oper,
                    'amount': amount,
                    'trade_method': trade_method,
                    'price': price,
                    'limitprice': limitprice,
                    'shedule_time': shedule_time,
                    'status': 0}
    '''

    def read(self):
        pass

    def write(self):
        pass

    def commit(self):
        self.sig[6] = 1

    def commit_error(self):
        self.sig[6] = 2


class Signals:
    #  属性...
    #  一个signal是多个sig_item的列表：
    broker = ''
    options = ''
    sig_items = []

    def __init__(self, broker, options, sig_items):
        self.sig = [broker, options, sig_items]
'''        self.sig = {'broker': broker,
                    'options': options,
                    'sig_items': sig_items}
'''