class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where:
        # key   = sorted version of the word
        # value = list of words that match that sorted pattern
        groups = defaultdict(list)

        # Loop through each word in the input list
        for word in strs:
            # Sort the word alphabetically
            # Example:
            # "eat" -> "aet"
            # "tea" -> "aet"
            # Both will have the same key
            key = ''.join(sorted(word))

            # Add the word into the correct anagram group
            groups[key].append(word)

        # Return only the grouped lists
        # groups.values() gives:
        # dict_values([['eat', 'tea', 'ate'], ['tan', 'nat']])
        # Convert it into a normal list
        return list(groups.values())