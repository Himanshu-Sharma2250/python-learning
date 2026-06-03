class A:
    label = "A: Base Class"

class B(A):
    label = "B: Child of A"

class C(A):
    label = "C: Child of A"

class D(B, C):
    pass

d = D()

print(d.label)
print(D.__mro__)