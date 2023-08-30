import random
str = ""
for i in range (4):
    str = str + (chr(random.randint(48,57)))
    str = str + (chr(random.randint(65,90)))
    str = str + (chr(random.randint(97,122)))

#str = str +(chr(random.randint(33,47)))

print (''.join(random.sample(str, len(str))))