class Allocator:
    def __init__(self):
        self.abs_cnt = 0
        self.match_cnt = 0
    
    def new_abs(self):
        ret = '_Abs{}'.format(self.abs_cnt)
        self.abs_cnt = self.abs_cnt + 1
        return ret
    
    def new_match(self):
        ret = '_Match{}'.format(self.match_cnt)
        self.match_cnt = self.match_cnt + 1
        return ret