kumpulan=[2,4,5,10,13,18,23,29,31,51,64]
target = (10)
def binse(kumpulan, target):
    low =0
    
    high = len(kumpulan)-1
    while low <= high:
        mid =(high+low)//2
        if kumpulan[mid] ==target:
            return True
        elif target <kumpulan[mid]:
            high=mid-1
        else :
            Slow = mid+1
    return false

binse(kumpulan, target)