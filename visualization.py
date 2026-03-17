import graphviz as gph
def nfa(states, symbols, initial_state, final_states, transitions):
  graph = gph.Digraph()
  for s in states:
    if s in final_states:
      graph.node(s, shape="doublecircle")
    else:
      graph.node(s)
  for key in transitions:
    start = key[0]
    symbol = key[1]
    for end in transitions[key]:
      graph.edge(start, end, label = symbol)
  return graph
def dfa(dfa_states, dfa_trans):
    graph = gph.Digraph()
    for s in dfa_states:
        graph.node(str(s))
    for key in dfa_trans:
        start = str(list(key[0]))
        symbol = key[1]
        end = str(dfa_trans[key])
        graph.edge(start, end, label=symbol)
    return graph
