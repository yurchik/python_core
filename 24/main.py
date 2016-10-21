from urllib import request

url='http://chart.finance.yahoo.com/table.csv?s=GOOG&a=8&b=16&c=2016&d=9&e=16&f=2016&g=d&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fw = open(dest_url, 'w')

    for line in lines:
        fw.write(line + "\n")
    fw.close()

download_stock_data(url)