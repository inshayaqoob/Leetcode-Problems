class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line, line_length = [], [], 0
    
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '
                result.append(''.join(line))
                line, line_length = [word], len(word)
        
        result.append(' '.join(line).ljust(maxWidth))
        return result