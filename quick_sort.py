def quick_sort(list):
    quick_sort_recurse(0, len(list) - 1, list)

def quick_sort_recurse(beginning, ending, list):
    if(beginning >= ending):
        return
    half = int(beginning + (ending-beginning)/2)

    print("Pivot = %d" %(list[half]))

    end = ending - 1
    location = beginning
    for x in range(beginning, end):
        while(list[x] > list[ending] and x < ending):
            list[x], list[end] = list[end], list[x]
            end -= 1
        location += 1

    list[ending], list[location] = list[location], list[ending]
    print(list)
    print("Recurse \n \n")
    quick_sort_recurse(beginning, half - 1, list)
    quick_sort_recurse(half + 1, ending, list)

list = [3,1,6,2,7,5,8,9,0]
print(list)
quick_sort(list)
