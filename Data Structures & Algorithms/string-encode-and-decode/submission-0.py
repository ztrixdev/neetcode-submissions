class Solution:

    def encode(self, strs: List[str]) -> str:
        ec = ""
        for s in strs:
            ec = ec + f"{s}\0"
        return ec
        
    def decode(self, s: str) -> List[str]:
        li = []
        buff = ""
        for c in s:
            if c != "\0":
                buff += c
            elif c == "\0":
                li.append(buff)
                buff = ""
        return li
