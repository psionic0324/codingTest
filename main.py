# 병합 정렬
import sys
N = int(input())
nlist = []
for i in range(N):
  nlist.append(int(sys.stdin.readline()))

def merge_sort(nlist):
  if len(nlist) < 2:
    return nlist
  mid = len(nlist) // 2
  left_arr = merge_sort(nlist[:mid])
  right_arr = merge_sort(nlist[mid:])
  
  new_merge = []
  i = j = 0
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] < right_arr[j]:
      new_merge.append(left_arr[i])
      i += 1
    else:
      new_merge.append(right_arr[j])
      j += 1
  new_merge += left_arr[i:]
  new_merge += right_arr[j:]
  return new_merge

result = merge_sort(nlist)
for i in result:
  print(i)