class Solution:
    def groupAnagrams(
            self,
            strs: List[str]) -> List[List[str]]:  # 68.95% 52.70%
        count = {}
        for word in strs:
            key = tuple(sorted(word))
            count[key] = count.get(key, []) + [word]
        return list(count.values())

    def groupAnagrams_best_speed(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        dict ={}
        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord not in dict:
                dict[sortedWord] = [s]
            else:
                dict[sortedWord].append(s)
        for key, item in dict.items():
            anagrams.append(item)
        return anagrams

    def groupAnagrams_best_memory(self, strs: List[str]) -> List[List[str]]:
        results = []
        for word in strs:
            flag = False
            for result in results:
                if (
                        len(result[0]) == len(word) and
                        sorted(result[0]) == sorted(word)):
                    result.append(word)
                    flag = True
            if not flag:
                results.append([word])
        return results
