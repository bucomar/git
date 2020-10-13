import math as m

def qww(k, du):
    ''' input k, du [l/s] | output: qww [l/s] '''
    qww = k*m.sqrt(du)
    return qww
