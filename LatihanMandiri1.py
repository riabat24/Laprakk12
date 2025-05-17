a = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 :60}

print("{:<4} {:<7} {:<5}" .format ("key", "values","item"))
for b, c in a.items():
    print("{:<4} {:<7} {:<5}" .format(b, c, b))
