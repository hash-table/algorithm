# Rule


## 1. Repo path rule

    1. repo path
        - <year> - <month> - <week> - <problem>
            - year  : YYYY (2020 ~)
            - month : MM (01 ~ )
            - week  : WW (01 ~ )
            - problem : <source>_<identifier>_<algo type>(_<marker>)
    
    2. Example 

	- year#1
		- month#1
			- week#1
				- <problem source>_<problem identifier>_<main algo type>(_<marker>)
			- week#2
				- leet_1386-cinema-seat-allocation_string
				- leet_1382-balance-a-binary-search-tree_bst_good
		- month#2
	- year#2



## 2. Commit message rule	
	=> <problem source>_<problem identifier>_<main algo type>(_<special marker>)

## 3. Code rule

1. Write meta info ( file path, search keywords ) 

        # <relative path>
        # - _<source> 
        # - _<algo_type>
        # - _<marker>
        # - _<algo_type>_<marker>

2. Write codes in 3 parts, problem - idea - test
    
        Example)

            def some_func(self, root: TreeNode) -> TreeNode:
            '''
                problem
                    => write one-line summary        
                                    
                idea
                    => ideation with time, space cost
                    => code draft
                
                test 
                    => edge case
                    => base case 
                    => recusrion case           
                                        
            '''
        
3. Write results of algorithm with time

        Example (Leet output)
            '''
                202009261120 202009261150 

                Runtime: 356 ms, faster than 85.58% of Python3 online submissions for Balance a Binary Search Tree.
                Memory Usage: 20.7 MB, less than 5.19% of Python3 online submissions for Balance a Binary Search Tree.
            '''

