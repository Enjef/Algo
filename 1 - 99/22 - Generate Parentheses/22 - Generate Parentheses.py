class Solution:
    def generateParenthesis(self, n: int) -> List[str]:  # 96.05% 41.10%
        # result for n == 3: ["()()()","()(())","(())()","(()())","((()))"]
        def generate(left, right, cur, out=[]):
            if not left and not right:
                out.append(cur)
            if right and right > left:
                generate(left, right-1, cur+')', out)
            if left:
                generate(left-1, right, cur+'(', out)
            return out
        return generate(n, n, '')

    def generateParenthesis_left(self, n: int) -> List[str]:  # 87.33% 41.10%
        # result for n == 3: ["((()))","(()())","(())()","()(())","()()()"]
        def generate(left, right, cur, out=[]):
            if not left and not right:
                out.append(cur)
            if left:
                generate(left-1, right, cur+'(', out)
            if right and right > left:
                generate(left, right-1, cur+')', out)
            return out
        return generate(n, n, '')

    cache = {}
    def generateParenthesis_best_speed(self, n: int):
        return self.fun(n, 0)
        
    def fun(self, n, to_close):
        if (n, to_close) in self.cache:
            return self.cache[(n, to_close)]
        out = set()
        if to_close == 0 and n == 0:
            return {""}
        else:
            if n >= 1:
                out = {"(" + x for x in self.fun(n-1, to_close+1)}
            if to_close >= 1:
                close_out = {")" + x for x in self.fun(n, to_close-1)}
                out = out.union(close_out)
        self.cache[(n, to_close)] = out
        return out

    def bfs(self, n, visited: List[str]):
        def can_add_right(s: str):
            return s.count("(") > s.count(")")
        def can_add_left(s: str):
            return s.count("(") < n

        left = [l + "(" for l in visited if can_add_left(l)]
        right = [r + ")" for r in visited if can_add_right(r)]
        if len(left + right) > 0:
            return self.bfs(n, left + right)
        else:
            return visited

    def generateParenthesis_2nd_to_best_speed(self, n: int) -> List[str]:
        return set(self.bfs(n, ["("]))
