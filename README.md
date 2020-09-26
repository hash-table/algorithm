# Rule

## 0. Intro

- Search conditions in github
	
        - <problem source> + #
        - tokens in <problem identifier>
        - # + <algo type>
        - # + <algo type> + # + <marker type>
        - # + marker type
            - 'good' : tag for good problems


## 1. Repo path rule

    1. repo path
        - <year> - <month> - <week> - <problem>
            - year  : YYYY (2020 ~)
            - month : MM (01 ~ )
            - week  : WW (01 ~ )
            - problem : <source>#<identifier>#<algo type>(#<marker>)
    
    2. Example 

	- year#1
		- month#1
			- week#1
				- <problem source>#<problem identifier>#<main algo type>(#<special marker>)
			- week#2
				- #leet#1386-cinema-seat-allocation#string
				- #leet#1382-balance-a-binary-search-tree#bst#good
		- month#2
	- year#2



## 2. Commit message rule	
	=> #<problem source>#<problem identifier>#<main algo type>(#<special marker>)


