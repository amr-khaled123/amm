# --------------
# --- Errors ---
# --------------

# x = -10
# if x < 0 :
#     raise Exception(f"the number {x} is neg")
#     print(f"{x} is neg number")
# else:
#     print(f"{x} is pos num")

y="l"
if type(y)!=int:
    raise ValueError("only numbers allowed")

print("print message after if condition")