import numpy as np
a = np.arange(0, 20).reshape((4, 5))
print(f"=>\n{a}\n{'*'*20}")
print(f"=> {a[1, 1]}\n{'*'*20}")
print(f"=>{a[2]}\n{'*'*20}")

# =========================================
for i in range(4):
    for j in range(5):
        a[i, j] = a[i, j]+1

print(f"=>\n{a}\n{'*'*20}")

print(f"=>\n{a[1:, 2:]}\n{'*'*20}")
print(f"=>\n{a[:, 2]}\n{'*'*20}")

# ==========================================
a = np.arange(0, 20).reshape((4, 5))
b = np.copy(a[:, 2])
print(f"=>\n{b}\n{'*'*20}")
print(f"=>\n{b[2]}\n{'*'*20}")

# ==============================================
a = np.arange(0, 20).reshape((4, 5))
b = a[1:, 2:].copy()
print(f"=>\n{b}\n{'*'*20}")

# ============================================
a = np.arange(0, 20).reshape((4, 5))
b = np.diag(a)
print(f"=>\n{a}\n{'*'*20}")
print(f"=>\n{b}\n{'*'*20}")

# ===============================================
a = np.arange(1, 21).reshape((4, 5))
b = np.diag(a, k=1)
print(f"=>\n{a}\n{'*'*20}")
print(f"=> diagonal of a\n{b}\n{'*'*20}")
b = np.diag(a, k=-1)
print(f"=>\n{b}\n{'*'*20}")
b = np.diag(a, k=2)
print(f"=>\n{b}\n{'*'*20}")

# ============================================
a = np.arange(1, 21).reshape((4, 5))
print(f"=>unique of a is: {np.unique(a)}\n{'*'*20}")
print(f"=>a great than 10\n{a > 10}\n{'*'*20}")

# ========================
a = np.array([1, 2, 3, 4, 5])
b = np.array([11, 12, 13, 14, 15])

print(np.intersect1d(a, b))  # taqt3
print(np.setdiff1d(b, a))  # b farq a
print(np.union1d(a, b))  # a itehad b

print(a.searchsorted(2), f"\n{'*'*20}")  # search for item

# ====================================
a = np.array([[50, 22], [1, 60]])
print(np.sort(a))
print(a.sort())
