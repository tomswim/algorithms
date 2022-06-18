def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 0
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1
  print(str(arr))

  return next_non_duplicate


def remove_duplicates_fully(arr):
  # index of the next non-duplicate element
  # next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    if arr[i-1] == arr[i]:
      arr.remove(arr[i])
    else:
      i += 1
  print(str(arr))

  return len(arr)


def main():
  # print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  # print(remove_duplicates([2, 2, 2, 11]))

  print(remove_duplicates_fully([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates_fully([2, 2, 2, 11]))


main()
