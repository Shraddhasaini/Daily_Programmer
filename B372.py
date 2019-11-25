def bonus(str):
    res = list(set(str))
    rs = []
    for r in res:
        rs.append(str.count(r))
    if len(set(rs))==1:
        print("True")
    else print("False")

bonus("xxyyyyyyyyyyyyyyyyy")
