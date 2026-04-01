class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "1234;1234;;;"
        return "_;/;".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "1234;1234;;;":
            return []
        if s == "":
            return [""]
        return s.split("_;/;")