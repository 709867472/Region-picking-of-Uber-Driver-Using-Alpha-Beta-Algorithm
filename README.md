# 1. Problem Description:
There are 2 Uber drivers(R1 and R2) pick regions in turn. Both of the them are interested in maximizing their profit. And one region can only be picked once. And every region they pick must be adjacent to the privoius regions they picked. If one driver has no region to pick, it mean he or her "Passed".

We assume that Region Profitability List (RPL) will be released in advance by ride-sharing companies. This list shows the profit the driver can get from a specific region. we represent the RPL in an ordered list of tuples (Region_Identifier, Profit_Number). So for a map with 4 regions: A,B,C,D. For example the list might be (A, 10), (B, 8), (C, 10), (D, 7) where A and C have a 10 profitability number followed by B with 8 and D with 7.

# 2. Evaluation Function:
Sometimes the RPL is not available due to the ride-sharing company not having enough resources to generate the list that day. In this case the drivers pick the next region using the following heuristic evaluation function:

<img width="1068" src="https://user-images.githubusercontent.com/11751622/43682193-9339bee4-9821-11e8-8c46-1a97c53cd78f.png">

In this problem we will represent a map with an adjacency matrix. If 2 regions are adjacent, the corresponding value in the matrix is 1, otherwise it is 0. For example consider a map with 4 regions A,B,C,D and the following adjacency matrix:

<img width="877" alt="screen shot 2018-08-04 at 8 14 15 pm" src="https://user-images.githubusercontent.com/11751622/43682222-fd73c984-9822-11e8-9e47-adfdb6285c8e.png">

A map with this matrix could look like:

<img width="780" alt="screen shot 2018-08-04 at 8 18 01 pm" src="https://user-images.githubusercontent.com/11751622/43682239-8df4b720-9823-11e8-95e3-2a7810b287a7.png">

# 3. Task:
The task is to generate the tree from a given point that lets you pick an optimal choice no matter what choices have been
made already. The program need to take the input from the file “input.txt” and print out its output to the file “output.txt”.
Each input file contains an abstract representation of a particular picking activity (region profitability list, and the map adjacency matrix) and a particular state in that activity (whose move it is (P1 or P2), and the sequence of picked regions up to that point in the activity). The input file will also specify a maximum depth limit D and the day the region profitability list was posted.

In the case of a current RPL, the program should output the utility values for the nodes at depth D. That is, the leaf nodes of the corresponding activity tree should be either an activity position after exactly D picks (alternating between P1 and P2) or an end-activity position after no more than D picks. In the case of a stale RPL, your program should output the utility values according to the heuristic function for the nodes of the activity tree that correspond to the next pick of the specified driver.

# 4. File Formats:
**Input.txt**\
**\<DAY\>**\
Contains “today” or “yesterday” indicating which day the RPL was posted\
**\<PLAYER\>**\
Containseither “R1” or “R2” indicating which roommate has next turn\
**\<REGION PROFITABILITY LIST\>**\
Ordered list of tuples (Region_Identifier, Profit_Number).\
**\<ADJACENCY MATRIX ROWS\>**\
The rows of the adjacency matrix representing the map.\
**\<REGIONS PICKED SO FAR\>**\
Comma separated list of regions picked so far. Will contain “*” if no activity yet.\
**\<MAX DEPTH\>**\
determines the maximum depth of your search tree
