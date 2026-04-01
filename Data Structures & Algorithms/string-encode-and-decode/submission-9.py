class Solution:

    def encode(self, strs: List[str]) -> str:
        # faster than using string class since strings are immutable in python
        output_list = []
        for s in strs:
            output_list.append(str(len(s)))
            #delimit
            output_list.append('#')
            output_list.append(s)
        if len(output_list) == 0:
            return "#"
        return "".join(output_list)


    def decode(self, s: str) -> List[str]:
        current_index = 0
        output = []
        print(f"Input {s}")

        while current_index < len(s):
            num_to_munch = ""
            while s[current_index] != '#':
                num_to_munch += s[current_index]
                current_index += 1
            #account for eating the hastag
            current_index+=1
            if num_to_munch == '':
                return []
            num_to_munch = int(num_to_munch)
            print("THE NUM TO MUNCH", num_to_munch)
            current_string = []
            for i in range(current_index, num_to_munch + current_index):
                current_string.append(s[i])
            output.append("".join(current_string))
            current_index += num_to_munch
        print(output)
        return output