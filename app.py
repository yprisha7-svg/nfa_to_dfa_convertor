import streamlit as st
from subset_construction import convert_to_dfa
from visualization import nfa, dfa
st.title("NFA To DFA Converter Using Subset Construction Method")
#Input NFA details
states_input = st.text_input("Enter states (example: q0,q1,A,B): ")
symbols_input = st.text_input("Enter symbols (for ex: a,b,0,1): ")
initial_state = st.text_input("Enter initial state: ")
initial_state = intial_state.strip()
final_state = st.text_input("Enter final state: ")
states = []
for s in states_input.split(","):
    remspace = s.strip()
    states.append(remspace)
symbols = []
for s in symbols_input.split(","):
    remspace = s.strip()
    symbols.append(remspace)
final_states = []
for s in final_state.split(","):
    remspace = s.strip()
    final_states.append(remspace)
st.write("Enter transitions like:\n q0,a=q0,q1 ")
transitions_input = st.text_area("Enter transitions as mentioned above: ")
def read_transitions(text):
  transitions = {}
  trans =  text.split("\n")
  for lines in trans:
    if "=" in lines:
      left, right = lines.split("=")
      state, symbol = left.split(",")
      next_states = right.split(",")
  transitions[(state, symbol)] = next_states
  return transitions
if st.button("Convert"):
  states = states_input.split(",")
  symbols = symbols_input.split(",")
  final_states = final_state.split(",")
  transitions = read_transitions(transitions_input)
  dfa_states, dfa_trans, steps = convert_to_dfa(
        states, symbols, initial_state, transitions, final_states
    )
  st.subheader("NFA Details:")
  st.write("States:", states)
  st.write("Symbols:", symbols)
  st.write("Initial state:", initial_state)
  st.write("Final states:", final_states)
  for key in transitions:
        st.write(key[0], ",", key[1], "--->", transitions[key])
  #NFA Diagram
  st.subheader("NFA Diagram")
  st.graphviz_chart(nfa(states, symbols, initial_state, final_states, transitions))
  st.subheader("Subset Construction Steps")
  for s in steps:
    st.write(s)
  #Conversion to DFA
  st.subheader("DFA States")
  for s in dfa_states:
    st.write(s)
  st.subheader("DFA Transition Table")
  for key in dfa_trans:
    start = list(key[0])
    symbol = key[1]
    end = dfa_trans[key]
    st.write(start, "--", symbol, "-->", end)
  st.subheader("DFA Diagram")
  st.graphviz_chart(dfa(dfa_states, dfa_trans))

  
