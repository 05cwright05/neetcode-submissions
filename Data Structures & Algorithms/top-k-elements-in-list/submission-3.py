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
        
        output = []
        print(num_counts)
        for i in range(0, k):
            print(num_counts)
            max_value = -1001
            max_key = None
            for key, value in num_counts.items():
                print(key,value)
                if value > max_value:
                    max_value = value
                    max_key = key
            if max_key == None:
                break
            del num_counts[max_key]
            output.append(max_key)
        return output
        