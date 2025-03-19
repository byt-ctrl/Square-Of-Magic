# Magic Square Generator 🔢

### What is Magic Square ?
**→** A magic square consists of square grids which contain arranged numbers whose row and column additions along with both diagonal totals match exactly.

---

**→** The Python application produces magic squares from any provided odd number value. The total values in a magic square arrangement match along the diagonals as well as in each row and column. The algorithm starts its sequence from the middle of the top row then goes **North-East** (Up-Right) to insert each number. When a cell already contains value the number moves to an empty cell below.

## How the Algorithm Works 🔄
**→** **ALGORITHM**

1. **Starting Position**: The algorithm begins at the middle of the top row (`a = 0, b = n // 2`).

2. **Placing Numbers**: For each number from `1` to `n*n`, the program places the number in the current position `(a, b)`.

3. The algorithm progresses **North-East** to its subsequent position after placing numbers by following this sequence: `new_a,new_b=(a-1)%n,(b+1)%n`.

    ```python
    new_a,new_b=(a-1)%n,(b+1)%n
    ```

    The formula enables the algorithm to move through the grid by wrapping the placement when it reaches the edges.

4. A check for occupied cells occurs in the program by moving to the next row when an existing cell is detected.

    ```python
    if square[new_a][new_b]:
        a+=1  # Move down (South)
    ```

5. The algorithm resumes placing numbers by advancing to the following vacant position.

Each row and column along with all diagonal patterns in this magic square produce identical sums overall.

---
### Example :- 
```python 
Enter the order of the Magic Square (The Number Should Be 'ODD' Number) -->  3

Magic Square --> 
 8  1  6
 3  5  7
 4  9  2
```

---
## 🤝 Contributing :

If u have any idea's feel free to contribute
Fork the repository if necessary , make your changes , and send a pull request.



## 📜 License :

This project is licensed under the **Apache 2.0 License**.



