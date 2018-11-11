"""
Published by: Khalib Baker, President
Organization: Data and Cloud Computing Society

This challenge was posted on HackerRank.com. The link to the challenge description
is posted in the link below:
url -> https://www.hackerrank.com/challenges/the-minion-game/problem

"""
import re
def minion_game():
    string = 'BANANANAAAS'
    # Find the starting letter for each playerOne
        # PlayerOne must start with constanant
        # PlayerTwo must start with vowel

    # PlayerOne: Getting Possible Combinations
    playerOne_combinations = []
    for charIndex in range(0, len(string)):
        # Solo characters
        if string[charIndex] not in 'AEIOU':
            if string[charIndex] not in playerOne_combinations:
                playerOne_combinations.append(string[charIndex])

            for ii in range(charIndex + 1, len(string)+1):
                if string[charIndex: ii] not in playerOne_combinations:
                    playerOne_combinations.append(string[charIndex: ii])

    # PlayerTwo: Getting Possible Combintations
    playerTwo_combinations = []
    for charIndex in range(0, len(string)):
        # Solo characters
        if string[charIndex] in 'AEIOU':
            if string[charIndex] not in playerTwo_combinations:
                playerTwo_combinations.append(string[charIndex])

            for ii in range(charIndex + 1, len(string) + 1):
                if string[charIndex: ii] not in playerTwo_combinations:
                    playerTwo_combinations.append(string[charIndex: ii])

    # PlayerOne: Scoring
    playerOne_score = 0
    for combo in playerOne_combinations:
        playerOne_score += len(re.findall('(?=%s)' % combo, string))

    # PlayerTwo: Scoring
    playerTwo_score = 0
    for combo in playerTwo_combinations:
        playerTwo_score += len(re.findall('(?=%s)' % combo, string))
        #print(string.count(combo))

    # Get Winner
    if playerOne_score == playerTwo_score:
        print('Draw')
    elif playerOne_score > playerTwo_score:
        print('Stuart', playerOne_score)
    else:
        print('Kevin', playerTwo_score)
#len(re.findall('(?=11)', text))


if __name__ == '__main__':
    minion_game()
