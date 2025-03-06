class Solution:
    # Capital One
    # https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description/?envType=company&envId=capital-one&favoriteSlug=capital-one-all
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        n = len(arrival)
        # Sorted list of free servers (initially all are free)
        free = list(range(k))
        # Min-heap to track busy servers: (finish_time, server_index)
        busy = []
        # Count of requests handled by each server
        count = [0] * k

        for i in range(n):
            # Free any servers that have finished processing by now
            while busy and busy[0][0] <= arrival[i]:
                finish_time, server = heapq.heappop(busy)
                # Insert server back into the sorted free list.
                bisect.insort(free, server)
            
            # If no servers are free, drop the request.
            if not free:
                continue

            # Determine the starting server based on request index.
            start_index = i % k
            # Use binary search to find the first free server with index >= start_index.
            idx = bisect.bisect_left(free, start_index)
            # If no such server exists, wrap around and choose the first free server.
            if idx == len(free):
                idx = 0
            
            server = free.pop(idx)
            count[server] += 1
            # Mark the server as busy until (arrival time + load time)
            heapq.heappush(busy, (arrival[i] + load[i], server))
        
        max_requests = max(count)
        return [i for i, cnt in enumerate(count) if cnt == max_requests]
