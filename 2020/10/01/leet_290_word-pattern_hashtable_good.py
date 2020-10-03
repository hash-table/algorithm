# leet_290_word-pattern_hashtable_good
# - _leet 
# - _hashtable
# - _good
# - _hashtable_good
# 202010032013 202010032028


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        
            problem
                pattern과 string s 가 있음 
                s가 pattern에 맞는지를 체크하라 

                follow 란, full match를 뜻함. 

                pattern = 'abba' s = 'dog cat cat dog' -> true

                pattern = 'abba' s = 'dog cat cat fish' -> false


                # pattern은 영어 소문자로만 구성이 된다 
                # pattern의 길이는 300 이하 

                pattern 문자열이 있고 white space 한칸과 영어 소문자로 구성된 s 가 있을 때 s를 white space 기준으로 나누었을때, pattern과 일치하는지를
                반환하라 
                s는 leading 이나 trainlign 이 없다는게 중요

            idea
                # 모든 token과 pattern은 1:1 관계를 이루어야 한다. 
                tokens = s.split()
                pattern := str
                table = dict() # 이건 하나의 패턴이 n개의 token을 가질 수 있음을 나타냄
                used = set() 
                for p, token in zip(pattern, tokens):
                    # 1. table[p]가 존재하지 않는다면 token을 넣고 끝 
                    pass

                    # 2. table[p]가 존재하는 경우 
                        2-1 table[p]에 들어있는 것과 token이 같고 token이 아직 한번도 안나왔는가? 
                        ab
                        aa

                return True

            well formed

                aba  dog dog cat

                (a, dog) -> dict[a] = dog
                (b, cat) -> dict[b] 는 None이야 근데 

                tokens = s.split()
                if len(p) != len(tokens):
                    reutnr False
                table = dict()
                used = set()
                for p, token in zip(pattern, tokens):
                    if table.get(p, None) == None :
                        if token not in used:
                            table[p] = token
                            used.add(token)
                        else:
                            return False
                    else:
                        if table[p] != token:
                            return False
                return True


            test

        
        
        '''
        
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        table = dict()
        used = set()
        for p, token in zip(pattern, tokens):
            if table.get(p, None) == None:
                if token not in used:
                    table[p] = token
                    used.add(token)
                else:
                    return False
            else:
                if table[p] != token:
                    return False
        return True

'''
    Runtime: 32 ms, faster than 40.72% of Python3 online submissions for Word Pattern.
    Memory Usage: 14.2 MB, less than 5.37% of Python3 online submissions for Word Pattern.

'''