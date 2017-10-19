from utils import rand_in_range, rand_un
action=["up","down","left","right","upleft","upright","downleft","downright"]
action_index = rand_in_range(len(action))
print action[action_index]