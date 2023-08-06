count = 0
for x1 in range(0,4):
    for x2 in range(1,4):
        for x3 in range(15,22):
            for x4 in range(0,22):
                for x5 in range(0,22):
                    sum = x1+x2+x3+x4+x5
                    if sum == 21:
                        count += 1

print(count)