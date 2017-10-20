# test case
import recursiveMethods as recMethod

board=[["A","Q","A","H"],
       ["A","X","V","W"],
       ["A","L","T","I"],
       ["T","T","J","I"]]

# board=[["C","B","C","H"],
#        ["C","B","V","B"],
#        ["A","L","T","R"],
#        ["A","T","E","O"]]

words = ["LACBCBB", "TAXA", "AXOLOTL", "ABA", "VITA", "VITTA", "GO", "AXAL", "TALA"]

# board=[["S","A"],
#        ["M","O"],
#        ["W","E"],
#        ["H","R"]]
#
# words = ["WHERE", "SOME", "DRONE", "SOMEWHERE", "WORD", "WE", "MORE"]

# board = [["G","T"],
#          ["O","A"]]
# words = ["TOGGLE", "GOAT", "TOO", "GO"]


#board = [["R", "L", "D"],
#         ["U", "O", "E"],
#         ["C", "S", "O"]]

#words = ["CODE","SOLO","RULES","COOL"]

# test the functions
def wordBoggle(board, words):
    goodword=[]
    for indWords in range(0,len(words)):
        lenWd = len(words[indWords])
        position = []
        histPos = []
        availPos = []
        avaiii = recMethod.wordCheck(lenWd,words[indWords],board,position,histPos,availPos)
        if avaiii == 1:
            goodword.append(words[indWords])
    goodword.sort()
    return goodword

if __name__ == "__main__":
    testword = wordBoggle(board,words)
    print("find correct words: ", testword)