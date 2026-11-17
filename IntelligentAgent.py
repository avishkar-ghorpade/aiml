import random
from datetime import datetime
print("=" * 50)
print(" Student Assistant ChatBot")
print("Type 'exit' to end the chat.")
print("=" * 50)
responses = {
"hello": [
"Hello Student!",
"Hi! How can I help you today?",
"Welcome! Ready to learn?"
],
"bye": [
"Goodbye!",
"See you again!",
"Best of luck with your studies!"
],
"python": [
"Python is easy to learn and widely used.",
"Python is popular for AI, Web Development, and Data Science."
],
"java": [
"Java is an Object-Oriented Programming language.",
"Java is used for Android and Enterprise applications."
],
"c": [
"C is a powerful procedural programming language.",
"C is the foundation of many modern programming languages."
],
"exam": [
"Practice previous question papers regularly.",
"Understand concepts instead of memorizing."
],
"motivation": [
"Success comes from consistency!",
"Never stop learning.",
"Believe in yourself and keep coding."
]
}
facts = [
"The first computer programmer was Ada Lovelace.",
"Python was created by Guido van Rossum in 1991.",
"The first computer bug was an actual moth."
]
while True:
user = input("\nYou: ").lower()
if user == "exit":
print("Bot: Goodbye! Happy Coding!")
break
elif "time" in user:
print("Bot:", datetime.now().strftime("%I:%M:%S %p"))
elif "date" in user:
print("Bot:", datetime.now().strftime("%d-%m-%Y"))
elif "fact" in user:
print("Bot:", random.choice(facts))
elif "marks" in user:
try:
marks = float(input("Enter your marks: "))
if marks >= 90:
print("Bot: Excellent! Grade: A+")
elif marks >= 75:
print("Bot: Very Good! Grade: A")
elif marks >= 60:
print("Bot: Good! Grade: B")
elif marks >= 40:
print("Bot: Pass. Grade: C")
else:
print("Bot: Fail. Work harder!")
except:
print("Bot: Invalid input.")
elif user.startswith("calculate"):
try:
expression = user.replace("calculate", "")
result = eval(expression)
print("Bot: Answer =", result)
except:
print("Bot: Invalid calculation.")
else:
found = False
for keyword in responses:
if keyword in user:
print("Bot:", random.choice(responses[keyword]))
found = True
break
if not found:
print("Bot: Sorry, I don't understand that.")
