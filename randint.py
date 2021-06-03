## program to generate random integers
## generates 100 random integers
## stores their sums and max/min in a separate file called key

import random
randStr = str("")
generated = int(0)

max = int(0)
min = int(10000) ## the highest random number my program will guess is 10,000, can change if user desires
sum = int(0)
numberOfInts = int(10) ## Set by user

for j in range(10):
    for i in range(numberOfInts):
        generated = random.randint(0,10000)
        randStr = randStr + '\n' + str(generated)
        ## can change the \n if you want to try the whitespace as spaces, or even tabs with \t
        sum = sum + generated
        if(generated>max):
            max = generated
        if(generated<min):
            min = generated
    file_name = "integers" + str(j) + ".dat"
    with open(file_name, 'w') as txtFile:
        txtFile.write(randStr)
        txtFile.write(' ')
