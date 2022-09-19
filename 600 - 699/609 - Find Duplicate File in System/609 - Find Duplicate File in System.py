class Solution:
    # 32.88% 24.41%
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for path in paths:
            path_to_file, *files = path.split()
            for file in files:
                filename, content = file.split('(')
                count[content[:-1]].append('/'.join([path_to_file, filename]))
        return [value for value in count.values() if len(value) > 1]

    # 35.76% 24.41%
    def findDuplicate_v2(self, paths: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for path in paths:
            path_to_file, *files = path.split()
            for file in files:
                filename, content = file.split('(')
                count[content].append('/'.join([path_to_file, filename]))
        return [value for value in count.values() if len(value) > 1]

    def findDuplicate_best_speed(self, paths: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for path in paths:
            strs = path.split()
            root = strs[0]
            for s in strs[1:]:
                file_name, _, content = s.partition('(')
                maps[content].append(root+'/'+file_name)
        return [x for x in maps.values() if len(x) > 1]

    def findDuplicate_best_memory(self, paths: List[str]) -> List[List[str]]:
        contentCounts = collections.defaultdict(lambda: 0)
        ans = collections.defaultdict(lambda: [])
        for i in range(len(paths)):
            strings = paths[i].split(" ")
            for s in strings:
                try:
                    content = s[s.index('('):s.index(')') + 1]
                    contentCounts[content] += 1
                except:
                    continue
        for i in range(len(paths)):
            strings = paths[i].split(' ')
            for s in strings:
                try:
                    content = s[s.index('('):s.index(')') + 1]
                    if contentCounts[content] > 1:
                        ans[content].append(
                            strings[0] + '/' + s[0:s.index('(')])
                except:
                    continue
        return ans.values()
