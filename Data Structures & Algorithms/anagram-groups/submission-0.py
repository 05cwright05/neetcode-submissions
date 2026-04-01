class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy_strs = strs.copy()
        word_dict = {}
        for i in range(0, len(copy_strs)):
            copy_strs[i] = "".join(sorted(copy_strs[i]))
            if word_dict.get(copy_strs[i]):
                word_dict[copy_strs[i]].append(i)
            else:
                word_dict[copy_strs[i]] = [i]

        list_of_lists = []

        for value in word_dict.values():
            new_list = []
            for i in value:
                new_list.append(strs[i])
            list_of_lists.append(new_list)
        return list_of_lists

        