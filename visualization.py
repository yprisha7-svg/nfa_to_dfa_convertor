import graphviz as gph
def nfa(states, transitions):
  graph = gph.Diagraph()
  for s in states:
    graph.node(s)
  for key in transtions:
    start = key[0]
    symbol = key[1]
    for end in tansitions[key]:
      graph.edge("start, end, label = symbol)
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
