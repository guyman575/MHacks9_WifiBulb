import yahoo_finance as yf



def get_stock_color():
    DOW = yf.Share('DOW')
    open_price = DOW.get_open()
    cur_price = DOW.get_price()
    if(open_price > cur_price):
        return 'ff0000'
    else:
        return '00ff00'
