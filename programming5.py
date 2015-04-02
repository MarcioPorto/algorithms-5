"""
  Comp 221 F14 
  Programming Assignment #5 
  Marcio Porto
"""

def openHash():
    """ This function implements a Open Hash Table  based on input by the user
    regarding the table size and the numbers to insert """    
    n = input("Please enter the table size: ")
    tab = []
    for i in range(n):
        tab.append([])
    while n > 0:
        m = input("Please enter an integer: ")
        if m >= 0:
            tab[m%n].append(m)
            print tab
        else:
            break
        
         
def closedHash():
    """ This function implements a Closed Hash Table based on input by the user
    regarding the table size and the numbers to insert """       
    n = input("Please enter the table size: ")
    tab = []
    for i in range(n):
        tab.append("")
    for i in range(n):
        m = input("Please enter an integer: ")
        if m >= 0:
            temp = m%n
            for j in range(n):
                if tab[temp] == "":
                    tab[temp] = m
                    break
                else:
                    if tab[temp] == "":
                        tab[temp] = m
                        break
                    else:
                        if temp >= n-1:
                            temp = 0
                        else:
                            temp+=1
                        pass
            print tab
        else:
            break
        if i==n-1:
            print("Array is full!")


#openHash()
closedHash()
