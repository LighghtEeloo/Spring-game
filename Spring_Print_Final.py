#-*-coding:utf8;-*-
from collections import OrderedDict

class Board(object):
    def __init__(self,default=1):
        if default == 1:
            self.board = OrderedDict()  # stores the info of occupied blocks.
            self.s = (4,5)  # Shape
            
    def move(self,player):
        # get a valid input
        while 1:
            pos = self._ask(player)
            try:
                pos = tuple([int(a) for a in pos.split(',')])
                if pos[0] in range(self.s[0]) and pos[1] in range(self.s[1]):
                    if pos in self.board and self.board[pos][0] == player:
                        break
                    elif not pos in self.board:
                        break
                print('Bad input.')
            except:
                print('Bad input.')
                continue
        # put piece
        self._drop(player,pos)
        # chain reaction
        while 1:
            lst = []
            flag = False
            for pos in self.board:
                if self.board[pos][1] >= self._check(pos):
                    print('blooming:', pos)
                    lst = self._bloom(player,pos)
                    flag = True
                    break
            if flag:
                self.board[pos][1] -= self._check(pos)
                if self.board[pos][1] == 0:
                    del self.board[pos]
                self._bigdrop(player,lst,override = True)
            else:
                break
        #print(self.board)
    
    def _ask(self,player):
        pos = input('Player %d: ' %player)
        return pos
    
    def _bigdrop(self,player,lpos,override=False):
        for pos in lpos:
            self._drop(player,pos,override) 
    
    # drop a piece
    def _drop(self,player,pos,override=False):
        status = self.board.get(pos,[-1])
        if status[0] == -1:
            self.board[pos] = [player,1]
            return 0
        elif status[1] + 1 <= self._check(pos) and not override:
            self.board[pos][1] += 1
            return 1
        elif override:
            self.board[pos][0] = player
            self.board[pos][1] += 1
        else:
            pass
                  
    # whether at corner, by side or in the middle
    def _check(self,pos):
        lst = [(0,0),(0,self.s[1]-1),(self.s[0]-1,0),(self.s[0]-1,self.s[1]-1)]
        if pos in lst:
            return 2
        elif pos[0] in [0,self.s[0]-1] or pos[1] in [0,self.s[1]-1]:
            return 3
        else:
            return 4
            
    # returns nearby block positions
    def _bloom(self,player,pos):
        lpos = list(pos)
        diffs = [[0,1],[0,-1],[1,0],[-1,0]]
        nposs = []
        for diff in diffs:
            nposs.append([lpos[i]+diff[i] for i in range(2)])
        lpos = []
        for npos in nposs:
            if npos[0] in range(self.s[0]) and npos[1] in range(self.s[1]):
                lpos.append(tuple(npos))
        return lpos
        
    def judge(self):
        if len(self.board) >= 2:
            # getting the owners of blocks
            lst = []
            for k in self.board.items():
                lst.append(k[1][0])
            if 1 in lst and not 2 in lst:
                print('\nPlayer 1 wins!')
                return 1
            elif not 1 in lst and 2 in lst:
                print('\nPlayer 2 wins!')
                return 2
            else:
                return 0
        else:
            return 0
        
    def display(self):
        print('\n')
        print('  0 1 2 3 4',end = '')
        cnt = 0
        lne = 0
        for cpos in [(a,b) for a in range(4) for b in range(5)]:
            if cnt % self.s[1] == 0:
                print()
                print('\033[0m%d '%lne,end = '')
                lne += 1
            cnt += 1
            piece = self.board.get(cpos,[0,0])
            if piece[0] == 1:
                print('\033[47;34m%d '%piece[1], end = '')
            elif piece[0] == 2:
                print('\033[47;31m%d '%piece[1], end = '')
            else:
                print('\033[30;47m0 ', end = '')
        print('\033[0m')
        
        
bd = Board()
player = 1
for ni in range(42):
    print('\n')    
    bd.move(player)
    bd.display()
    result = bd.judge()
    if result != 0:
        print('---End.---')
        break
    player = player % 2 + 1 # switch player 1/2
    