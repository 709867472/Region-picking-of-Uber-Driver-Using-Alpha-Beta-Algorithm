import time
start_time = time.time()

inputFile = open('test_cases/test_case1.txt', 'r')
outputFile = open('output.txt', 'w')
lines = inputFile.readlines()
# get the maximum depth limit
maxDepth = int(lines[-1][:-1])
# get the regions already picked by 2 drivers
picked = lines[-2][:-1].replace('*', '').replace(',', '')
# get the regions "I" already picked
myPicked = []
for i in range(len(picked) - 2, -1, -2):
    myPicked.append(picked[i])
# get the regions and profit information of each region
list = lines[2][1:-2].replace('),(', ',').split(',')
regions = list[0::2]
pairs = dict(zip(regions, map(int, list[1::2])))
# store (region: index) pairs into a dictionary
indices = {}
for i in range(len(regions)):
    indices.update({regions[i]: i})
# get the total profit "I" already got
total = 0
for region in myPicked:
    total = total + pairs[region]
# get the starting depth when we start to pick regions
startDepth = len(picked)
# get average profit of all regions
average = sum(pairs.values()) / len(pairs)
utilities, nextStep = [], []


def getChildPaths(prePath):
    """ Get all the child paths
    Arguments:
    prePath -- the squence of picked regions
    """
    paths = []
    # if "I" already passed, just return
    if len(prePath) > 1 and prePath[-2] == '#':
        paths.append(prePath + '#')
        return paths
    found = False
    # if "I" already picked some regions, then "I" should pick regions
    # according to my previous region
    if len(prePath) > 1:
        pre = prePath[-2]
        vector = lines[3 + indices[pre]][1:-2].split(',')
        for i in range(len(vector)):
            if regions[i] not in prePath and vector[i] == '1':
                found = True
                paths.append(prePath + regions[i])
    # if "I" have not picked any regions, then "I" should pick a region
    # have not been picked yet
    else:
        for i in range(len(regions)):
            if regions[i] not in prePath:
                found = True
                paths.append(prePath + regions[i])
    # if "I" did not find any region to pick, it means "I" passed
    if not found:
        paths.append(prePath + '#')
    return paths


def getMax(prePath, preSum, minValue, maxValue, height, pickedCount):
    """ Max function in alpha-beta algorithm
    Arguments:
    prePath -- the squence of picked regions
    preSum -- the profit "I" already got
    minValue -- the minimum value of subtrees
    maxValue -- the maximum value of subtrees
    height -- current height
    pickedCount -- the number of picked regions
    """
    sum = 0
    value = -float('inf')
    # if "I" already ran out of regions, the total profit should not increase
    if len(prePath) > 0 and prePath[-1] == '#':
        sum = preSum
    else:
        pickedCount = pickedCount + 1
        # if it is current RPL
        if lines[0].startswith('T'):
            sum = preSum + pairs[prePath[-1]] if height % 2 == 0 else preSum
        else:
            # if it is stale RPL, we compute profit using evaluation fucntion
            if (height % 2 == 0):
                sum = presum + (average + pairs[prePath[-1]]) / 2.0
            else:
                sum = preSum
    # if we met the depth limit or already picked all the regions, we stop
    if startDepth + height == maxDepth or pickedCount == len(regions):
        utilities.append(sum)
        return sum
    # get the the maximum value of all the subtrees, if the value returned by
    # subtree is larger than or equal to the minimum value, we do pruning
    for path in getChildPaths(prePath):
        value = getMin(path, sum, minValue, maxValue, height + 1, pickedCount)
        if value >= minValue:
            return value
        if value > maxValue:
            maxValue = value
            if height == -1:
                nextStep.append(path[-1])
    return maxValue


def getMin(prePath, preSum, minValue, maxValue, height, pickedCount):
    """ Min function in alpha-beta algorithm
    Arguments:
    prePath -- the squence of picked regions
    preSum -- the profit "I" already got
    minValue -- the minimum value of subtrees
    maxValue -- the maximum value of subtrees
    height -- current height
    pickedCount -- the number of picked regions
    """
    sum = 0
    value = -float('inf')
    # if "I" already ran out of regions, the total profit should not increase
    if len(prePath) > 0 and prePath[-1] == '#':
        sum = preSum
    else:
        pickedCount = pickedCount + 1
        # if it is current RPL
        if lines[0].startswith('T'):
            sum = preSum + pairs[prePath[-1]] if height % 2 == 0 else preSum
        # if it is stale RPL, we compute profit using evaluation fucntion
        else:
            if (height % 2 == 0):
                sum = presum + (average + pairs[prePath[-1]]) / 2.0
            else:
                sum = preSum
    # if we met the depth limit or already picked all the regions, we stop
    if startDepth + height == maxDepth or pickedCount == len(regions):
        utilities.append(sum)
        return sum
    # get the the minimum value of all the subtrees, if the value returned by
    # subtree is smaller than or equal to the maximum value, we do pruning
    for path in getChildPaths(prePath):
        value = getMax(path, sum, minValue, maxValue, height + 1, pickedCount)
        if value <= maxValue:
            return value
        if value < minValue:
            minValue = value
    return minValue

getMax(picked, total, float('inf'), -float('inf'), -1, len(picked) - 1)

# write the optimal next action into output file
if (nextStep[-1] == '#'):
    outputFile.write('PASS\n')
else:
    outputFile.write(nextStep[-1] + '\n')
# write the utilities list into the output file
for i in range(len(utilities)):
    utilities[i] = int(utilities[i] + 0.5)
    if i == len(utilities) - 1:
        outputFile.write(str(utilities[i]))
    else:
        outputFile.write(str(utilities[i]) + ',')

print("--- %s seconds ---" % (time.time() - start_time))
