from datetime import *
#from dateutil import *

current_date = date.today()

output_format = '%d/%m/%y'

c_d_formatted = datetime.strftime(current_date, output_format)
weekday = datetime.strftime(current_date, '%A')

current_time = datetime.now()
time_output = datetime.strftime(current_time, '%H:%M')

def time_based_commands(prev_dt_list):
    pass


#datetime.now()
#datetime.today()
#datetime.combine()
#date.fromisoformat("")
#datetime.timedelta

