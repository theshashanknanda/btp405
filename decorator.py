
def decorator(func):
    def wrapper():
        nums = [1,1, 2,3]
        sum = 0

        dict = {}
        for i in nums:
            print(i)
            sum = sum + i

            # counting dict
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1

        print("Sum: ")
        print(sum)

        print("Count: ")
        print(dict)

        func()

    return wrapper

@decorator
def numbers():
    print('inside numbers')

numbers()