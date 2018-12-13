#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:59:56 2018

@author: sandilya
"""
import random
board='---------'
def terminalState(board):
	#check who wins or Draw or board not filled
	for i in range(3):
		if board[i]!='-' and board[i]==board[i+3]==board[i+6]:
			if board[i]=='O':
				return -1
			elif board[i]=='X':
				return 1	
	i=0
	while i<9:
		if board[i]==board[i+1]==board[i+2] and board[i]!='-':
			if board[i]=='O':
				return -1
			elif board[i]=='X':
				return 1
		i+=3			
	if board[0]==board[4]==board[8] and board[0]!='-':
		if board[0]=='O':
			return -1
		elif board[0]=='X':
			return 1	
	if board[2]==board[4]==board[6] and board[2]!='-':
		if board[0]=='O':
			return -1
		elif board[0]=='X':
			return 1	
	for i in range(9):
		if board[i]=='-':
			return 2
		#board is filled but no more moves possible		 
	return 0								
def printBoard(board):
    for i in range(9):
        print board[i],
        if i%3==2:
            print

#true for X false for O
turn=True
while True:
    printBoard(board)
    if turn:
        print("Player's turn")
        print("Enter row and column")
        row=int(input())
        col=int(input())
        board=board[:row*3+col]+'X'+board[row*3+col+1:]
        printBoard(board)
    else:
        print("Computer's turn")
        while True:
        	row=random.randint(0,2)
        	col=random.randint(0,2)
        	if board[row*3+col]!='-':
        		continue
        	else:
        		board=board[:row*3+col]+'O'+board[row*3+col+1:]
        		break		
        printBoard(board)
    print    
    turn=not turn
    result=terminalState(board)
    if result==2:
        continue
    elif result==1:
        print("Player wins")
        break
    elif result==-1:
        print("Computer wins")
        break
    else:
        print("Draw")
        break