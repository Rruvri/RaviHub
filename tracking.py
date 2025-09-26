from datetime import *


current_date = date.today()

output_format = '%d/%m/%y'

c_d_formatted = datetime.strftime(current_date, output_format)
