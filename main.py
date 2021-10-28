# 삽입정렬
array = [8,4,6,2,9,1,3,7,5]
n = len(array)
for i in range(1, n):
    for j in range(i, 0, - 1):
		if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
print(array)