import random
sum = input('see your capital')
arr = [random.randint(1, 50) for i in range(1)]
num = input('enter a number')
if num == arr:
    sum= sum*1,25
    print('your capital has doubled')

else:
    sum = sum * 0,75
    x=print('YOU HAVE LOST 25% OF YOUR CAPITAL. But you can win 50% in our super game')
    super = input('if you want to play a super game write yes otherwise no')
    superarr = [random.randint(1, 100) for i in range(1)]
if x == 'yes':
    if super==superarr:
        sum * 1,50
        print('you have won the super game')
    else:
        sum = sum / 0,5
        print('you have lost a super game')

else:
    print(num)
    print('goodbay')