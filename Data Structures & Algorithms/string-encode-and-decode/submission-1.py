class Solution:
   

    def encode(self, strs: List[str]) -> str:
        delimintator = chr(31)
        total = ""
        for element in strs:
            total += (element + delimintator)
        return total
        

    def decode(self, s: str) -> List[str]:
        delimintator = chr(31)
        list_of_all_elements = []
        last_deliminator_index = 0;
        for i in range(len(s)):
            if (s[i] == delimintator):
                list_of_all_elements.append(
                    s[last_deliminator_index:i])
                last_deliminator_index = i + 1;
        return list_of_all_elements
            
