class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        riches = []
        
        for account in accounts:
            wealth = sum(account)
            riches.append(wealth)
            
            
        riches.sort(reverse=True) #backwards sorting from largest to smallest
        
        
        return riches[0]