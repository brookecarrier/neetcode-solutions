class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        #len then # then word
        for string in strs:
            lenStr = str(len(string))
            result += lenStr + '#' + string
        
        return result



    def decode(self, s: str) -> List[str]:

        result = []

        pointer = 0;
        while pointer < len(s):
            lenStr = ""
            while s[pointer] != '#':
                lenStr += s[pointer]
                pointer += 1

            pointer += 1
            string = ""
            for i in range(int(lenStr)):
                string += s[pointer]
                pointer += 1
            
            result.append(string)
        
        return result
        


        

