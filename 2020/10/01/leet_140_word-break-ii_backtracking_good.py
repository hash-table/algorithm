

# leet_140_word-break-ii_backtracking_good
# - _leet 
# - _backtracking
# - _good
# - _backtracking_good
# 2020100415
# 202010042230 202010042254

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        
            problem
                non-empty string s가 있음
                s에 적절하게 white space를 넣는다고 하자. 그럼 s가 white space 기준으로 쪼개지지
                이 때 모든 token이 wordDict에 있게 쪼갤꺼야
                그럼 만들 수 있는 모든 가지수는 ? 
                s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]                
                => 
                    [
                      "cats and dog",
                      "cat sand dog"
                    ]

            idea
            
                cache = dict()
                # cache['catsanddog'] = [ [cats, and, dog],[cat, sand, dog]]
                aux = defaultdict(lambda : [])
                for word in wordDict:
                    aux[word[0]].append(word)
                for k in aux:
                    aux[k].sort(key = len)
                    
                    
                # 실패하는 case에 대해서는 안넘겨야 한다. 근데 이게 끝까지 가야 알 수 있어. 
                # 그럼 이게 실패했는지, 안했는지에 대해 뭔가 분기를 넘겨야 하는데 이거 설계하는데 있어서 바로바로 나오지가 않는다. 
                # base case일 때의 고민을 해야한다 
                # 내려갔는데 더이상 만들어지지 않는 경우에 대한 고민이야 
                len_s = len(s)
                def func(sidx) -> List[List[]]:
                    # cache[s[sidx:]] 를 채운다
                    nonlocal s, aux, cache, len_s
                    # 다음 분기 태울때 길이 맞게 넘겨야함
                    if sidx == len_s:
                        return ['']
                    elif sidx > len_s:
                        return []
                    else:
                        ret = []
                        for cand in aux[s[sidx]]:
                            if s.startswith(cand, sidx):
                                next_answer = func(sidx + len(cand))
                                for na in next_answer:
                                    ret.append([cand] + na)
                    return ret
                    
                func(0)
                
                return [ ' '.join(_) for _ in cache[s]]
            
            well-formed


                cache = dict()
                aux = defaultdict(lambda : [])
                
                for word in wordDict:
                    aux[word[0]].append(word)
                for k in aux:
                    aux[k].sort(key = len)    
                len_s = len(s)
                
                def func(sidx) -> List[List[]]:
                    nonlocal s, aux, cache, len_s
                    if cahce.get(s[sidx:], None) != None:
                        return cache[s[sidx:]]
                    else:
                        if sidx == len_s:
                            return ['']
                        elif sidx > len_s:
                            return []
                        else:
                            ret = []
                            for cand in aux[s[sidx]]:
                                if s.startswith(cand, sidx):
                                    next_answer = func(sidx + len(cand))
                                    for na in next_answer:
                                        ret.append([cand] + na)
                            return ret
                func(0)
                return [ ' '.join(_) for _ in cache[s]]

            
            test
        '''
        cache = dict()
        aux = defaultdict(lambda : [])

        for word in wordDict:
            aux[word[0]].append(word)
        
        for k in aux:
            aux[k].sort(key = len)    
        
        len_s = len(s)
        def func(sidx) -> List[List[str]]:
            nonlocal s, aux, cache, len_s
            if cache.get(s[sidx:], None) != None:
                return cache[s[sidx:]]
            else:
                if sidx == len_s:
                    return [[]]
                elif sidx > len_s:
                    return []
                else:
                    ret = []
                    for cand in aux[s[sidx]]:
                        if s.startswith(cand, sidx):
                            next_answer = func(sidx + len(cand))
                            for na in next_answer:
                                ret.append([cand] + na)
                    cache[s[sidx:]] = ret
                    return ret
        
        func(0)
        return [ ' '.join(_) for _ in cache[s]]
    
    '''    
        Runtime: 36 ms, faster than 91.38% of Python3 online submissions for Word Break II.
        Memory Usage: 14.4 MB, less than 11.34% of Python3 online submissions for Word Break II.    
    '''


        