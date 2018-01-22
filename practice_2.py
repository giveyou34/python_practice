import random
'''
num=[]
for i in range(1, 46) :
  num.append(i)
'''
num = range(1, 46)

lotto = random.sample(num, 6)

print(lotto)
