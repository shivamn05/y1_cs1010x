def num_cards(h):
    # base case of height 1
    if h == 1:
        return 2
    # recursive solution
    else:
        # returns number of cards for tower of height h
        return 3*(h-1) + 2 + num_cards(h-1)


#--- TEST CASES ---#
print(num_cards(1)==2)
print(num_cards(2)==7)
print(num_cards(3)==15)
print(num_cards(4)==26)

def num_triangles(h):
    # base case of height 1 
    if h == 1:
        return 0
    if h == 2:
        return 2
    else:
        # for upside down triangles 
        if h % 2 == 0:
            final = 1
            curr = 1
            add_to = 0
            for i in range(h//2-1):
                add_to =  5 + 4*i
                curr = curr + add_to
                final = final + curr
        else:
            final = 3
            curr = 3
            add_to = 0
            for i in range(h//2-1):
                add_to = 7 + 4*i
                curr = curr + add_to
                final = final + curr
        # for normal triangles 
        upside_final = 1
        upside_curr = 1
        for i in range(h-2):
            upside_curr = upside_curr + 2 + i*1
            upside_final = upside_final + upside_curr
    return final + upside_final

#--- TEST CASES ---#
for i in range(1,10):
    print(num_triangles(i))

