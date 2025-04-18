# Source: https://usaco.guide/general/io

nums = list(map(int, input().split()))

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
  return array

test = bubbleSort(nums)
print(nums[0], nums[1], (nums[-1] - (nums[0] + nums[1])))