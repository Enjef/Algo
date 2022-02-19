class Solution:
    def findSubstring(self, s: str, words) -> List[int]: # 40.60% 67.35%
        target = {}
        for word in words:
            target[word] = target.get(word, 0) + 1
        step = len(words[0])
        win = len(words)*step
        out = []
        for i in range(len(s)-win+1):
            test = dict(zip(target.keys(), [0]*len(target)))
            for j in range(i, i+win, step):
                if s[j:j+step] not in test:
                    break
                test[s[j:j+step]] += 1
                if test[s[j:j+step]] > target[s[j:j+step]]:
                    break
            else:
                out.append(i)
        return out

    def findSubstring_v2_copy_target(self, s, words): # 39.85% 93.35%
        target = {}
        for word in words:
            target[word] = target.get(word, 0) + 1
        step = len(words[0])
        win = len(words)*step
        out = []
        for i in range(len(s)-win+1):
            test = target.copy()
            for j in range(i, i+win, step):
                if s[j:j+step] not in test:
                    break
                test[s[j:j+step]] -= 1
                if test[s[j:j+step]] < 0:
                    break
            else:
                out.append(i)
        return out

    def findSubstring_best_speed(self, s, words):
        if not s or words==[]:
            return []
        lenstr=len(s)
        lenword=len(words[0])
        lensubstr=len(words)*lenword
        times={}
        for word in words:
            if word in times:
                times[word]+=1
            else:
                times[word]=1
        ans=[]
        for i in range(min(lenword,lenstr-lensubstr+1)):
            self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
        return ans
    
    def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
        wordstart=strstart
        curr={}
        while strstart+lensubstr<=lenstr:
            word=s[wordstart:wordstart+lenword]
            wordstart+=lenword
            if word not in times:
                strstart=wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+lenword]]-=1
                    strstart+=lenword
                if wordstart-strstart==lensubstr:
                    ans.append(strstart)
        
    def findSubstring_best_memory(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        k = len(words[0])
        target = ''.join(sorted(words))
        ans = []
        for i in range(len(s) - n * k + 1):
            given = ''.join(sorted([s[i+a*k:i+a*k+k] for a in range(n)]))
            if target == given:
                ans.append(i)
        return ans

    def findSubstring_2nd_best_memory(self, s, words):
        indices = []
        if s is None or len(s) == 0 or words is None or len(words) == 0:
            return indices
        wordCount = dict()
        for i in range(len(words)):
            if words[i] in wordCount:
                wordCount[words[i]] += 1
            else:
                wordCount[words[i]] = 1
        wordLength = len(words[0])
        wordArrayLength = wordLength * len(words)
        for i in range(0, len(s) - wordArrayLength + 1):
            current = s[i:i + wordArrayLength]
            wordMap = dict()
            index = 0
            j = 0
            while index < len(words):
                part = current[j: j + wordLength]
                if part in wordMap:
                    wordMap[part] += 1
                else:
                    wordMap[part] = 1
                j += wordLength
                index += 1
            if wordMap == wordCount:
                indices.append(i)
        return indices
