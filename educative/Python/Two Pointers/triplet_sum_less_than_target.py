def triplets_with_smaller_sum(arr, target):
  arr.sort()
  count = 0
  triplets = []
  for i in range(len(arr)-2):
    # count += search_pair(arr, target-arr[i], i)
    search_pair(arr, target-arr[i], i, triplets)
  # return count
  return triplets, len(triplets)


def search_pair(arr, target_sum, first, triplets):
  # count = 0
  left = first + 1
  right = len(arr) -1
  while(left < right):
    if arr[left] +arr[right] < target_sum:  # found the triplet
      # count  += right - left
      for i in range(right, left, -1):
        triplets.append([arr[first], arr[left], arr[i]])
      left += 1
    else:
      right -= 1  # we need a pair with a smaller sum
  # return count

def main():
  print(triplets_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
