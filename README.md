# Region-picking-of-Uber-Driver-Using-Alpha-Beta-Algorithm
## 1. Problem Description:
There are 2 Uber drivers(R1 and R2) pick regions in turn. Both of the them are interested in maximizing their profit. And one region can only be picked once. And every region they pick must be adjacent to the privoius regions they picked. If one driver has no region to pick, it mean he or her "Passed".

We assume that Region Profitability List (RPL) will be released in advance by ride-sharing companies. This list shows the profit the driver can get from a specific region. we represent the RPL in an ordered list of tuples (Region_Identifier, Profit_Number). So for a map with 4 regions: A,B,C,D. For example the list might be (A,10),(B,8),(C,10),(D,7) where A and C have a 10 profitability number followed by B with 8 and D with 7.

## 2. Evaluation Function:
Sometimes the RPL is not available due to the ride-sharing company not having enough resources to generate the list that day. In this case the drivers pick the next region using the following heuristic evaluation function:


In this problem we will represent a map with an adjacency matrix. The adjacency
matrix is an abstract representation of a map with regions that captures the
necessary information about the adjacency relationships of all the regions on the
map. Each row,column value in the matrix represents whether the region associated
with the column and the region associated with the row are adjacent (i.e. – whether
or not their borders touch). A value of 1 indicates regions are adjacent and a value
of zero indicates the regions are not adjacent. So for example consider a map with
4 regions A,B,C,D and the following adjacency matrix:

A map with this matrix could look like:
