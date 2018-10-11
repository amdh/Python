def reorderElements(logFileSize, logLines):
    # WRITE YOUR CODE HERE

    output = []
    aplha_log = []
    numeric_log = []
    for line in logLines.split('['):
        if line:
            line_ = line.replace('[', '').strip()
            if line_.split(' ')[1].isalpha():
                aplha_log.append(line_)
            else:
                numeric_log.append(line_)

    alpha_dict = {}
    for log in aplha_log:
        alpha_dict[log.split(None, 1)[1]] = log.split()[0]
        #alpha_dict[log.split()[0]] = log.split(None, 1)[1]

    alpha_ = sorted(alpha_dict)  # sort by values
    for  v in alpha_:
        print(v)
        line = v +" "+ alpha_dict.get(v)
        print(line)
        output.append(line)
    print(alpha_dict)
    #output.extend(aplha_log)
    output.extend(numeric_log)
    print(output)
    return output

reorderElements(2, "[z1 ss df] [k2 3 5]  [p1 ks fd]")


