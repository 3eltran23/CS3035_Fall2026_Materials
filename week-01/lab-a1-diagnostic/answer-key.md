# Lab A1 Diagnostic — Instructor Answer Key

----

## Part 3: CS 2012 Skills

- Question - Polymorphism output: `dog`
- Question 9: Recursion - `mystery(5)` result: `9`
- Question 9B - Recursive base case: `if (n <= 1) return 1;`

----

## Part 4: CS 2013 Skills
Question 10: Data Structure Selection

- Undo operation: stack
- Arrival order: queue
- Student ID lookup: hash table/map
- Connections between cities: graph
- Hierarchical file system: tree
Question 11-11C: Stack Tracing

- Stack trace: `x = 2`, `y = 9`, remaining bottom-to-top values are `4, 7`
Question 12: Algorithm Analysis
- Nested-loop duplicate algorithm: `O(n²)`

----

## Debugging
Question 13: Find the Error
The `findLargest` implementation fails for all-negative input because `largest` begins at zero. Initialize it with the first element and define behavior for empty input.

----

## Programming Problem

Question 14: Count Even Numbers 

```text
function countEven(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

    return count
```

Accept equivalent implementations.

Example tests:

| Input | Expected output |
|---|---:|
| `[3, 8, 2, 7, 10]` | `3` |
| `[]` | `0` |
| `[1, 3, 5]` | `0` |
| `[2, 4, 6]` | `3` |
| `[-4, -3, 0, 7]` | `3` |

----
