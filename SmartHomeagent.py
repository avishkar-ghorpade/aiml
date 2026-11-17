# SMART CURTAIN AGENT 
class SmartCurtainAgent:
def __init__(self):
self.history = [] # Internal model: stores last 3 light readings
def perceive(self, light_level):
self.history.append(light_level)
if len(self.history) > 3:
self.history.pop(0)
return self.decide_action(light_level)
def decide_action(self, light_level):
if light_level < 300:
action = "Open Curtains"
else:
action = "Close Curtains"
return action
print("SMART CURTAIN AGENT \n")
agent = SmartCurtainAgent()
n = int(input("How many light sensor readings do you want to enter "))
print()
for i in range(n):
print(f"------ Sensor Reading {i+1} ------")
light_level = float(input("Enter Light Intensity (Lux): "))
action = agent.perceive(light_level)
print("\n------ OUTPUT ------")
print(f"Sensor -> Light Intensity : {light_level} Lux")
print(f"Actuator -> {action}")
print(f"Internal Model (Last 3 Light Readings): {agent.history}")
print()
