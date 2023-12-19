#Two numbers are positive
def check_positive_integers(i,j,k):
    #returnTrue if all the numbers are positive
    if (i>0 and j>0 and k>0):
        return True
    #return true if any two of the numbers are positive
    elif (i<0 and j>0 and k>0):
        return True
    elif (i>0 and j<0 and k>0):
        return True
    elif (i>0 and j>0 and k<0):
        return True
    #return false if only one of the numbers is positive
    else:
        return False
    
print(check_positive_integers(7,-9,2))