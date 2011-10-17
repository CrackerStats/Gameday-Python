from datetime import timedelta
from datetime import date
from time import *
import string

start_date = date(2000,1,1)
end_date = date(2011,11,21)

day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    print strftime("%Y-%m-%d", single_date.timetuple())