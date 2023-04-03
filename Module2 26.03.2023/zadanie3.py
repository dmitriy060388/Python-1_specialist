hour = int(input())
minutes = int(input())

if hour >= 0 and hour < 24 and 0 <= minutes < 60:
    print('Can')
else:
    print('Can"t')
    