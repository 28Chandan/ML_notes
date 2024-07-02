import re
a = 'From Stephen.marq@uct.ac.za sat Tan 5'
u=re.findall('\+@\s+',a)
print(u)