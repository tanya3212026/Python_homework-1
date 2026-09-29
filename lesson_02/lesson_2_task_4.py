def fizz_buzz(n):
    for step in range(1, n):
        if step % 3 == 0 and step % 5 == 0:
            print('FizzBuzz')
        elif step % 5 == 0:
            print('Buzz')
        elif step % 3 == 0:
            print('Fizz')
        else:
            print(step)


fizz_buzz(20)
