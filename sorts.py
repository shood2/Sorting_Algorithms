def bubble_sort(list):
    switched = 1
    while(switched != 0):
        switched = 0
        for x in range(0, len(list) - 1):
          if(list[x + 1] < list[x]):
            list[x], list[x + 1] = list[x + 1], list[x]
            switched += 1

list = [3,13, 2, 1, 0, 14, 10, 5, 7, 3]
print(list)
bubble_sort(list)
print(list)
