rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# now suppose you want to iterate over the data in chunks grouped by date
# to do this, first sort by the desired field (date) and then groupby()

from operator import itemgetter
from itertools import groupby

# sort by desired field first
rows.sort(key=itemgetter('date'))

#iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('     ', i)

# If your goal is to simply group the data together by dates into a large data structure that
# allows random access, you may have better luck using defaultdict() to build a multidict
# ex
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)

# for the above, it is not necessary to sort the records first, thus if memory is no concern,
# than it may be faster to do this approach


