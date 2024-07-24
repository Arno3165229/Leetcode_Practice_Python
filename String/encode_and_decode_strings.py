class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" +s
        
        return encode

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decode = []

        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            end = int(str[i:j])
            decode.append(str[j+1:j+1+end])
            i = j + 1 + end

        return decode