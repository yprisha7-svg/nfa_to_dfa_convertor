def convert_to_dfa(states, symbols, start_state, transitions):
    dfa_states = []
    dfa_trans = {}
    initial_set = [initial_state]
    queue = []
    queue.append(initial_set)
    dfa_states.append(intial_set)
    steps = []
    while queue:
        current_state = queue.pop(0)
        steps.append(f"Processing state: {current_state}")
        for symbol in symbols:
            next_states = []
            for state in current_state:
                key = (state, symbol)
                if key in transitions:
                    for s in transitions[key]:
                        if s not in next_states:
                            next_states.append(s)
            next_states.sort()
            if next_states == []:
                next_states = ["∅"]
            steps.append(f"δ({current_state},{symbol}) = {next_states}")
            dfa_trans[(tuple(current_state), symbol)] = next_states
            if next_states not in dfa_states:
                dfa_states.append(next_states)
                queue.append(next_states)
    if ["∅"] in dfa_states:
        for symbol in symbols:
            dfa_trans[(("∅",), symbol)] = ["∅"]
    return dfa_states, dfa_trans, steps
