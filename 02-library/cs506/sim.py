def euclidean_dist(x, y):
    sum = 0
    for i in range(len(x)):
        sum = sum + abs(x[i] - y[i])**2
    return sum**(1/2)
    #raise NotImplementedError()

def manhattan_dist(x, y):
    sum = 0
    for i in range(len(x)):
        sum = sum + abs(x[i] - y[i])
    return sum
    #raise NotImplementedError()

def jaccard_dist(x, y):
    if (x==[] or y == []):
        return 0
    jaccard_coe = len(set(x)&set(y))/len(set(x)|set(y))
    return 1 - jaccard_coe
    #raise NotImplementedError()

def cosine_sim(x, y):
    if (x==[] and y == []):
        raise ValueError("lengths must not be zero")
    if(len(x) != len(y)):
        raise ValueError("lengths must be equal")
    x_sum = 0
    y_sum =0
    xy_sum = 0
    for i in range(len(x)):
        x_sum = x_sum + (x[i])**2
        y_sum = y_sum + (y[i])**2
        xy_sum = xy_sum + (x[i])*(y[i])

    return xy_sum/(x_sum*y_sum)**(1/2)
    #raise NotImplementedError()

# Feel free to add more