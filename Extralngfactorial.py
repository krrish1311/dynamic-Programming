memory={}
def exlongfactorial(n,memory):
    f0=1
    f1=1
    if n==0:
        return 1
    if n==1:
        return 1
    if n not in memory :
        memory[n]=n*exlongfactorial(n-1,memory)
        
    return memory[n]    
exlongfactorial(45,memory)