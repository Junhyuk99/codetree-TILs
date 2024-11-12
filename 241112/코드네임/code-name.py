class Agent:
    def __init__(self, code=0, sco=0):
        self.code = code
        self.sco = sco

# agents = [
#     tuple(tuple(input().split()))
#     for _ in range(5)
# ]
agents=[]
for _ in range(5):
    code, sco = tuple( input().split())
    agents.append(Agent(code, int(sco)))

agents.sort(key=lambda x:x.sco)
agent0 = agents[0]
print(f"{agent0.code} {agent0.sco}")