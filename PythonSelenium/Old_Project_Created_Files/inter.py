#list1 = ["Scrips", 123 , 12.4, "python"]
#dic = {"key":"123","pasw":"abc1234"}


def _sum(arr):
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
    return (sum)


# main function
if __name__ == "__main__":
    # input values to list
    arr = [12, 3, 4, 15]
    # calculating length of array
    n = len(arr)
    print(n)
    # calling function ans store the sum in ans
    ans = _sum(arr)
    # display sum
    print('Sum of the array is ', ans)


def largest(arr, n):
        # Initialize maximum element
    max = arr[0]
        # Traverse array elements from second
        # and compare every element with
        # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)




start = 1

end = 10

for i in range(start, end + 1):

    if i % 2 == 0:
        print(i)

print([i for i in range(1, 30) if i % 2 == 0])




