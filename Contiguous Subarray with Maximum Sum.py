def max_subarray_sum(arr):
  sums = arr[0];
  for i in arr:
    s = 

def add_right_element(arr, i, sums):
  if arr[i+1] != None:
    sums = sums + arr[i + 1]
    return sums
  else:
    return sums

def add_right_element(arr, i, sums):
  if arr[i-1] != None:
    sums = sums + arr[i + 1]
    return sums
  else:
    return sums


print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137
