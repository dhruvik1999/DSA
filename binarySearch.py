
ff=False;
def binarySearch(list,key,l,r):
    if(l<=r):
        mid=(l+r)//2
        print(mid)
        if list[mid]==key:
            print("Found")
            return "Found"
        else:
            if list[mid] < key:
                l=mid+1
                binarySearch(list,key,l,r)
            else:
                r=mid-1
                binarySearch(list,key,l,r)
    else:
        print("Not Found")
        return "Not Found"


li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
binarySearch(li,7,0,19)


