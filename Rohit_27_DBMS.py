####################### FUNCTIONS FOR CODE ###################################################
def closure(elems, fds):
    '''
    Objective : Find closure for given functional dependencies.
    --------------------------------------------------------------------------------------
    Parameters:
        elems <String>            Elements in question for closure
        fds <list of tuples>       Tuples of x -> b in form ('X1X2X3', 'Y1')
    --------------------------------------------------------------------------------------
    Returns <set of elements>:
        set of elements under closure here element is in string.
    '''
    closure = set(elems)
    
    while(1):
        l=len(closure)
        for i in range(len(fds)):
            if set(fds[i][0]).issubset(closure):
                closure.update(fds[i][1])
        if len(closure)==l:
            break
        
    return closure


def Candidate_key(attribute,fds):
    '''
    Objective : Find the set of candidate keys
    --------------------------------------------------------------------------------------
    Parameters:
        attribute <String>        All the attribute of the table
        fds <list of tuples>       Tuples of x -> b in form ('X1X2X3', 'Y1')
    --------------------------------------------------------------------------------------
    Returns <Set of elements>:
        set Candidate keys here every element x is 'X1X2X3'
    '''
    
    
    all_att=list(attribute)
    test=set(attribute)
    cand=[]
    check=list(all_att)
    
    # genrating all combination of attributes and finding whether it is a superkey or not
    
    for i in range(1,2**len(all_att)):
        
        temp=''
        for j in range(len(all_att)):   
            if i & (1 << j): 
                temp+=all_att[j]

        if test==closure(temp,fds):
            cand.append(temp)
    
    #find the location of superkey which are not candidate key
    
    r=set()
    for j in range(len(cand)):
        for i in range(j+1,len(cand)):
            if set(cand[j]).issubset(set(cand[i])):
                r.update(set([i]))
    
    #remove superkey which are not candidate key
    
    r=list(r)
    temp=list(cand)
    
    for i in r:
        cand.remove(temp[i])
    
    return cand


def minimalset(fd):
    '''
    Objective : Find the minimal set or conanical cover of FDs for a given FD
    -----------------------------------------------------------------------------------------------------
    Parameters:
                fds <list of tuples>        Tuples of x -> b in form ('X1X2X3', 'Y1')
    -----------------------------------------------------------------------------------------------------
    Return <list of tuples> : It is our minimal fd
    '''
    fd=set(fd)						#remove duplicate FDs
    fd=list(fd)
    
    minfd=[]
    
    for i in fd:
        t1=closure(i[0],fd)
        temp=list(fd)
        temp.remove(i)
        t2=closure(i[0],temp)
        if t1==t2:
            pass
        else:
            minfd.append(i)
            
    
    for i in range(len(minfd)):
        if len(minfd[i][0])>1:
            temp=[]
            for j in minfd[i][0]:
                t1=closure(minfd[i][0],fd)
                t2=closure(j,fd)
                if t1==t2:
                    temp.append(j)
            temp="".join(temp)
            if temp=='':
                temp=minfd[i][0]
            t=list(minfd[i])
            minfd.remove(tuple(t))
            t[0]=temp
            minfd.insert(i,tuple(t))
                
    return minfd


def equivalance(fds1,fds2):
    '''
    Objective : Find Whether the 2 FDs are Equivalent or not
    ----------------------------------------------------------------------------------------------------
    Parameters :
                fds1 <list of tuples>        first fd Tuples of x -> b in form ('X1X2X3', 'Y1')
                fds2 <list of tuples>        second fd Tuples of x -> b in form ('X1X2X3', 'Y1')
    ----------------------------------------------------------------------------------------------------
    Return <Boolean> : Return True if Both Fds are equivalent else False
    
    '''
    # checking whether fds1 is subset of fds2 or not
    for i in fds1:
        t1=closure(i[0],fds1)
        t2=closure(i[0],fds2)
        if t1==t2:
            pass
        else:
            return False
    
    #checking whether fds2 is subset of fds1 or not
    for i in fds2:
        t1=closure(i[0],fds1)
        t2=closure(i[0],fds2)
        if t1==t2:
            pass
        else:
            return False
    
    return True

def _2nf(fds,attribute):
    '''
    OBjective : Find whether the given functional dependency is 2NF or Not
    ------------------------------------------------------------------------------------------------
    Parameters:
                fds <list of tuples>       Tuples of x -> b in form ('X1X2X3', 'Y1')
                attribute <String>        All the attribute of the table
    -------------------------------------------------------------------------------------------------  
    Return <Boolean> : return true if it is 2NF else Return False
    '''
    candidate=Candidate_key(attribute,fds)                                  #genrate a list of candidate keys
    prime=[]
    for i in candidate:
        for j in i:
            prime.append(j)

    for i in fds:
        for i in candidate:
            if not (set(i[0]).issubset(candidate)) and (i[1] not in prime):         #if lhs of fd is not a candidate key and rhs in not prime
                for j in i[0]:
                    if j in prime:                                      # lhs does not contain prime attributes
                        return False
    return True

