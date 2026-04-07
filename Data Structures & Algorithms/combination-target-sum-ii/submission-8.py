class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def backtrack(path, index, target):
            if target < 0:
                return
            if target == 0:
                to_add = path.copy()
                answer.append(to_add)
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    # i > index means that this is not the first value we are considering in this branch
                    # since if i = index that means we are looking at the very next thing since we upped i to get here
                    # so only ban that value if we haev already passed up on it basically
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    path.append(candidates[i])
                    backtrack(path, i+1, target - candidates[i])
                    path.pop()

        backtrack([], 0, target)
        return answer
