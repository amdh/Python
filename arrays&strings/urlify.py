

def url(str):
    str = str.replace(' ','%20')
    print(str)
    a = []
    for i in str:

        if i == ' ':
            index = str.index(i)
            str[index] = '%20'

    print(str)

url("mr john smith")