def pair_goal_sum(arr, goal_sum):
  left = 0
  right = len(arr) - 1

  while left < right:
    sum = arr[left] + arr[right]
    if sum == goal_sum:
      return [left, right]
    if sum < goal_sum:
      left += 1
    else:
      right -= 1
    sum = arr[left] + arr[right]

  return [-1, -1]


def pair_goal_sum_hash(arr, goal_sum):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if goal_sum - num in nums:
      return [nums[goal_sum - num], i]
    else:
      nums[arr[i]] = i
      print(str(nums))
  return [-1, -1]


def main():

  # result = pair_goal_sum([1,2,3,4,6],6)
  # print( "indices of pair adding up to goal_sum is: " + str(result))

  # result = pair_goal_sum([2,5,9,11],11)
  # print( "indices of pair adding up to goal_sum is: " + str(result))

  # result = pair_goal_sum([2,5,9,11],21)
  # print( "indices of pair adding up to goal_sum is: " + str(result))


  result = pair_goal_sum_hash([1,2,3,4,6],6)
  print( "indices of pair adding up to goal_sum is: " + str(result))

  result = pair_goal_sum_hash([2,5,9,11],11)
  print( "indices of pair adding up to goal_sum is: " + str(result))

  result = pair_goal_sum_hash([2,5,9,11],21)
  print( "indices of pair adding up to goal_sum is: " + str(result))

main()