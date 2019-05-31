from .lifetables import life_tables

def lx(x, Table):
    
    if x > 120:
        return 0
    if x < 0:
        raise NameError('Age(x) must be at least 0!')
    if Table not in life_tables:
        raise NameError('Life table ', Table, ' not found ! Add it using add_life_table.')
    return life_tables[Table][x]

def nPx(x, n, Table):
    l1 = lx(x + n, Table)
    l2 = lx(x, Table)
    if l2 != 0:
        return l1 / l2
    else:
        return 0
        
def nQx(x, n, Table):
    if lx(x, Table) != 0:
        return (1 - lx(x + n, Table) / lx(x, Table))
    else:
        return 1

def Dx(x, Table, rate):
    return lx(x, Table)/(1+rate)**x

def nEx(x, n, rate, Table):
    return Dx(x+n, Table,rate)/Dx(x, Table, rate)

def Mx(x, Table, rate):
    temp = 0
    for i in range(x, 121):
        temp = temp + nQx(x, i, Table)/(1+rate)**(i+1)
    
    return temp

def Ax(x, Table, rate):
    return Mx(x, Table, rate)/Dx(x, Table, rate)

def Ax_n(x, n, Table, rate):
    return (Mx(x, Table, rate)-Mx(x+n, Table, rate))/Dx(x, Table, rate)


def Nx(x, Table, rate):
    temp = 0
    for i in range(x, 121):
        temp = temp + Dx(i, Table, rate)
    return temp

    def ax(x, Table, rate, immediate = 0):
        

