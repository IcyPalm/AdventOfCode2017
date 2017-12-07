with open("inputs/day_06.txt") as f:
    lines = f.readlines()

bank = [int(n) for n in lines[0].split()]

#bank = [0, 2, 7, 0]  # Test values

previous_banks = []
same = False
counter = 0
bank_length = len(bank)

previous_banks.append(list(bank))
while not same:
    counter += 1
    index_max = bank.index(max(bank))
    value_max = bank[index_max]
    bank[index_max] = 0

    while value_max > 0:
        index_max += 1
        if index_max == bank_length:
            index_max = 0
        bank[index_max] += 1
        value_max -= 1
    if bank in previous_banks:
        same = True
    else:
        previous_banks.append(list(bank))

print(counter)
