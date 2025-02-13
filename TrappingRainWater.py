class TrappingRainWater:
    
    # ContainerVolume calculates the amount of water trapped in a defined "container" in the
    # height list between leftIndex and rightIndex.
    # This method assumes that no height between the indices is taller than the heights
    # at the indices.
    def containerVolume(height, leftIndex, rightIndex):
        # I should raise exceptions if the leftIndex or rightIndex are out of range of 0 to len(height)
        # TO DO
        
        containerHeight = min(height[leftIndex],height[rightIndex])
        volume = 0
        for i in range(leftIndex + 1, rightIndex):
            volume += containerHeight - height[i]
        return volume
    #end ContainerVolume

    # This solution is probably O(n**2) due to sorting the values
    # The heights are sorted with original indices
    # Then the heights are popped from the sorted list and the bucket sizes are calculated until the
    # entire range of heights has been processed
    def trap1(height):
        if (len(height) == 0):
            return 0
        # if we get here, there is at least one height in the list
        result = 0
        # order the max heights in descending order with their indexes in height
        maxes = [(height[x], x) for x in range(len(height))]
        maxes.sort() # number 1 done
        leftBound = rightBound = maxes.pop()
        while (len(maxes) > 0):
            temp = maxes.pop()
            # calculate the volume held between the current bounds and the next max height
            if (temp[1] < leftBound[1]):
                result += TrappingRainWater.containerVolume(height, temp[1], leftBound[1])
                leftBound = temp
            elif (temp[1] > rightBound[1]):
                result += TrappingRainWater.containerVolume(height, rightBound[1], temp[1])
                rightBound = temp
            # it's possible that the index is already within bounds. if so, we can throw it away
            # if our bounds encompass the entire list, we can exit
            if (leftBound[1] == 0 and rightBound[1] == (len(height) - 1)):
                break
        return result
    # end trap1

    # trap2 is under construction as an O(n) algorithm
    # the goal is to keep a running total as we go and avoid having to look back through the list
    # trading off more data stored as we go vs. time
    # I need to think more on method for this one
    def trap2(height):
        if (len(height) == 0):
            return 0
        # if we get here, there is at least one height in the list
        result = 0
        # keep track of heights so we can backtrack
        currentMax = 0
        lookBackIndex = 0
        lookBackTotal = 0
        for i in range(0, len(height)):
            # at the start, if height[i] > currentMax, simply update currentMax
            if height[i] > currentMax:
                currentMax = height[i]
    # end trap2
#end TrappingRainWater

# testing based on use cases from the problem description on LeetCode
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(TrappingRainWater.trap1(height))
height = [4,2,0,3,2,5]
print(TrappingRainWater.trap1(height))

