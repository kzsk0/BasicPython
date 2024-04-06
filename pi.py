text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
txt = list(map(len,text.replace(",", " ").replace(".", " ").split()))
print(txt)

result = "".join(map(str,txt))

print(result)
