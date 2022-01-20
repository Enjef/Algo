class Solution:
    def subdomainVisits(
            self, cpdomains: List[str]) -> List[str]: # 13.07% 17.63%
        count = {}
        for domain in cpdomains:
            qty, dom = domain.split()
            temp = []
            dom = dom.split('.')
            while dom:
                if not temp:
                    temp.append(dom.pop())
                else:
                    temp.append('.'.join([dom.pop(), temp[-1]]))
            for key in temp:
                count[key] = count.get(key, 0) + int(qty)
        return [f'{val} {key}' for key, val in count.items()]

    def subdomainVisits(
            self, cpdomains: List[str]) -> List[str]: # 5.16% 17.63%
        count = {}
        for domain in cpdomains:
            temp = []
            qty, dom = domain.split()
            qty = int(qty)
            dom = dom.split('.')
            while len(dom) > 1:
                temp.append('.'.join(dom))
                dom.pop(0)
            temp.append(dom.pop())
            for key in temp:
                count[key] = count.get(key, 0) + qty
        return [f'{val} {key}' for key, val in count.items()]

    def subdomainVisits_refactored(
            self, cpdomains: List[str]) -> List[str]: # 83.72% 98.57%
        count = {}
        for q_domain in cpdomains:
            qty, sub = q_domain.split()
            qty = int(qty)
            sub = sub.split('.')
            for i in range(len(sub)):
                cur = '.'.join(sub[i:])
                count[cur] = count.get(cur, 0) + qty            
        return [f'{val} {key}' for key, val in count.items()]

    def subdomainVisits_best_speed(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for cpdomain in cpdomains:
            num, string = cpdomain.split(' ')
            frags = string.split('.')
            for index in range(len(frags)):
                hashmap['.'.join(frags[index:])] += int(num)
        return ['{} {}'.format(value, key) for key, value in hashmap.items()] 


