# 🎯 Tic Tac Toe Game (Python LLD + Implementation)

### 🧩 Problem Statement

Design and implement a **Tic Tac Toe** game for **two human players** on a **3x3 grid** using Python.  
The system should allow two players to take turns, validate moves, detect wins or draws, and display the game board after each move.

This is designed as a **Low-Level Design (LLD)** problem suitable for a **1-hour system design coding interview**.

---

## 🧱 Requirements

- Two players (Human vs Human)
- Board size: 3x3
- Each player uses a symbol (`X` or `O`)
- The game alternates turns
- Detect win or draw
- Simple CLI-based interface (no AI)
- Robust input validation

**Optional (for follow-ups):**
- Extendable to NxN
- Add AI Player (Minimax)
- Networked multiplayer

---

## ⚙️ Design Approach

### Key Design Principles
- **Single Responsibility Principle:** Each class handles one concern (Board, Player, Game loop).
- **Encapsulation:** Board state and counters hidden behind `Board` methods.
- **Extendability:** Easy to scale for larger boards or additional player types.
- **Constant-time winner check:** O(1) update and check after each move using counters.

---

## 🧩 Class Design

### 1. `Player`
Represents a human player.

| Attribute | Type | Description |
|------------|------|-------------|
| `name` | `str` | Player name |
| `symbol` | `str` | 'X' or 'O' |

### 2. `Board`
Handles the game board and logic for moves and winner detection.

| Attribute | Type | Description |
|------------|------|-------------|
| `size` | `int` | Size of the board (3x3) |
| `grid` | `List[List[str]]` | 2D array storing board cells |
| `rows`, `cols` | `List[int]` | Track counts for win detection |
| `diag`, `anti_diag` | `int` | Track diagonal sums |
| `moves_count` | `int` | Count total moves |

**Methods**
- `make_move(r, c, symbol)` → bool  
- `check_winner(r, c, symbol)` → bool  
- `is_full()` → bool  
- `display()` → prints board  
- `reset()` → clears state  

### 3. `Game`
Controls game flow and player turns.

| Attribute | Type | Description |
|------------|------|-------------|
| `board` | `Board` | Game board instance |
| `players` | `List[Player]` | Two players |
| `current_idx` | `int` | Whose turn it is |

**Methods**
- `start()` → starts CLI game loop  
- `switch()` → toggles turns  
- `_get_move_from_user()` → reads validated input  

---

## 📊 Class Diagram

```

+----------------+     1         1     +-------------+
|    Game        |---------------------|   Player    |
|----------------|                     |-------------|
| - board:Board  |                     | - name:str  |
| - players:list |                     | - symbol:str|
| - current_idx  |                     +-------------+
|----------------|
| + start()      |
| + play_turn()  |
+----------------+
|
| 1
|
+---v---+
| Board |
|-------|
| - size: int
| - grid: List[List[str]]
| - rows: List[int]
| - cols: List[int]
| - diag: int
| - anti_diag: int
|-------------------------
| + make_move(r,c,player)
| + check_winner(r,c,p)
| + is_full()
| + display()
+-------------------------

````

---

## 🧠 Winner Detection Approach

To avoid scanning rows/columns each time (O(n)), we maintain integer counters:

- For each move:
  - X = +1, O = -1
  - Update `rows[r]`, `cols[c]`
  - If `rows[r] == size` → X wins  
  - If `rows[r] == -size` → O wins

This gives **O(1)** time per move — efficient and scalable.

---

## 🧪 Unit Testing

### Framework
Uses Python’s built-in `unittest`.

### Example Test Cases
| Test | Description |
|------|--------------|
| `test_make_move_success` | Valid move placed correctly |
| `test_make_move_invalid_out_of_range` | Out-of-bounds move rejected |
| `test_row_win_X` | Detects horizontal win |
| `test_col_win_O` | Detects vertical win |
| `test_diag_win_X` | Detects diagonal win |
| `test_anti_diag_win_O` | Detects anti-diagonal win |
| `test_draw_detection` | Detects draw condition |
| `test_reset` | Board resets correctly |

Run using:
```bash
python -m unittest test_tic_tac_toe.py
````

---

## 🧭 Example Gameplay (CLI)

```
Starting Tic-Tac-Toe (3x3)
Player 1 (X): Alice
Player 2 (O): Bob

Board:
  |   |  
---------
  |   |  
---------
  |   |  

Alice's turn (X)
Enter move as 'row col': 1 1

Board:
X |   |  
---------
  |   |  
---------
  |   |  
...
```

---

## 📈 Complexity Analysis

| Operation      | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| `make_move`    | O(1)            | O(n²)            |
| `check_winner` | O(1)            | O(n)             |
| `is_full`      | O(1)            | O(1)             |

---

## 🧩 Possible Follow-up Questions & Answers

### 1. **How would you extend to an N×N board?**

* The logic is already parameterized by `size`.
* Only change `Board(size=N)` — counters scale automatically.

### 2. **How to implement AI (computer player)?**

* Add an `AIPlayer` subclass of `Player`.
* Implement `get_move()` using **Minimax algorithm**.
* For efficiency, prune branches using **Alpha-Beta pruning**.

### 3. **How would you handle concurrent players (networked version)?**

* Introduce a server managing game state.
* Use WebSockets or sockets to synchronize moves.
* Ensure moves are serialized (one at a time).

### 4. **What about saving/resuming a game?**

* Add serialization in `Board` and `Game`:

  ```python
  def to_dict(self): ...
  def from_dict(cls, data): ...
  ```
* Store in JSON format.

### 5. **How do you ensure input robustness?**

* Validate numeric inputs.
* Handle out-of-range and occupied cells.
* Optional: limit retries or add default safe move.

### 6. **Can you detect invalid symbol configurations?**

* Yes, assert in `Player` constructor ensures only 'X' or 'O'.
* In `Game`, assert that both players use distinct symbols.

### 7. **How would you make this testable (no console input)?**

* Abstract `_get_move_from_user()` — mock in tests.
* Inject a “move provider” for automated play.

### 8. **How can this scale for multi-round matches or tournaments?**

* Add a `Match` or `Tournament` class to track multiple `Game` instances and scores.

---

## 🧱 Future Enhancements

| Feature     | Description                            |
| ----------- | -------------------------------------- |
| Undo/Redo   | Maintain move stack                    |
| AI Opponent | Minimax with difficulty levels         |
| GUI         | Tkinter or Pygame                      |
| Web Version | Flask/FastAPI backend + React frontend |
| Multiplayer | Socket-based sync                      |

---

## 📚 Files Overview

| File                  | Purpose                                        |
| --------------------- | ---------------------------------------------- |
| `tic_tac_toe.py`      | Main implementation                            |
| `test_tic_tac_toe.py` | Unit tests                                     |
| `README.md`           | Design, diagrams, and explanations (this file) |

---

## 🧠 Key Takeaways for Interviews

* Focus on **class design clarity** and **encapsulation**.
* Justify **O(1) winner checking** logic — good optimization insight.
* Explain **extension points**: AI, network, persistence.
* Clean, modular code reflects good LLD practices.
* Keep CLI separate from game logic → testable & extensible.

---

**Author:** *[Your Name]*
**Language:** Python 3.x
**Time Complexity:** O(1) per move
**Ideal for:** LLD + Coding Interview (1 hour)

---