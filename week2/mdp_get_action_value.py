
def get_action_value(mdp, state_values, state, action, gamma):
    """ Computes Q(s,a) as in formula above """

    # YOUR CODE HERE
    next_states=mdp.get_next_states(state, action) # next states for current state and action
    sum_q=0 # Initial value of sum
    
    for nxt_st in next_states:
        sum_q+=next_states[nxt_st]*(mdp.get_reward(state, action, nxt_st)+gamma*state_values[nxt_st]) # Qi formula

    return sum_q
