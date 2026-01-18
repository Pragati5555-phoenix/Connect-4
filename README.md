# Connect Four 🎲🔴🟡

A two-player command-line Connect Four game written in **Python 3.11.5**.

## 🎮 Features
- 7×6 grid with a **stylized ASCII board display**:
-  A   B   C   D   E   F   G
- Players drop tokens (`X` and `O`) into columns **A–G**
- Input validation (rejects invalid or full columns)
- Win detection for horizontal, vertical, and diagonal lines
- Draw detection when the board is full
- Replay option after each game

## 🛠 Requirements
- Python **3.11.5** (tested)
- Works on Windows 64-bit (MSC v.1936)

## ▶️ How to Run
Clone the repository and run:
```bash
python connectfour_ultimate.py
```
🧩 How to Play
- Player X goes first.
- On your turn, type a column letter (A–G) to drop your token.
- The game updates the ASCII board after each move.
- First player to connect four tokens in a row (horizontally, vertically, or diagonally) wins!
