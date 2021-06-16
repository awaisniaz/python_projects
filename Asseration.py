def average(score):
    assert len(score) != 0 ,"This is an empty array"
    return sum(score)/len(score)


scores = []

print(average(scores))