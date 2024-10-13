def set_operations(set1, set2):
 union = set1.union(set2)
 intersection = set1.intersection(set2)
 difference = set1.difference(set2)
 return union, intersection, difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union, intersection, difference = set_operations(set_a, set_b)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
