# 이진탐색의 단점  새로운 노드 추가/기존 노드 삭제시 = 정렬을 유지 

def find(list, taget, start,end):
    mid = (start + end) //2
    if start > end:
        return -1
    if list[mid] == taget:
        return mid 
    
    if list[mid] > taget:  # 40 > 66
        return find(list, taget, start, mid-1)
    else:
        return find(list, taget, mid+1, end)

    

L = []
L.append(5)
L.append(8)
L.append(10)
L.append(15)
L.append(20)
L.append(25)
L.append(30)
L.append(40)
L.append(50)
L.append(54)
L.append(66)
L.append(83)
L.append(90)

index = find(L, 66, 0, len(L)-1)
print(index)