number=int(input("How many quick picks?"))

import random
for line in range(0,number,1):
    lists = []
    for randomnumber in range (0,6,1):
        lists.append(random.randint(1,46))
    lists=list(set(lists))
    lists.sort()
    print(",".join(str(i) for i in lists))