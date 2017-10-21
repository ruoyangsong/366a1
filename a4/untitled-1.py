import random
def choose_random_largest(Q):
    old_Q = Q
    Q = sorted(Q,reverse = True)
    choices = []
    for i in range(len(Q)):
        if old_Q[i]==Q[0]:
            choices.append(i)
    #randomly choose from largest estimate actions
    return random.choice(choices)

Q = [-1,-2,-3,-1,0,-6,0]
print choose_random_largest(Q)