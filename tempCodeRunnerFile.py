    print(f'\tQuestion 1: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations

        if isAnswerCorrect(QUESTIONS[i], int(ans),  ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
