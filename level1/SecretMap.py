def solution(n, arr1, arr2):

    def binary(arr):
        for i in range(n):
            arr[i] = bin(arr[i])[2:]
            if len(arr[i]) != n:
                arr[i] = arr[i].zfill(n)
        return arr
    answer = []
    letter = ''
    for x, y in zip(binary(arr1), binary(arr2)):
        x = list(x)
        y = list(y)
        for a, b in zip(x, y):
            if a == '1' or b == '1':
                letter += '#'
            else:
                letter += ' '
        answer.append(letter)
        letter = ''
    return answer
