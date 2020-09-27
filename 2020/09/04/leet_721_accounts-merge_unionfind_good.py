
# 2020\09\04\leet_721_accounts-merge_unionfind_good.py
# - _leet 
# - _unionfind
# - _good
# - _unionfind_good



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        
            problem
                accounts : List 
                accounts[i] : List[str]
                    accounts[i] = [ name , email1, email2..]
                
                merge theses accounts 
                    
                    accounts[0] = ["a" , "e1", "e2"]
                    accounts[1] = ["a" , "e3", "e4"]
                    accounts[2] = ["a" , "e1", "e5"]
                    => accounts 0, 2 는 merge 가 됨, 1은 아직 공통되는게 없어서 알 수 가 없음 
                    
                    => 동명이인 문제가 있음
                    => 근데 mail에 공통적인게 하나라도 있다면 같은 사람이라고 볼 수 있음 
                    
                merge를 한 이후에, return the accounts in the following format
                
                    [
                        [name, e1, e2, e3.. ], 근데 e1~en은 sorted order야 한다. 
                        ..                        
                    ]
                    account들은 어떠한 순서에도 상관없다 
            idea
                
                union find 를 이용. 
                
                - 모든 메일들은 parent를 가짐                
                mail_set = set()
                mail_parent = dict() # key : str, val : str
                # mail_parent[mail#1] = mail#2 : mail#1 의 parent는 mail#2 이다 
                # find_root(mail_parent, specific_mail) 
                name_mapping = dict() # key : mail, val : person_name
                
                # mail_parent, mapping construct
                
                mail_parent 들에 대해서 다음을 수행
                final = defaultdict( lambda : [] )
                # key 는 대표메일, val은 대표메일 밑에 있는 메일들
                for mail in mail_set
                    root = get_root(mail)
                    final[root].append(mail)
                for k in final:
                    ret.append([mail_parent[k]] + sorted(final[k])                
                return ret 
                
                mail_num = |N|
                Time, Space : O(|N| * log**N), O(|N|)
                
            test        
                * mail 없는 사람 존재할 수 있겠다, 마지막에 관리 
                mail_set = set()
                mail_parent = dict()
                mail_person_map = defaultdict(lambda : [])
                no_mail = []
                
                for account in accounts:
                    person_name = account[0]
                    len_account = len(account)
                    if len_account == 1 :
                        # mail이 없는 경우 
                        no_mail.append(person_name)
                    else:
                        repr_mail = account[1]
                        for idx in range(1, len(account)):
                            mail_set.add(account[idx])
                            mail_person_map[account[idx]] = person_name
                            mail_parent[account[idx]] = repr_mail
                def get_root(mail_parent : Dict, mail: str)->str:
                    pass
                    
                final = defaultdict(lambda: [])
                for mail in mail_set:
                    root = get_root(mail_parent, mail)
                    final[root].append(mail)
                for k in final:
                    ret.append([mail_person_map[k]] + sorted(final[k]))
                return ret 
        
        
        '''
        
        mail_set = set()
        mail_parent = defaultdict(lambda : 'none')
        mail_person_map = defaultdict(lambda : [])
        no_mail = []
        
        def get_root(mail_parent : Dict, mail: str)->str:
            if mail_parent[mail] == mail:
                return mail
            else:
                mail_parent[mail] = get_root(mail_parent, mail_parent[mail])
                return mail_parent[mail] 

        for account in accounts:
            person_name = account[0]
            len_account = len(account)
            if len_account == 1 :
                # mail이 없는 경우 
                no_mail.append(person_name)
            else:
                repr_mail = min(account[1: ])
                if mail_parent[repr_mail] == 'none': 
                    mail_parent[repr_mail] = repr_mail 

                for idx in range(1, len_account ):
                    mail_set.add(account[idx])
                    mail_person_map[account[idx]] = person_name
                    # 이런식이면 parent가 만들어질떄 a: b, b: a가 될 수 있음 
                    if mail_parent[account[idx]] == 'none': 
                        mail_parent[account[idx]] = repr_mail 
                    else:
                        # mail_parent[account[idx]] 와 repr_mail 에서 경쟁
                        root1 = get_root(mail_parent, account[idx])
                        root2 = get_root(mail_parent, repr_mail)
                        tmp = [root1, root2]
                        tmp.sort()
                        # print(tmp)
                        # reprmail : david1
                        # othermail : dvaid0
                        mail_parent[tmp[0]] = tmp[0]
                        mail_parent[tmp[1]] = tmp[0]
                        

            
        ret = []
        # for k in mail_parent:
        #     print(k, mail_parent[k])
        # print(mail_parent)
        final = defaultdict(lambda: [])
        for mail in mail_set:
            root = get_root(mail_parent, mail)
            final[root].append(mail)
        
        for k in final:
            ret.append([mail_person_map[k]] + sorted(final[k]))
        
        for no_mail_person in no_mail:
            ret.append([no_mail_person])
        
        return ret 


        '''
            202009261323  202009261400
            Runtime: 208 ms, faster than 89.63% of Python3 online submissions for Accounts Merge.
            Memory Usage: 18.4 MB, less than 49.20% of Python3 online submissions for Accounts Merge.


        '''