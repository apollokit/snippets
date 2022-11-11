indices = [1,2,3]
yo = 'asdf'
bee = None

# aa = hash(tuple(sorted(indices)))
aa = hash(yo)

# aa = hash(tuple([
#     hash(tuple(sorted(indices))),
#     hash(yo),
#     hash(bee)
#     ]))

print(aa)
a=1