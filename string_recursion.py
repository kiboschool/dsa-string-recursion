class String:
    def print_dashed(s):
        if s is None or s == '':
            return
        if len(s) == 1:
            print(s)
            return
        print(s[0], end='-')
        String.print_dashed(s[1:])

    def remove_char(s, c):
        if s is None or s == '':
            return s
        removed_from_rest = String.remove_char(s[1:], c)
        if s[0] == c:
           return removed_from_rest
        else:
           return s[0] + removed_from_rest

    def to_upper_case(s):
        if s is None or s == '':
            return s
        upper_case_rest = String.to_upper_case(s[1:])
        return s[0].upper() + upper_case_rest

    def get_index(s, c):
        if s is None or s == '':
            return -1
        if c is None or c == '':
            return -1
        if s[0] == c:
            return 0
        index_in_rest = String.get_index(s[1:], c)
        if index_in_rest == -1:
            return -1
        else:
            return index_in_rest + 1

    def prune(s):
        if s is None or s == '':
            return -1
        if s[0] == ' ':
            return String.prune(s[1:])
        if s[-1] == ' ':
            return String.prune(s[:-1])
        return s

if __name__ == "__main__":
    String.print_dashed("hello")
