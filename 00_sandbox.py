greeting = "hello world"
side = "*" * 3

greeting = "{} {} {}".format(side , greeting, side)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)
