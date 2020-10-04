# leet_291_word-pattern-ii_dfs_good
# - _leet 
# - _dfs
# - _good
# - _dfs_good
# 2020100320030
# 202010041410 202010041457
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        '''
            problem
                
                Input: pattern = "abab", str = "redblueredblue" -> True
                Input: pattern = "aaaa", str = "asdasdasdasd" -> True
                Input: pattern = "aabb", str = "xyzabcxzyabc" -> F calse

            
            idea
                access1
                    pattern의 각 알파벳을 p0 p1 p2 .. 라고 할때
                    각 pi가 가져 갈 수 있는 모든 가지수에 대해서, 다 찾아보는 방법
                    
                    func('abcd', 'qewrqwerwqw', dict)
                        -> func(bcd, ewrqwerwqw, {a : q})
                        -> func(bcd, wrqwerwqw, {a : qe})
                        -> func(bcd, rqwerwqw, {a : qew})
                        -> func(bcd, qwerwqw, {a : qewr})
                        .... 
                        => Time complexity는
                            패턴문자열의 길이를 |P|, 타겟 스트링의 길이를 |N| 이라고 하자
                            이 때 O(nCp) 가 된다 . 
                            => 근데 |P|의 문자열은 a~z에 한정이 된다 따라서
                                unique한 패턴 문자의 개수를 |D|라고 할때, |D| <= 26
                                O(nCd)로 문제를 바꿀 수 있다 
                    
                        어떤 패턴의 unique character가 {a,b,c,d} 라고 하자
                        가지고 있는 hint에 대해서 생각을 해보자, 가장 첫 패턴에 대해 생각을 해보면
                        str[0: length]가 첫 패턴에 매핑 되는 가지수이다.
                        여기서 완전탐색을 진행할가? 
                -> 현재 생각해야할 것은, pattern으로 str을 나타낼 수 있는가 이다. 
                
                    결국, 쭉 가면서 다 뽑아보는 문제로 바꿔서 생각을 해보자
                    
                    aux = dict()
                    used = set()
                    len_p = len(pattern)
                    len_s = len(str)
                    def func(pidx, sidx, aux, used):
                        nonlocal len_p, len_s, pattern, str
                        if pidx == len_p and sidx == len_s:
                            return True
                        elif pidx == len_p and sidx < len_s:
                            return False
                        elif not pidx == len_p and sidx == len_s:
                            return False
                        else:
                            # 1. current_pattern에 이미 나온 것이 있는지를 체크한다.
                            #   존재하지 않는다면 될 수 있는 모든것에 대해 분기를 태운다
                            current_pattern = pattern[pidx]
                            mapping_val = aux.get(current_pattern, None)
                            
                            if mapping_val == None:
                                # sidx에서 시작해서 len_s 까지 갈 수 있겠네
                                for eidx in range(sidx+1, len_s):
                                    pick = pattern[sidx: eidx]
                                    # pick이 아직 사용되지 않았다면 이걸 써본다
                                    if pick not in used:
                                        used.add(pick)
                                        aux[current_pattern] = pick
                                        tmp = func(pidx+1, eidx, aux, used)
                                        if tmp:
                                            return True
                                        else:
                                            used.remove(pick)
                                            del aux[current_pattern]
                                return False
                                
                            else:
                                mappin_val = aux[current_pattern]
                                # mapping_val과 [sidx : sidx + len(mapping_val)] 까지 같은지를 비교한다
                                # 만약 둘이 같다면
                                # func(pidx+1, sidx+ len(mapping_val, aux, used)) 가 된다
                                # 만약 둘이 다르다면 return False
                                if str.startswith(mapping_val, sidx):
                                    return func(pidx+1, sidx + len(mapping_val), aux, used)
                                else:
                                    return False
                well-formed
                                    
                            
                    aux, used = dict(), set()
                    len_p, len_s = len(pattern), len(str)
                    
                    def func(pidx, sidx, aux, used):
                        nonlocal len_p, len_s, pattern, str
                        if pidx == len_p and sidx == len_s:
                            return True
                        elif pidx == len_p and sidx < len_s:
                            return False
                        elif not pidx == len_p and sidx == len_s:
                            return False
                        else:
                            current_pattern = pattern[pidx]
                            mapping_val = aux.get(current_pattern, None)                           
                            if mapping_val == None:
                                for eidx in range(sidx+1, len_s):
                                    pick = pattern[sidx: eidx]
                                    if pick not in used:
                                        used.add(pick)
                                        aux[current_pattern] = pick
                                        tmp = func(pidx+1, eidx, aux, used)
                                        if tmp:
                                            return True
                                        else:
                                            used.remove(pick)
                                            del aux[current_pattern]
                                return False
                            else:
                                mappin_val = aux[current_pattern]
                                if str.startswith(mapping_val, sidx):
                                    return func(pidx+1, sidx + len(mapping_val), aux, used)
                                else:
                                    return False
                    
                    return func(0, 0, aux, used)


            test
                'abab', 'redblueredble', aux : {}, used : {}
                
                (pidx = 0, sidx = 0, aux : {}, used : {})
                    current_pattern = 'a'
                    aux['a'] 는 None 
                        pick : r
                            -> (pidx = 1 sidx = 1, aux : {'a' : 'r'}, used : {'r'})
                                    current_pattern = 'b'
                                    aux['b'] 는 None
                                        pick : e
                                            
                                
                        pick : re
                        
                        pick : red
                        
                        pick : redb
                        
                        pick : redbl
                        
                        pick : redblu
                        
                        pick : redblue ..
                        
        
        '''
        aux, used = dict(), set()
        len_p, len_s = len(pattern), len(str)
        def func(pidx, sidx, aux, used):
            nonlocal len_p, len_s, pattern, str
            if pidx == len_p and sidx == len_s:
                return True
            elif pidx == len_p and sidx < len_s:
                return False
            elif not pidx == len_p and sidx == len_s:
                return False
            else:
                current_pattern = pattern[pidx]
                mapping_val = aux.get(current_pattern, None)                           
                if mapping_val == None:
                    for eidx in range(sidx+1, len_s+1):
                        # pick = pattern[sidx:eidx]로 해서 에러
                        pick = str[sidx: eidx]
                        if pick not in used:
                            used.add(pick)
                            aux[current_pattern] = pick
                            tmp = func(pidx+1, eidx, aux, used)
                            if tmp:
                                return True
                            else:
                                used.remove(pick)
                                del aux[current_pattern]
                    return False
                else:
                    mappin_val = aux[current_pattern]
                    
                    if str.startswith(mapping_val, sidx):
                        return func(pidx+1, sidx + len(mapping_val), aux, used)
                    else:
                        return False

        return func(0, 0, aux, used)        
    
    
    
'''
    Runtime: 200 ms, faster than 66.67% of Python3 online submissions for Word Pattern II.
    Memory Usage: 14 MB, less than 12.37% of Python3 online submissions for Word Pattern II.

'''