from mini_agent import Agent

for tok in Agent().stream('tell me a joke'):
    print(tok, end='')
