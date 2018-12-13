#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:59:56 2018

@author: sandilya
"""

board='---------'
totalMoves={}
nodeUtility={}
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
def convertBoard(board):
	parent=''
	for i in range(9):
		parent+=board[i]
	return parent

#Move Generator
#generates the moves			
def generateMoves(turn,board):
	possibleMoves=[]
	for i in range(9):
		result=''
		if board[i]=='-':
			for j in range(9):
				if i!=j:
					result=result+board[j]
				else:
					if turn:
						result=result+'X'
					else:
						result=result+'O'		
			#check if the node is terminal	
			utility=terminalState(result)
			possibleMoves.append(result)
			nodeUtility[result]=utility
			totalMoves[result]=generateMoves(not turn,result)
			#if node is a parent node then for MAX 
			if nodeUtility[result] == False:
				# X 's turn means MAX
				if turn == True:
					max=-2
					for i in totalMoves[result]:
						if i[2]>max:
							max=i[2]
					nodeUtility[result]=max		
				#O 's turn means MIN
				else:
					min=2
					for i in totalMoves[result]:
						if i[2]<min:
							min=i[2]
					nodeUtility[result]=min	
	#print(possible_moves)		
	return possibleMoves
def printBoard(board):
    for i in range(9):
        print board[i],
        if i%3==2:
            print
def chooseMin(board):
    min=10
    choosenBoard=''
    for i in totalMoves[board]:
        if nodeUtility[i]<min:
            min=nodeUtility[i]
            choosenBoard=i
    return choosenBoard        
#true for X false for O
turn=True
parent=convertBoard(board)
totalMoves[parent]=generateMoves(True,board)
print(len(totalMoves))
#
#print(totalMoves.keys())
#Moves are genereated

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
        boardNow=convertBoard(board)
        board=chooseMin(boardNow)
        printBoard(board)
    print    
    turn=not turn
    result=terminalState(board)
    print(result)
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