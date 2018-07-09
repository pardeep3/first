#ques 1

import re
emails='''"gogo98@gmail.com" "dipi456@yahoo.com"
"jeff42@facebook.com"'''
userid=re.findall('[a-z0-9]+',emails)
print(userid)

#ques 2

import re
text ="Betty bought a bit of butter,But the butter was so bitter,so she bought some better butter,To make the bitter butter better."
words=re.findall('[bB][a-z]*',text)
print(words)

#ques 3

import re
text=''' "A,very very;irregular_sentence"'''
words=re.sub(r'[,;_\s]',' ',text)
print(words)
