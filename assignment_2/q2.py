#def find_product(l):
#    z = len(l);
#    return map(lambda x: reduce(lambda x, y: x * y, map(lambda x: l[z] for l[z]!=None, range(5))), range(len(l)))
    
    
def test_lambda(l):    
    viable_ranges = filter(lambda x: x+5<=len(l), range(len(l)))   
    products = (map(lambda u: reduce(lambda z,q: z*q, map(lambda y: l[y+u], range(5))), viable_ranges))
    largest_index = filter(lambda x: len(filter(lambda y: products[y] < products[x], range(len(products)))) == (len(products)-1), range(len(products)))
    largest = map(lambda x: products[x], largest_index)
    return largest.pop(0), largest_index.pop(0)
    
if __name__ == "__main__":
    print "in main"
    #product = find_product([3,4,5,6,4])
    test = test_lambda([1,2,3,4,5,6,7,8,9])
    print test