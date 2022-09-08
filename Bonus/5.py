lst = [6,7,3,4,0,1,4,3]
target = 12

def pair (lst, target):
    lst.sort()
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] + lst[right] == target:
            return(f"{lst[left]} + {lst[right]} = {target}")
            break
        elif lst[left] + lst[right] < target:
            left += 1
        else:  right -= 1
        
    return(f"No pairs work for target {target}.") 

print(pair(lst, target))
