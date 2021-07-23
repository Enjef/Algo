import random


class Codec:  # 52.14% 77.59%
    def __init__(self):
        self.data = {}
        self.chars = list(
            range(48, 57+1)) + list(range(65, 90+1)) + list(range(97, 122+1))

    def generate(self):
        short = ''.join([chr(random.choice(self.chars)) for _ in range(6)])
        if short in self.data:
            return self.generate()
        return short

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = self.generate()
        self.data[short] = longUrl
        return f'http://tinyurl.com/{short}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.data[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
