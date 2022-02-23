str = 'X-DSPAM-Confidence: 0.8457'

ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
value = float(piece)
print(value)
