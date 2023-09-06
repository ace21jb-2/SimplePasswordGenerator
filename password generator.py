#Written by Jack Barker on 29/8/23

import random
str = ""
for i in range (4): #Uppercase letters
    str = str + (chr(random.randint(65,90)))

for i in range (4): #Lowercase letters
    str = str + (chr(random.randint(97,122)))

for i in range (4): #Numbers
    str = str + (chr(random.randint(48,57)))

for i in range (0): #Special Characters
    # ( !,",#,$,%,&,',(,),*,+,,,-,.,/ )
    str = str +(chr(random.randint(33,47)))

print (''.join(random.sample(str, len(str))))
