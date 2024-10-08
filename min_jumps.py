def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        
        res = 0  # Number of jumps
        l = r = 0  # Current range of jumps
        
        while r < n - 1:
            farthest = 0
            
            for i in range(l, r + 1):
                farthest = max(farthest, i + arr[i])
            
            if farthest <= r:  # If farthest doesn't move forward, we can't reach the end
                return -1
            
            l = r + 1  # Move the left boundary to the right end of the current range
            r = farthest  # Update the right boundary to the farthest we can reach
            res += 1
            
        return res