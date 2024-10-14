
from datetime import datetime

def convert_date(date_format):
    input_date = datetime.strptime(date_format, '%d-%m-%Y')
    convert_date = input_date.strftime('%Y-%m-%d')
    return convert_date



