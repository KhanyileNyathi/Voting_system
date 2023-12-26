# candidates
candidate_1 = input('Enter candidate name : ')
candidate_2 = input('Enter candidate name : ')

candidate1 = 0
candidate2 = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
no_of_voters = len(voter_id)
voter = int(input('Enter voter id : '))
vote = int(input('Enter your vote Here : '))
if vote == 1:
    candidate1 += 1
    print('thank you for voting', candidate_1)
elif vote == 2:
    candidate2 += 1
    print('thank you for voting', candidate_2)
elif vote > 2:
    print('ERROR:WRONG KEY')
else:
    print('you cannot vote again')
if voter is voter_id:
    print('Thank you for voting')
    voter_id.remove(voter)
    print('******************************************')
    print('To give ', candidate_1, 'your vote PRESS 1')
    print('To give ', candidate_2, 'your vote PRESS 2')
    print('******************************************')

while True:
    # complete voter list
    if voter_id is []:
        print('The voting session has ended')

        if candidate1 < candidate2:
            # calculate percentage
            percent = (candidate1 / no_of_voters) * 100
            print(candidate_1, 'has won the election with', percent, '%')
            break
        elif candidate1 > candidate2:
            percent = (candidate2 / no_of_voters) * 100
            print(candidate_2, 'has won the election with', percent, '%')
            break

        else:
            print('its a draw, Government wil decide the next step')
            break
