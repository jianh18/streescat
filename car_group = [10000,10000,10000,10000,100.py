
cat_group = [10000,10000,10000,10000,10000,10000,10000,10000];


def ste():
    global cat_group, cat_group_reproduct;
    cat_group_reproduct = cat_group.copy();
    rate = float(input("Enter the rate of ste: "));
    for i in range(8):
        cat_group_reproduct[i] = int(cat_group_reproduct[i]*rate);
    return cat_group_reproduct;

def reproduction_dead():
    
    #cat_group_reproduct = cat_group.copy();
    age_reproduct = 0;
    cat_group_reproduct[0] = int(cat_group_reproduct[0]*0.8);
    for i in reversed(range(1,8)):
        cat_group[i]=int(cat_group[i-1]*0.8);
        cat_group_reproduct[i] = int(cat_group_reproduct[i]*0.8);
    cat_group[0] = 0;
    #错位的两个数组
    while age_reproduct < 6:
        cat_group[0] = cat_group[0] + int(cat_group_reproduct[age_reproduct]*1.5);
        age_reproduct = age_reproduct + 1;
    cat_group_reproduct = cat_group.copy();
    return cat_group;

def total_count():
    total_numebr = sum(cat_group);
    age_dead = [7,0,6,5,4,3,2,1];
    while_num_count = 0;
    while total_numebr > 400000:
        cat_group[age_dead[while_num_count]] = int(cat_group[age_dead[while_num_count]]/4);
        total_numebr = sum(cat_group);
        while_num_count = while_num_count + 1;
        if while_num_count == 8:
            while_num_count = 0;
    return cat_group;




cat_group_reproduct = ste();
cat_group = reproduction_dead();
print(cat_group);







