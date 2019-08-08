import re

# colors
print('\u001b[31mHello World')

print('256 colors')

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        print(u'\u001b[38;5;' + code + 'm' + code.ljust(4), end='')
    print('\n')

print('\u001b[0m')

# highlighting certain words in text
text = 'Hello my name is Jeff. Today I went to work. Work is very hard. Work is tiring. Work is interesting.'


def highlight_text(t, w):
    return re.sub(r'\b({w})\b'.format(w=w), u'\u001b[31m'r'\1'u'\u001b[0m', t, flags=re.IGNORECASE)


def highlight_text_multiple(t, words):
    h_text = t
    for w in words:
        h_text = re.sub(r'({0})'.format(w), u'\u001b[31m'r'\1'u'\u001b[0m', h_text, flags=re.IGNORECASE)
    return h_text


highlighted_text = highlight_text_multiple(text, ['work', 'jeff'])
print(u''+highlighted_text)