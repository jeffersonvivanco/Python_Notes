text = 'pýtĥöñ\fis\tawesome\r\n'

# Making a traslation table from the sys and unicode data modules
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
if unicodedata.combining(chr(c)))

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None # Deleted
}

b = unicodedata.normalize('NFD', text)
c = b.translate(cmb_chrs)
d = c.translate(remap)
print(d)
