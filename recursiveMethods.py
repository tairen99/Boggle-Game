# using two recursive functions to do the word Boggle game
# Given words vector, check if word in words can be found on board.
# Rules:  The letters must be adjoining in a 'chain'.
# (Letter cubes in the chain may be adjacent horizontally,
# vertically, or diagonally.) Each letter can only be
# used one time in the word
#
# Test case is: for 4 by 4 dimensions board, any letters
# combinations.
# Two recursive functions are used to solve this problem
#
# By: Tairen Chen            Date: Sep, 10th, 2017
#

def wordCheck(lenWd,word,board,position,histPos,availPos):
    indW = len(word) - lenWd # check the left letters length of each word
    if indW == 0: # the case for the first charactor of each word
        sMap = len(board)
        # check the first letter on the board
        for ind in range(0, sMap):
            if word[indW] in board[ind]:
                col = [idx for idx, item in enumerate(board[ind]) if item == word[indW]]
                for colLen in range(0, len(col)):
                    position.append([ind, col[colLen]])
        if not position: # if not found
            return 0
        else:  # check the inner recursition for the characters
            lenPition = len(position)
            posChaInWd = lenWd - 1
            # call the inner recursion to find the availalbe characters for the following charactor in the word
            return chactCheck(lenPition, position, board, histPos, posChaInWd, word)

    elif indW < len(word)-1 and indW > 0:# for the letters that are not at the begining and the end of word
        positionNew = []
        if word[indW] in availPos: #check if the lettter from word in the available spaces
            col = [idx for idx, item in enumerate(availPos) if item == word[indW]]
            for colLen in range(0, len(col)): # if found the char in the available charactors, transfer indices of the character to position
                positionNew.append(position[col[colLen]])

        if not positionNew:
            return 0
        else:  # check the inner recursition for the characters
            lenPition = len(positionNew)
            hisPosition=[]
            posChaInWd = lenWd - 1
            # call the inner recursion to find the availalbe characters for the following charactor in the word
            return chactCheck(lenPition, positionNew, board, histPos, posChaInWd, word)
    else: # if last character of the word is also in the board, then return 1
        if word[indW] in availPos: #check if the last letter from word in the available spaces
            return 1
        else:
            return 0

def findPosition(currentPosition, board):
# Based on the current letter position, find the available positions on the board for the next letter.
    # for the test for whole function
    x = currentPosition[0]
    y = currentPosition[1]
    row = len(board)
    col = len(board[0])

    allPos = []
    indPos = []

    for jumpInd in [-1, 1]:
        if (x + jumpInd) >= 0 and (x + jumpInd < row):
            allPos.append(board[x + jumpInd][y])
            indPos.append([x + jumpInd, y])
        if (y + jumpInd) >= 0 and (y + jumpInd < col):
            allPos.append(board[x][y + jumpInd])
            indPos.append([x, y + jumpInd])
        if ((x + jumpInd) >= 0 and (x + jumpInd < row)) and ((y - 1) >= 0):
            allPos.append(board[x + jumpInd][y - 1])
            indPos.append([x + jumpInd, y - 1])
        if ((x + jumpInd) >= 0 and (x + jumpInd < row)) and (y + 1 < col):
            allPos.append(board[x + jumpInd][y + 1])
            indPos.append([x + jumpInd, y + 1])
    return allPos,indPos

def chactCheck(lenCha,chaPosition,board,hisPosition,posChaInWd,word):
    if lenCha == 1: # only one charactor find in the board
        # for the test for whole function
        x = chaPosition[0][0]
        y = chaPosition[0][1]
        currentPosition = [x,y]
        allPos,indPos = findPosition(currentPosition, board)

        # check if it is old character from prevous part
        lenHis = len(hisPosition)
        if lenHis:
            for hisP in hisPosition:
                if hisP in indPos:
                    pos = indPos.index(hisP)  # find the index of the hisP
                    indPos.pop(pos)  # remove [x,y] index from indPos
                    allPos.pop(pos)  # remove the correspond character from allPos(available character)

        hisPosition.append(chaPosition[0]) # update the historical position
        goodOne = wordCheck(posChaInWd, word, board, indPos, hisPosition,allPos)
        if goodOne == 1:
            return 1
        else:
            hisPosition.remove(chaPosition[0])

    else: # lenChar > 1. It means it exists more than one Character found in the board
        # then recursively find each possible letter combination
        for indChar in range(0,lenCha):

            # for the test for whole function
            x = chaPosition[indChar][0]
            y = chaPosition[indChar][1]
            currentPosition = [x, y]
            allPos, indPos = findPosition(currentPosition, board)

            # check if it is old character from prevous part
            lenHis = len(hisPosition)
            if lenHis:
                for hisP in hisPosition:
                    if hisP in indPos:
                        pos = indPos.index(hisP)  # find the index of the hisP
                        indPos.pop(pos)  # remove [x,y] index from indPos
                        allPos.pop(pos)  # remove the correspond character from allPos(available character)

            hisPosition.append(chaPosition[indChar]) # update the historical position
            goodOne = wordCheck(posChaInWd, word, board, indPos, hisPosition,allPos)
            if goodOne == 1:
                return 1
            else:
                hisPosition.remove(chaPosition[indChar])

