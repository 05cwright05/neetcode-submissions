class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O (kn) = O(kn) if we just hash them in a count dict and tehn iterate through all of tehm again to find teh k highest 
        # O(2n) = O(n) if we store the go thru and form a list in order, adn tehn return the top k.


        num_counts = {}
        for number in nums:
            if num_counts.get(number) == None:
                num_counts[number] = 1
            else:
                num_counts[number] += 1
        
        #crazy shit right here we are gonna make a list where the index is teh number of times and jawn at the bottom is the list of numbers pretaining to that
        # so we got O n+n+n+n.. but no loopy
        buckets_of_wrath = [[] for _ in range(0, len(nums))]
        #put them in the jawn
        for key, value in num_counts.items():
            buckets_of_wrath[value - 1].append(key)

        

        last_index = len(nums) - 1
        output = []

        while k > 0:
            curr_list = buckets_of_wrath[last_index]
            if len(curr_list) == 0:
                last_index -=1
                continue
            else:
                output.append(curr_list.pop())
                k-=1

        return output