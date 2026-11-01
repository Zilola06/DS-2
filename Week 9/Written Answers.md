# Graph Algorithms Lab

## Task 1: BFS

###  Hand trace on BFS Graph

| Step | Node dequeued | Newly enqueued | Queue after the step (front ... back) |
|---|---|---|---|
| Init | - | A | A |
| 1 | A | B, C | B, C |
| 2 | B | D, E | C, D, E |
| 3 | C | F | D, E, F |
| 4 | D | - | E, F |
| 5 | E | - | F |
| 6 | F | G | G |
| 7 | G | - | empty |

**Visit order:** A, B, C, D, E, F, G

### Short Answers

**1. Why mark a node when it is enqueued?**
Marking a node when it is enqueued prevents duplicate entries in the queue and ensures its shortest distance and parent are assigned correctly.

**2. What is BFS complexity? Why does it fail on weighted graphs?**
BFS runs in O(V+E) time. It finds paths with the fewest edges, not the lowest total weight, so it does not necessarily find the cheapest path in a weighted graph.

#
## Task 2: DFS

###  Hand trace on DFS Graph

| Step |  Node popped | Action | Pushed (in this order) | Stack after (top first) |
|---|---|---|---|---|
| Init | - | - | A | A |
| 1 | A | visit | C, B | B, C |
| 2 | B | visit | E, D | D, E, C |
| 3 | D | visit | - | E, C |
| 4 | E | visit | F | F, C |
| 5 | F | visit | G, C | C, G, C |
| 6 | C | visit | - | G, C |
| 7 | G | visit | - | C |
| 8 | C | skip (visited) | - | empty |

**Visit order:** A, B, D, E, F, C, G

### Short Answers

**1. Why can a node be in the stack twice? In which step of your trace is a copy skipped?**
A node can be pushed by different neighbours before it is visited because nodes are marked when popped, not when pushed. In the trace, node C is pushed twice. At step 8, the second copy of C is popped and skipped because it has already been visited. If we do not skip, it can create an infinite loop.

**2. Compare the BFS order and the DFS order on Graph 1. Which data structure explains the difference?**
BFS uses a queue (FIFO) and visits nodes level by level. DFS uses a stack (LIFO) and explores as deeply as possible before backtracking. The different data structures produce different traversal orders.
