#Pick number to find in list (23)
#If the value of the number is less than the item in the middle of the list, pick the lower half of the list
#Otherwise pick the upper half
#Continue till you find the number

numbers = [2,5,8,12,16,23,38,56,72,91]
target = 12

def binarySort(numbers, target):
    split_index = round(len(numbers)/2)
    new_list = []
    print(split_index)
    if numbers[split_index] > target:
        new_list = numbers[0:split_index]
    elif numbers[split_index] < target:
        new_list = numbers[split_index:len(numbers)]
    else:
        print(f"done\nOG list: {numbers} Target: {target} Target index: {split_index}")
        quit()
    binarySort(new_list,target)

binarySort(numbers,target)