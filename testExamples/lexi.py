
def creatStr(index,lst):
    print lst
    lar_str = []
    i =index

    while (True):
        lar_str.append(lst[i])
        i+=1
        if (i == len(lst)):
            i = 0
            continue
        elif ( i == index ):
            break
        else:
            continue

    print ''.join(lar_str)
    return  ''.join(lar_str)

def  rotate(x, y):
    w_x = list(x)
    print w_x
    l_x = len(w_x)
    print l_x
    all_words = []
    m_val = max(w_x)
    print m_val
    index = w_x.index(m_val)
    x_1 = creatStr(index, w_x)

    print "----"
    w_y = list(y)
    l_y = len(w_y)
    all_words = []
    m_val_y = max(w_y)
    print m_val_y
    index_y = w_y.index(m_val_y)
    y_1 =creatStr(index_y, w_y)

    print x_1.join(y_1)
    return x_1.join(y_1)


rotate("foawn","pay")