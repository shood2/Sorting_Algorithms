def bubble_sort(list):
    switched = 1
    while(switched != 0):
        switched = 0
        for x in range(0, len(list) - 1):
          if(list[x + 1] < list[x]):
            list[x], list[x + 1] = list[x + 1], list[x]
            switched += 1
