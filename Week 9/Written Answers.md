# Graph Algorithms Lab

## Task 1: BFS

###  Hand trace on Graph 1 (BFS)

| Step | Node dequeued | Newly enqueued |  Queue after the step (front ... back) |
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
