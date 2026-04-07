class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def backtrack(path, index, target):
            if target == 0:
                to_add = path.copy()
                answer.append(to_add)
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    # take this number
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    path.append(candidates[i])
                    backtrack(path, i+1, target - candidates[i])
                    path.pop()

        backtrack([], 0, target)
        return answer
