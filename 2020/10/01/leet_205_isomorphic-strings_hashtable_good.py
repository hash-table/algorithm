# leet_205_isomorphic-strings_hashtable_good
# - _leet 
# - _hashtable
# - _good
# - _hashtable_good
#  202010031957 202010032011

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
            problem
            
                string s랑 t가 주어졌음 
                이 때 s, t가 isomorphic 인지를 반환해라(bool)
                
                isomorphic
                    -> s 안의 문자들에 대해, t로 치환될 수 있는지
                    
                foo bar -> false
                
                egg add -> true
                
                paper title -> true
                
                
            
            idea
            
                1. s와 t의 길이가 다르면 아예안됨
                
                2.
                
                    s와 t 에 대해서 iteration을 진행한다 
                    
                    1. charactermap이 하나 있음 
                    
                    # siter, titer에 대해 다음 loop를 수행한다
                    dict_s = {k : None for k in 'abcdefghijklmnopqrstuvwxyz'}
                    
                        1. dict_s[siter] 가 있는 경우
                            mapping = dict_s[siter]
                            if mapping == tier:
                                continue
                            else:
                                return False
                        
                        2. dict_s[siter]가 없는 경우
                            dict_s[siter] = titer
                            contnue
                    
                    
                    # draft
                    
                    
                    if len(s) != len(t) :
                        return False
                    if len(s) == 0:
                        return True
                        
                    dict_s = {k : None for k in 'abcdefghijklmnopqrstuvwxyz'}                    
                    for siter, titer in zip(s, t):
                        if dict_s[siter] == None:
                            dict_s[siter] = titer
                        else:
                            mapping = dict_s[siter]
                            if mapping != titer:
                                return False
                    
                    return True
                
                
            well formed
            
                    if len(s) != len(t) :
                        return False
                    if len(s) == 0:
                        return True

                    dict_s = {k : None for k in 'abcdefghijklmnopqrstuvwxyz'}
                    for siter, titer in zip(s, t):
                        if dict_s[siter] == None:
                            dict_s[siter] = titer
                        else:
                            mapping = dict_s[siter]
                            if mapping != titer:
                                return False
                    
                    return True
            
            
            test
                    
                s = paper 
                t = title
                
                dicts[p] = t
                dict[a] = i
                dict[p]->있음, t == t 
                dict[e] = l 
                
                s = foo t = bar
                dicts[f] = b
                dicts[o] = a
                dicts[o] = a != r 
                
        
        
        '''
        if len(s) != len(t) :
            return False
        if len(s) == 0:
            return True


        used = set()
        dict_s = dict()
        for siter, titer in zip(s, t):
            if dict_s.get(siter, None) == None:
                if titer not in used:
                    dict_s[siter] = titer
                    used.add(titer)
                else:
                    return False
            else:
                mapping = dict_s[siter]
                if mapping != titer:
                    return False

        return True


    '''
    
        Runtime: 44 ms, faster than 53.88% of Python3 online submissions for Isomorphic Strings.
        Memory Usage: 14.5 MB, less than 15.52% of Python3 online submissions for Isomorphic Strings.
        Next challenges:    
    
    '''