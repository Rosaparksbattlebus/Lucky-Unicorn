"""Component 5 - Statement formatter v1
"""

decoration = "*"
text = "Hello goodbye"
sides = decoration * 3

formatted_text = f"{sides} {text} {sides}"
top_and_bottom = decoration * len(formatted_text)

print(top_and_bottom)
print(formatted_text)
print(top_and_bottom)