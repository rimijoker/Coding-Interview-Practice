def findPythagoreanTriplets(nums):
  squares = set([n**2 for n in nums])
  print(squares)

  for a in nums:
      for b in nums:
          if a**2 + b**2 in squares:
              return True
  return False

a = findPythagoreanTriplets([3, 5, 12, 5, 13, 7, 7, 7])
print(a)
# True