class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }
        for entity in entities.items():
            text = text.replace(entity[0], entity[1])

        return text


t = "&amp; is an HTML entity but &ambassador; is not."
sol = Solution()
sol.entityParser(t)

