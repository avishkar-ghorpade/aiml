class Rule:
def __init__(self, premises, conclusion):
self.premises = premises
self.conclusion = conclusion
rules = [
Rule(["DarkClouds", "HighHumidity"], "Rain"),
Rule(["Rain", "StrongWind"], "Storm"),
Rule(["Storm"], "StayHome"),
Rule(["DarkClouds"], "CarryUmbrella"),
Rule(["CarryUmbrella"], "BePrepared"),
Rule(["Rain"], "WetRoad") # Added another rule
]
# FORWARD CHAINING
def forward_chaining(facts, rules):
inferred = set(facts)
print("\nInitial Facts:", inferred)
changed = True
while changed:
changed = False
for rule in rules:
if all(p in inferred for p in rule.premises):
if rule.conclusion not in inferred:
inferred.add(rule.conclusion)
print("Rule Fired:",rule.premises,"->",rule.conclusion)
changed = True
return inferred
# BACKWARD CHAINING
def backward_chaining(goal, facts, rules, visited=None):
if visited is None:
visited = set()
if goal in facts:
print(goal, "is a known fact.")
return True
if goal in visited:
return False
visited.add(goal)
for rule in rules:
if rule.conclusion == goal:
print("\nTrying Rule:",rule.premises,"->",rule.conclusion)
success = True
for premise in rule.premises:
if not backward_chaining(premise,facts,rules,visited):
success = False
break
if success:
print("Goal", goal, "proved.")
return True
return False
# Main Program
facts = {"DarkClouds", "HighHumidity", "StrongWind"}
print(" FORWARD CHAINING ")
result = forward_chaining(facts, rules)
print("\nFinal Facts")
for fact in sorted(result):
print(fact)
goal = "StayHome"
print("\n BACKWARD CHAINING")
if backward_chaining(goal, facts, rules):
print("\nGoal Achieved:", goal)
else:
print("\nGoal Cannot be Proved").
