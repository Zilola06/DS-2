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

#
## Task 3: Dijkstra's Algorithm

###  Hand trace on Dijkstra's Algorithm Graph

| Step | Node settled (its dist) | Updates made (node = new dist via previous node) |
|---|---|---|
| Init | - | A=0, others=INF |
| 1 | A (0) | B=4 via A, C=2 via A |
| 2 | C (2) | B=3 via C, D=10 via C, E=12 via C |
| 3 | B (3) | D=8 via B |
| 4 | D (8) | E=10 via D, F=14 via D |
| 5 | E (10) | F=13 via E |
| 6 | F (13) | no updates |

**Final distances and previous nodes**

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Final dist | 0 | 3 | 2 | 8 | 10 | 13 |
| Final prev | - | C | A | B | D | E |

### Short Answers

**1. Explain relaxation with one line of your table (for example, why B changes from 4 to 3).**
When settling C, the distance to B changes from 4 to 3 because the path A -> C -> B costs 2 + 1 = 3, which is cheaper than the previous path A -> B with cost 4.

**2. Why does Dijkstra give wrong results when an edge has a negative weight? How is BFS related to Dijkstra when every weight is 1?**
Dijkstra assumes that once a node is settled, its shortest distance is final. A negative edge could later produce a cheaper path to an already settled node, violating this assumption.
When every edge has weight 1, the cheapest path is the path with the fewest edges. BFS finds these paths, so BFS and Dijkstra produce the same shortest-path distances in this case.







