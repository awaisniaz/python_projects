import re
paragraph = "I am Pakistan and what about you baby Pakistan"
print(re.match(paragraph,"Pakistan"))
print(re.search("[a-z]",paragraph))
print(re.findall("Pakistan",paragraph))
print()