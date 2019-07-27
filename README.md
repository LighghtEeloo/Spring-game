# Spring-game
  This is a minor chess game powered by python3 on linux.  
  This is a chess game with the following rules:  

|  |  |  |  |  |
| - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |

  As the chess board above illustrates, the chess game has a 4 × 5 board and has two players. Players take turns to drop their piece on the board. There are 20 blocks on the board, each block can contain multiple pieces of one player.  
The core rule of the game is spreading out. Take the block at the corner as an example: if it contains **2** pieces, these pieces will instantly seperate and move to nearby blocks, making this...

|  |  |  |  |  |
| - | - | - | - | - |
| **2** | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |

  ...into this...

|  |  |  |  |  |
| - | - | - | - | - |
| 0 | **1** | 0 | 0 | 0 |
| **1** | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |

  Also the pieces currently located in these invaded blocks will be ***turned*** to the invader's side.  
And for the blocks by the side, they need **3** pieces to spread out. For the blocks in the middle, they need **4**.  
  The spread out also has the possibility of chain reaction. If another block reaches the requirement of spreading out after one block's spread, it will spread out instantly as well.

  The goal is to ***turn*** all the pieces on the board to your side. Of course, it starts only after both players have dropped their first pieces.  

  The input stands for a position(<line>,<row>). For instance, "0,1" stands for the block in line 0 and row 1. To ensure the best experience, using "0,0" as player 1's first input is recommended.  
  The board is displayed by directly printing the board on the terminal. Do ensure you run it on **python3 for linux**.  
  
  Have fun!
