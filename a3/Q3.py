def get_a(s):
    return min(s,100-s)
def value_iteration(S,theta,P):
    #list for all value of state
    V = [0 for i in range(101)]
    V[100] = 1
    target = 0

    while target<theta:
        for s in S:
            v = V[s]
            #list for all possible action
            A = [i+1 for i in range(get_a(s))]
            value = [0 for i in range(len(A)+1)]
            for a in A:
                if a==get_a(s):
                    #print "%d %d %d %d"%(len(A),a,s+a,s-a)
                    value[a] = P*(1+V[s+a])+(1-P)*(0+V[s-a])
                else:
                    value[a] = P*V[s+a]+(1-P)*V[s-a]
            #find the max value except V[0] and V[100]
            V[s] = max(value)
            target = max(target,abs(v-V[s]))
        
    print V
                
             
                


if __name__=="__main__":
    #array for all the state
    S = [i for i in range(1,100)]
    theta = 0.001
    #probability of get head
    P = 0.25
    value_iteration(S,theta,P)
    
    

