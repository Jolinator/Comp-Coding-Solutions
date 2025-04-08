def solution(args):
    st = ''
    start = args[0]
    ln = 1
    for x in range(len(args)-1):       
        
        if args[x] != args[x+1]-1:
            if ln < 3:
                if ln == 2:
                    st += f'{args[x-1]},'
                st += f'{args[x]},'
                start = args[x+1]
            else:
                st += f'{start}-{args[x]},'
                start = args[x+1]
            ln = 1

        else:
            ln += 1

    if ln < 3:
        if ln == 2:
            st += f'{args[-2]},'
        st += f'{args[-1]}'
    else:
        st += f'{start}-{args[-1]}'
    return st

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))   
        