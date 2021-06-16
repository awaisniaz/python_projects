import itertools
temp = 0
for i in itertools.cycle("ABC"):
    if temp < 50:
      print(i,end='')
    else:
        break
    temp = temp + 1