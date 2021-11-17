class multifilter:           
    def judge_half(pos, neg):  #да больше нет или столько же
        return pos >= neg

    def judge_any(pos, neg):   #хотя бы одно да
        return pos >= 1

    def judge_all(pos, neg):   #ни одного нет
        return neg == 0
    
    def __init__(self, iterable, *funcs, judge=judge_any):   
        self.iterable = iterable   #послед-ть
        self.funcs = funcs         #рез-ты функций
        self.judge = judge         #рез-т функции сравнения
        
    def __iter__(self):
        for i in self.iterable:   #для всех эл-в послед-ти
            pos = 0
            neg = 0
            for f in self.funcs:  #для всех рез-в функций
                if f(i):  #True
                    pos += 1
                else:     #False
                    neg += 1
            if self.judge(pos, neg):  #True
                yield i               #вернуть эл-т послед-ти
