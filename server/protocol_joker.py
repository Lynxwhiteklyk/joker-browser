class JokerProtocol:
    def __init__(self):
        self.protocol = "joker://"

    def parse_url(self, url):
        if url.startswith(self.protocol):
            path = url[len(self.protocol):]
            return path
        else:
            raise ValueError("Invalid URL format")

    def build_url(self, path):
        return self.protocol + path
