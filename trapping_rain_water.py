# https://leetcode.com/problems/trapping-rain-water/description/

def container_volume(height, left_index, right_index):
    """
    Calculate the amount of water held between the indices in height.

    :param height: integer height values
    :type height: list
    :param left_index: container starting point
    :type left_index: int
    :param right_index: container end point
    :type right_index: int
    :rtype: int
    """
    
    container_height = min(height[left_index],height[right_index])
    volume = 0
    for i in range(left_index + 1, right_index):
        if height[i] > container_height:
            raise 
        volume += container_height - height[i]
    return volume
# end container_volume

def trap1(height):
    # This solution is probably O(n**2) due to sorting the values
    """
    Calculate the amount of water held by the entire topographic height list.

    :param height: integer height values
    :type height: list
    :rtype: int
    """

    if (len(height) == 0):
        return 0
    result = 0
    # order the max heights with their indices
    maxes = [(height[x], x) for x in range(len(height))]
    maxes.sort()
    # remove from the right end of list, i.e. the highest first
    left_bound = right_bound = maxes.pop()
    while (len(maxes) > 0):
        temp = maxes.pop()
        # calculate the volume held between the current bounds and the next max height
        if (temp[1] < left_bound[1]):
            result += container_volume(height, temp[1], left_bound[1])
            left_bound = temp
        elif (temp[1] > right_bound[1]):
            result += container_volume(height, right_bound[1], temp[1])
            right_bound = temp
        # There is no else: we discard any max/index within calculated bounds.
        if (left_bound[1] == 0 and right_bound[1] == (len(height) - 1)):
            break # When calculated bounds include the entire list, we are done.
    return result
# end trap1

def trap2(height):
    # This solution will be O(n), traversing the array only twice
    # We need to know the highest height to the left of each index and the highest to the right
    """
    Calculate the amount of water held by the entire topographic height list.

    :param height: integer height values
    :type height: list
    :rtype: int
    """
    if (len(height) == 0):
        return 0
    # If we get here, there is at least one height in the list.
    result = 0
    # We will keep track of the highest height to the left so we can calculate on the return pass.
    left_max = []
    # The first pass is from left to right.
    current_max = 0
    for i in range(0, len(height)):
        # Update current_max, if needed, and store left_max for this index.
        if height[i] > current_max:
            current_max = height[i]
        left_max.append(current_max)
    # The second pass is right to left
    current_max = 0
    water_level = 0 # This variable will be updated for each index to be the max of left_max and current_max
    for i in range(len(height) -1, -1, -1):
        # Update current_max, if needed.
        if height[i] > current_max:
            current_max = height[i]
        # Add the amount of rain trapped at this height to result
        result += min(left_max[i], current_max) - height[i]
    return result
# end trap2

# testing based on use cases from the problem description on LeetCode
heights = []
heights.append([0,1,0,2,1,0,1,3,2,1,2,1])
heights.append([4,2,0,3,2,5])
heights.append([1,2,3,14,4,5,3,2,1,10,4,5,6,7,9,3,2,1])
for height in heights:
    print(height)
    print("Trap1: " + str(trap1(height)))
    print("Trap2: " + str(trap2(height)))