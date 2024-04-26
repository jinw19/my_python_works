print("-" * 30)
print("1-) C to F")
print("2-= F to C")
print("-" * 30)

choice = input("Your Choice 1/2:")

if choice == "1":
    print("\n# C to F")
    C = float(input("Degree to convert:"))
    F = (C * 1.8) + 32
    print("{} Derece C {} Derece F'ye esittir.".format(C,F))
elif choice == "2":
    print("\n# F to C")
    F = float(input("Degree to convert:"))
    C = (F - 32) * 1.8
    print("{} Derce F {} Derece C'ye esittir.".format(F,C))
else:
    print("lutfen gecerli bir secenegi seciniz")
