# frozenset are immutable -> not changable and can not allow duplicate values
# used as dictionary keys and elemnts of other sets

f1 = frozenset([0,1,2,3,4,5,"mom"])
f2 = frozenset([0,3,8,4,5,6,2,"sis"])
print(f1)
print(f2)

union = f1.union(f2)
intersection = f1.intersection(f2)
difference = f1.difference(f2)
print("union:",union)
print("intersection:",union)
print("difference:",union)

# used in dictionaries
dic_with_frozenset = {f1:"val 1",f2:"val 2"}
print("dic_with_frozenset:",dic_with_frozenset)

# set of frozen sets
print(" set of frozen sets:",{f1,f2})



