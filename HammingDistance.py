code = [
(1,1,1,1,0),
(0,1,0,0,1),
(1,0,1,0,0),
(1,0,1,0,1),
(0,1,0,1,0),
(0,1,0,1,1),
(0,1,1,1,0),
(0,1,1,1,1),
(1,0,0,1,0),
(1,0,0,1,1),
(1,0,1,1,0),
(1,0,1,1,1),
(1,1,0,1,0),
(1,1,0,1,1),
(1,1,1,0,0),
(1,1,1,0,1)]

def hammingDistance(a, b):
	distance = 0
	for i in range(len(a)):
		distance += a[i]^b[i]
	return distance

def minHammingDist(arr):
	minHammingDistance = len(arr[0])
	for a in arr:
		for b in arr:
			if a != b:
				tempDist = hammingDistance(a, b)
				if tempDist < minHammingDistance:
					minHammingDistance = tempDist
	return minHammingDistance

print ("Minimum Hamming Distance: %i" % minHammingDist(code)


# CS158 HW:
	# Errors Detected where d is distance and e is number of errors detected: d = e + 1.
		# Our min distance is 1 so we can detect 0 errors.
	# Errors corrected where d is distance and e is number of errors corrected: d = 2e+1.
		# Our min distance is 1 so we can detect 0 errors.