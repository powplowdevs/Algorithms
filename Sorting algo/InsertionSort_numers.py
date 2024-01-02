
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def sort_lines():
    sorted = False
    index = 0
    numbers = [2,4,3,1,5]
    numbers_og = numbers 
    #while not sorted
    #1. get the height on our line
    #2. get the height of the last line (if we are not at the ends)
    #3. if the last line is > the current line swap them
    #3. index -= 1
    #4. loop
    while not sorted:
        try:
            index += 1
            current = numbers[index]
            last = numbers[index-1]
            sub_sort = False
            while not sub_sort:
                if current < last and index != 0:
                    swapPositions(numbers,index,index-1)
                    index-=1
                    current = numbers[index]
                    last = numbers[index-1]
                else:
                    sub_sort = True
        except:
            print(f"OG list: {numbers_og}\nSorted list: {numbers}")
            break

sort_lines()