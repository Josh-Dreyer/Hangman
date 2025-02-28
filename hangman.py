def Hangman(Word):
    wrong = 0
    stages = ["",
              "     ___   ",
              "      |    ",
              "      0    ",
              "     /|\   ",
              "     / \   "
              ]
    rLetters = list(Word)
    board = ["__"] * len(Word)
    Win = False
    print("Welcome to Hangman")
    print("\n", " ".join(board))
    while wrong < len(stages)-1:
        msg = "Please enter a letter? "
        cLetter = input(msg)
        if cLetter in rLetters:
            pos = Word.index(cLetter)
            board[pos] = cLetter
            rLetters[pos] = "$"
        else:
            wrong += 1
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win")
            Win = True
            break
    if not Win:
        print("You lose the word was {}".format(Word))

Hangman("cat"
