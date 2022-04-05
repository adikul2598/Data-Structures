# in ascending order, then rotated
def countRotations(arr, n):

	# We basically find index
	# of minimum element
	min = arr[0]
	for i in range(0, n):

		if (min > arr[i]):

			min = arr[i]
			min_index = i

	return min_index;


# Driver code
arr = [15, 18, 17, 11, 6, 12]
n = len(arr)
print(countRotations(arr, n))
