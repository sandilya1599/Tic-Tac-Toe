# Tic-Tac-Toe

/tic-tac-toe
│
├── src
│   ├── models
│   │   ├── Board.py
│   │   ├── CellValue.py
│   │   └── Enums.py   # GameState, Winner
│   │
│   ├── players
│   │   ├── Player.py       # abstract/interface
│   │   ├── HumanPlayer.py
│   │   └──  ComputerPlayer.py
│   │
│   ├── game
│   │   └── Game.py
│   │
│   └── main
│       └── main.py            # console entry point
│
├── tests
│   ├── test_board.py
│   ├── test_game.py
│   └── test_player.py
│
└── README.md


LLD

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
