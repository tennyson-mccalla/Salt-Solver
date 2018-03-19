Na_mass = 22.99
Cl_mass = 35.45
Na_frac = 22.99 / (22.99 + 35.45)

butter = float(input("What's a serving size of butter in g? "))

Na = float(input("How much sodium is in a serving in mg? ")) / 1000

salt_serv = (Na / Na_frac) / butter

print(f"A serving has {salt_serv:.3g} g of salt")

b_total = float(input("How much butter does the recipe call for in g? "))

s_added = b_total * salt_serv

s_total = float(input("How much salt does the recipe call for in g? "))

salt_diff = s_total - s_added

message = f"With the salted butter you're using you "\
            f"only need to add {salt_diff:.3g} g."

print(message)
print(f"The butter adds {s_added:.3g} g.")
