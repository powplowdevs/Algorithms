def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def sort_lines(lis):
    global pivot_index

    #pick a pivoit (at middle ruffly)
    #move pivoit to end of list (just remove it then append it)
    #find item from left (first number from left larger than pivot) 
    #find item from right (first number from right smaller than pivot)
    #if item from left > item from right then we are done, swap item from left with out pivot 
    #if we are not done we will swap item from left with item from right
    try:
        pivot = lis[pivot_index]
        lis.remove(pivot)
        lis.append(pivot)
    except:
        print(f"Sorted list {lis}")
        quit()

    while True:
        IFL = 0
        IFR = 0
        index = 0
        for i in range(len(lis)):
            if lis[i] <= pivot:
                IFR = lis[i]
        for i in range(len(lis)):
            index += 1
            if lis[len(lis)-index] >= pivot:
                IFL = lis[len(lis)-index]
        
        if lis.index(IFL)>lis.index(IFR) or lis.index(IFL)==lis.index(IFR):
            print(f"\nDONE!\nSwaping {IFR} with {pivot} becuse {IFL} > {IFR}")
            swapPositions(lis,lis.index(IFL),lis.index(pivot))
            print(lis)
            pivot_index+=1
            sort_lines(lis)
            break
        else:
            print(f"Swaping {IFR} with {IFL}")
            swapPositions(lis,lis.index(IFR),lis.index(IFL))
        

numbers = [2,4,3,1,5]
pivot_index = 0
sort_lines(numbers)