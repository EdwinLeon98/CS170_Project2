import random

# Node class
class Node():

    def __init__(self, f):
        self.feats = set()
        for i in f:
            self.feats.add(i)
        self.acc = round(random.uniform(1.00, 100.00), 2)

print("Welcome to Edwin Leon and Josh McIntyre's Feature Selection Algorithm")

# Features prompt and input sanitization
features = None
invalid = True
while invalid:
    features = input("Please enter the total number of features\n")
    if int(features) < 0:
        invalid = True
    else:
        invalid = False

# Algorithm prompt and input sanitization
algorithm = None
invalid = True
while invalid:
    algorithm = input("Type the number of the algorithm you want to run\n1. Forward Selection\n2. Backward Elimination\n")
    if(algorithm == '1'):
        invalid = False
    elif(algorithm == '2'):
        invalid = False
    else:
        invalid = True

# Forward Selection Search
if(algorithm == '1'):
    n = Node(set())         # Set n to Node with features = {}
    print("Using no features and \"random\" evaluation, we get an accuracy of {}%".format(n.acc))
    print("Beginning search.")
    currMax = n             # Set current and true max to n
    trueMax = currMax
    size = 1
    decreased = False       # Flag to see if our accuracy decreased during an iteration of our search

    while not size > int(features):
        tmpMax = currMax    # tmpMax helps track last iterations max Node
        count = 1           # helps track current iteration's first valid subset

        # Loop to find currMax
        for i in range(1, int(features)+1):
            n = Node(set.union({i}, tmpMax.feats))

            # Do not want to create subsets we checked last iteration
            if not len(n.feats) == size:
                continue

            # Init currMax to first valid subset
            if count == 1:
                currMax = n
            
            # Updates currMax
            if n.acc >= currMax.acc:
                currMax = n
            print("Using feature(s) {} accuracy is {}%".format(str(n.feats), n.acc))
            count += 1

        if not size+1 > int(features):
            print("\nFeature set {} was best, accuracy is {}%\n".format(str(currMax.feats), currMax.acc))
        
        # Update true max, and set decreased flag if currMax < trueMax, meaning our search decreased from a higher accuracy
        if currMax.acc >= trueMax.acc:
            trueMax = currMax
        else:
            decreased = True
        size += 1

    # Display results and accuracy decreased warning if applicable
    if decreased:
        print("\n(Warning, Accuracy has decreased!)")
    if len(trueMax.feats) == 0:
        print("Finished search!! The best feature subset is {{}}, which has an accuracy of {}%".format(trueMax.acc))
    else:
        print("Finished search!! The best feature subset is {}, which has an accuracy of {}%".format(str(trueMax.feats), trueMax.acc))

# Backward Elimination Search
else:
    n = Node(set())         # Set n to Node with features = {1, 2, 3, 4, ..., nFeatures}
    for i in range(1, int(features)+1):
        n.feats.add(i)
    print("Using all features {} and \"random\" evaluation, we get an accuracy of {}%".format(n.feats, n.acc))
    print("Beginning search.")
    currMax = n             # Set current and true max to n
    trueMax = currMax
    size = int(features)-1
    decreased = False       # Flag to see if our accuracy decreased during an iteration of our search

    while not size < 0:
        tmpMax = currMax    # tmpMax helps track last iterations max Node
        count = 1           # helps track current iteration's first valid subset

        # Loop to find currMax
        for i in range(1, int(features)+1):
            n1 = Node(tmpMax.feats)
            if(i in n1.feats):
                n1.feats.remove(i)

            # Do not want to create subsets we checked last iteration
            if not len(n1.feats) == size:
                continue

            # Init currMax to first valid subset
            if count == 1:
                currMax = n1
            
            # Updates currMax
            if n1.acc >= currMax.acc:
                currMax = n1
            if size == 0:
                print("Using feature(s) {{}} accuracy is {}%".format(n1.acc))
            else:
                print("Using feature(s) {} accuracy is {}%".format(str(n1.feats), n1.acc))
            count += 1

        if not size == 0:
            print("\nFeature set {} was best, accuracy is {}%\n".format(str(currMax.feats), currMax.acc))
        
        # Update true max, and set decreased flag if currMax < trueMax, meaning our search decreased from a higher accuracy
        if currMax.acc >= trueMax.acc:
            trueMax = currMax
        else:
            decreased = True
        size -= 1

    # Display results and accuracy decreased warning if applicable
    if decreased:
        print("\n(Warning, Accuracy has decreased!)")
    if len(trueMax.feats) == 0:
        print("Finished search!! The best feature subset is {{}}, which has an accuracy of {}%".format(trueMax.acc))
    else:
        print("Finished search!! The best feature subset is {}, which has an accuracy of {}%".format(str(trueMax.feats), trueMax.acc))