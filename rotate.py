def rotate(strg, n):
     print(strg[n:] + strg[:n])


def create_key(key, rounded):
     if 10>rounded>0:
          rotate(key, rounded)
     elif rounded ==0:
          rotate(key, -1)
     elif rounded>9:
          rounded = rounded -10
          rotate(key, rounded)


