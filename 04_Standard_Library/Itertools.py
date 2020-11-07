import itertools

# ========================
# ========================
# Endless....iterator...
# ========================
# ========================

# 0부터 시작, 12씩 증가
iter = itertools.count(0, 12)
for i in iter:
    print(i)
    if i > 100: break

# "ABCD" 반복
iter = itertools.cycle("ABCD")
for idx, i in enumerate(iter):
    print(i)
    if idx > 100: break

# element를 n번 반복
iter = itertools.repeat("as", 9)
for idx, i in enumerate(iter):
    print(i)
    if idx > 100: break


# ========================
# ========================
# Combination....iterator...
# ========================
# ========================

#(ABCD, ABCD)
iter = itertools.product("ABCD", repeat=2)
for idx, i in enumerate(iter):
    print(i)
    if idx > 100: break
print("")

# (A, BCD), (B, ACD), (C, ABD), (D, ABC)
iter = itertools.permutations("ABCD", 2)
for idx, i in enumerate(iter):
    print(i)
    if idx > 100: break
print("")


iter = itertools.combinations("ABCD", 2)
for idx, i in enumerate(iter):
    print(i)
    if idx > 100: break
print("")

iter = itertools.combinations_with_replacement("ABCD", 2)
for idx, i in enumerate(iter):
    print(i)
    if idx > 100: break