def _3nf(fds,attribute):
    '''
    OBjective : Find whether the given functional dependency is 3NF or Not
    ------------------------------------------------------------------------------------------------
    Parameters:
                fds <list of tuples>       Tuples of x -> b in form ('X1X2X3', 'Y1')
                attribute <String>        All the attribute of the table
    -------------------------------------------------------------------------------------------------  
    Return <Boolean> : return true if it is 3NF else Return False
    '''
    if not (_2nf(fds,attribute)):
        return False
    
    candidate=Candidate_key(attribute,fds)                                  #genrate a list of candidate keys
    prime=[]
    for i in candidate:
        for j in i:
            prime.append(j)
    
    for i in fds:
        f=False
        for j in candidate:
            if set(j).issubset(set(i[0])):
                f=True
                break
        if f:
            continue
        
        if i[1] not in prime:
            return False
    return True

def BCNF(fds,attribute):
    '''
    OBjective : Find whether the given functional dependency is BCNF or Not
    ------------------------------------------------------------------------------------------------
    Parameters:
                fds <list of tuples>       Tuples of x -> b in form ('X1X2X3', 'Y1')
                attribute <String>        All the attribute of the table
    -------------------------------------------------------------------------------------------------  
    Return <Boolean> : return true if it is BCNF else Return False
    '''
    if not (_3nf(fds,attribute)):
        return False
    
    candidate=Candidate_key(attribute,fds)                                  #genrate a list of candidate keys
    prime=[]
    for i in candidate:
        for j in i:
            prime.append(j)
    
    for i in fds:
        f=False
        for j in candidate:
            if set(j).issubset(set(i[0])):
                f=True
                break
        if not f:
            return False
        
    return True

################################################## MAIN PROGRAM ##############################################################

'''
Taking input from user
'''
attri=input("attributes in the relation (e.g ABCD): ")
attri=attri.replace(" ","")
N=int(input("NUMBER OF FUNCTIONAL DEPENDENCY IN THE RELATIONS : "))
FD=[]                                                         # FD
for i in range(N):                                            # loop to take all the relations of FD as input
    temp=input("Enter functional dependency "+str(i+1)+" ( e.g A->B or AB->CD) : ").strip()
    t=temp.split("->")
    t[0]=t[0].replace(" ","")
    t[1]=t[1].replace(" ","")
    for i in t[1]:
        FD.append((t[0],i))
'''
now our fd is in 'FD' of form [a,b,c...] where a is a tuple and Tuples is of x -> y is in form ('X1X2X3', 'Y1')
here we have seprated the RHS into individual attributes
'''
while(1):
    ch=int(input('\nMenu for inputed functional Dependency\n'+
             '1. Closure\n' +
             '2. Candidate Keys\n' +
             '3. Minimal set\n' +
             '4. Equivalance\n' +
             '5. Check 2NF\n' +
             '6. Check 3NF\n' +
             '7. Check BCNF\n'+
             '8. Exit\n'+
             'Choice : '))
    print("")
    if ch==1:
        el=input("Enter the elements for closure to be found out")
        el=el.replace(" ","")
        print("\nCLOSURE OF "+el+" "+str(closure(el,FD)))
    elif ch==2:
        print("Candidate keys are "+str(Candidate_key(attri,FD)))
    elif ch==3:
        print("Minimal set is"+str(minimalset(FD)))
    elif ch==4:
        M=int(input("NUMBER OF FUNCTIONAL DEPENDENCY IN THE  2nd RELATION : "))
        FD1=[]                                                         # FD
        for i in range(N):                                            # loop to take all the relations of FD as input
            temp=input("Enter functional dependency "+str(i+1)+" ( e.g A->B or AB->CD) : ").strip()
            t=temp.split("->")
            t[0]=t[0].replace(" ","")
            t[1]=t[1].replace(" ","")
            for i in t[1]:
                FD1.append((t[0],i))
        if equivalance(FD,FD1):
            print("\nBOTH Functional dependency are equal")
        else:
            print("\nGiven Functional dependency are not equal")
    elif ch==5:
        if _2nf(FD,attri):
            print("Functional dependency is in 2NF")
        else:
            print("Given Functional dependency is not in 2NF")
    elif ch==6:
        if _3nf(FD,attri):
            print("Functional dependency is in 3NF")
        else:
            print("Given Functional dependency is not in 3NF")
    elif ch==7:
        if BCNF(FD,attri):
            print("Functional dependency is in BCNF")
        else:
            print("Given Functional dependency is not in BCNF")
    elif ch==8:
        break