class Solution:
	def pushZerosToEnd(self, arr: list[int]) -> None:
    	# code here
    	i=j=0
    	
    	while i<len(arr):
    	   if arr[i] != 0:
    	        arr[i], arr[j] = arr[j], arr[i]
    	        j+=1
    	   i+=1
    	
    	arr[:]=arr
    	return arr
    	       
