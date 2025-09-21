# Tic‑Tac‑Toe

A simple console Tic‑Tac‑Toe implementation with a human and computer player. The computer uses a precomputed minimax dataset (output/minmax.json) or an algorithm fallback.

Features
- 3×3 Tic‑Tac‑Toe
- Human vs Human and Human vs Computer
- Precomputed minimax moves available in output/minmax.json
- Minimal, dependency‑free runtime (only Python)

Requirements
- Python 3.8+ recommended
- Optional: pytest for tests

Quick start (Windows)
1. Create a virtual environment:
   - PowerShell:
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
   - CMD:
     python -m venv .venv
     .\.venv\Scripts\activate.bat
2. Install dev deps (optional):
   pip install -r requirements-dev.txt
   or pip install pytest
3. Run the game:
   - Direct:
     python src\main.py
   - As a package (if imports require it):
     python -m src.main
4. Run tests (if you add tests):
   pytest

Project layout

```
- src/
  - main.py                — console entry point
  - algorithm/
    - minmax.py            — minimax generator / helpers
  - game/
    - game.py              — game loop, move validation, win/draw logic
  - models/
    - board.py             — Board data structure
    - board_evaluator.py   — win/draw detection and scoring helpers
    - cell_values.py       — X/O/Empty enum
    - enums.py             — Game state / winner enums
  - players/
    - player.py            — Player base interface
    - human_player.py      — Console input player
    - computer_player.py   — AI player (reads output/minmax.json)
- output/
  - minmax.json            — precomputed minimax results (used by AI)
```

Low Level Design
```

           +----------------+
           |    Board       |
           +----------------+
           | - cells[][]    |
           +----------------+
           | +getCell(r,c)  |
           | +setCell(r,c,v)|
           | +display()     |
           +----------------+
                   ^
                   |
                   | used by
                   |
           +----------------+
           |     Game       |
           +----------------+
           | - board        |
           | - player1      |
           | - player2      |
           | - currentPlayer|
           | - state        |
           | - winner       |
           +----------------+
           | +play()        |
           | +switchTurn()  |
           | +validateMove()|
           | +checkWinner() |
           | +isDraw()      |
           +----------------+
                   ^
                   |
           -----------------
           |               |
   +----------------+  +----------------+
   |    Player      |  |  Winner Enum   |
   +----------------+  +----------------+
   | - name         |  | PLAYER1        |
   +----------------+  | PLAYER2        |
   | +getMove()     |  | DRAW           |
   | +validateMove()|  +----------------+
   +----------------+
           ^
           |
   ---------------------
   |                   |
+----------------+  +----------------+
| HumanPlayer    |  | ComputerPlayer |
+----------------+  +----------------+
| +getMove()     |  | +getMove()     |
|                |  | - depthLimit   |
|                |  | - minimax()    |
+----------------+  +----------------+
```

Notes about AI and output/minmax.json
- The computer player loads moves from output/minmax.json if available. If you want to regenerate that dataset, run algorithm/minmax.py (it can produce a JSON file of best moves).
- If the JSON is missing or incomplete, the computer player falls back to a local minimax heuristic.

Suggested README improvements
- Document valid console input format and examples (e.g., "row col" or "A1").
- Add a short example session showing moves and final board.
- Add a CONTRIBUTING.md and requirements-dev.txt for contributors.
- Add a LICENSE (e.g., MIT) and include license badge.
- Add a GitHub Actions workflow to run pytest on push/PR.

Contributing
PRs welcome. Please add tests for new behavior and follow consistent style (consider adding linters/mypy).

License
Add a LICENSE file (e.g., MIT) if you intend to open source the project.