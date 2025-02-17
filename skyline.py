# https://leetcode.com/problems/the-skyline-problem/description/

def skyline(buildings):
    """
    Given an input of multiple buildings described in [x1,x2,height]
    output a skyline described by [x,y] coordinates originating horizontal
    lines of the skyline

    :param buildings: a list of building definitions
    :type buildings: list
    :rtype: list
    """
    height = []
    current_position = 0
    for building in buildings:
        x1 = building[0]
        x2 = building[1]
        h = building[2]
        while current_position < x1: # Pad out the height list with zero to length of x1, if needed.
                height.append(0)
                current_position += 1
        current_position = x1 # Return to x1 to add/compare/update values in height list.
        while current_position < x2:
            if current_position == len(height):
                height.append(h) # Add to the end of the list.
            elif height[current_position] < h:
                    height[current_position] = h # Update the current position in the list.
            current_position += 1
        current_position = len(height) # Go to the end of the list.
    # After the height map is built, add a coordinate to result for each change in height.
    result = []
    prior_height = 0
    for i in range(0,len(height)):
        if height[i] != prior_height:
            result.append([i,height[i]])
            prior_height = height[i]
    result.append([len(height), 0]) # Terminate the list.
    return result
# end skyline


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(buildings)
print(skyline(buildings))
buildings = [[0,2,3],[2,5,3]]
print(buildings)
print(skyline(buildings))