# Works with numbers or strings
# Random number generator - https://www.calculatorsoup.com/calculators/statistics/number-generator.php
toSort = [66, 82, 85, 69, 85, 43, 38, 84, 42, 55, 56, 70, 4, 70, 90, 85, 46, 32, 66, 30]
n = 0
for x in toSort:
    for index in toSort:
        try:
            if toSort[n] > toSort[n+1]:
                toSort[n], toSort[n+1] = toSort[n+1], toSort[n]
        except IndexError:
            n = 0
            continue
        n += 1
print(toSort)

