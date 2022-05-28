class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(int)
        val_max = -1
        for i in range(len(messages)):
            counter[senders[i]] += len(messages[i].split())
            val_max = max(val_max, counter[senders[i]])
        return sorted([x for x in counter if counter[x] == val_max]).pop()
