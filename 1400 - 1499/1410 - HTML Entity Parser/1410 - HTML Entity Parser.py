class Solution:
    def entityParser(self, text: str) -> str:  # 5.13% 32.48%
        out = []
        i = 0
        n = len(text)
        while i < n:
            if text[i] == '&':
                if text[i:].startswith('&quot;'):
                    i += 6
                    out.append('"')
                elif text[i:].startswith('&apos;'):
                    i += 6
                    out.append("'")
                elif text[i:].startswith('&amp;'):
                    i += 5
                    out.append('&')
                elif text[i:].startswith('&gt;'):
                    i += 4
                    out.append('>')
                elif text[i:].startswith('&lt;'):
                    i += 4
                    out.append('<')
                elif text[i:].startswith('&frasl;'):
                    i += 7
                    out.append('/')
                else:
                    out.append(text[i])
                    i += 1
            else:
                out.append(text[i])
                i += 1
        return ''.join(out)

    def entityParser_v2(self, text: str) -> str:  # 5.13% 50.43%
        pattern = {
            '&quot;' : '"',
            '&apos;' : "'",
            '&amp;' : '&',
            '&gt;' : '>',
            '&lt;' : '<',
            '&frasl;' : '/'
        }
        out = []
        it = enumerate(text)
        for i, char in it:
            if char == '&':
                for key in pattern:
                    if text[i:].startswith(key):
                        out.append(pattern[key])
                        [next(it) for _ in range(len(key)-1)]
                        break
                else:
                    out.append(char)
            else:
                out.append(char)
        return ''.join(out)
        
    def entityParser_v3(self, text: str) -> str:  # 5.13% 32.48%
        pattern = {
            '&quot;' : '"',
            '&apos;' : "'",
            '&amp;' : '&',
            '&gt;' : '>',
            '&lt;' : '<',
            '&frasl;' : '/'
        }
        out = []
        i = 0
        n = len(text)
        while i < n:
            if text[i] == '&':
                for key in pattern:
                    if text[i:].startswith(key):
                        out.append(pattern[key])
                        i += len(key) - 1
                        break
                else:
                    out.append(text[i])
            else:
                out.append(text[i])
            i += 1
        return ''.join(out)
        
    def entityParser_best_speed(self, text: str) -> str:
            return (text.replace("&quot;", '"').replace("&apos;", "'")
                    .replace("&frasl;", "/").replace("&gt;", ">")
                    .replace("&lt;", "<").replace("&amp;", "&"))

    def entityParser_2nd_best_speed(self, text: str) -> str:
        html_symb = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symb = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym1, formal_sym1 in zip(html_symb, formal_symb):
            text = text.replace( html_sym1 , formal_sym1 )
        
        return text

    def entityParser_3d_best_speed(self, text: str) -> str:
        text = re.sub('&quot;', '\"', text)
        text = re.sub('&apos;', "\'", text)
        text = re.sub('&gt;', '>', text)
        text = re.sub('&lt;', '<', text)
        text = re.sub('&frasl;', '/', text)
        text = re.sub('&amp;', '&', text)
        return text
