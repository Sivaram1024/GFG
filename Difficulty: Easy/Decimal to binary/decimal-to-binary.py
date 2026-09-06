class Solution:
    def decToBinary(self, n):
        # code here
        n = int(n)
        binary = bin(n)[2:]
        
        return binary