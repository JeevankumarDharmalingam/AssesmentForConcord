from itertools import permutations

def construct_word(dict,s):
    dict = dict
    dict = dict.split(" ")

    s = s

    for i in dict:
        if i in s:
            continue
        else:
            dict.remove(i)

    if len(dict)==0:
        print("Empty")
        return
    p = permutations(dict)

    l = list(p)

    result = []
    for i in l:
        res = s
        res_str = ""
        for j in list(i):
            if j in res:
                res_str = res_str + " " + j
                res = res.replace(j, '')

        if (len(res) == 0) and res_str not in result:
            result.append(res_str)


    final_str = []
    for i in result:
        rev = i.replace(" ", "")
        if rev == s:
            final_str.append(i)



    for value in final_str:
        print(f"({value[1:]})", end="")



if __name__ == '__main__':
    dict = "lr m lrm hcdar wk"
    s = "hcdarlrm"
    construct_word(dict,s)