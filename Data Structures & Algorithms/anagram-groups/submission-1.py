class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_of_freq_maps = dict()

        for element in strs:
            freq_map = [0] * 26

            for char in element:
                freq_map[ord(char) - ord('a')] += 1

            freq_map = tuple(freq_map)

            if freq_map in set_of_freq_maps:
                set_of_freq_maps[freq_map].append(element)
            else:
                set_of_freq_maps[freq_map] = [element]

        return list(set_of_freq_maps.values())