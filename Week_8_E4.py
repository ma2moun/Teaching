# nest while loops to create coordinates from (0,0) to (10,10)

i = 0
while i <= 10:
    j = 0
    while j <= 10:
        print(f"({i},{j})")
        j = j + 1
    i = i + 1
