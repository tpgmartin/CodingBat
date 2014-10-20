def in1to10(n, outside_mode):
    if(outside_mode):
        return n not in range(2,10)
    else:
        return n in range(1,11)
  