from datetime import datetime
from re import split

text = 'Sat, 06 Jul 2019 18:55:37 -0400'
y = datetime.strptime(text, '%a, %d %b %Y %H:%M:%S %z') # strptime() bad performance

text2 = 'Wed, 10 Jul 2019 18:54:00 GMT'
months = {
    'Jul': 7
}


# instead use custom solution that parses date string and creates datetime object from them
def parse_datetime(s):
    df = split(r',\s|\s', s)
    t = split(':', df[4])
    month = months[df[2]]
    h = t[0]
    m = t[1]
    s = t[2]
    return datetime(int(df[3]), month, int(df[1]), int(h), int(m), int(s))


d1 = parse_datetime(text)
d2 = parse_datetime(text2)

print(d1, d2)

