str = 'a5e6'
str1 = ''
l = len(str)
for i in range(1, l, 2):
    str1 += str[i - 1]
    c = chr(ord(str[i - 1]) + int(str[i]))
    str1 += c
print(str1)
