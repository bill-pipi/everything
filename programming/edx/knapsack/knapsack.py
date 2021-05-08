class Item :
    def __init__(self, weight, value) :
        self.w = weight
        self.v = value


    def add(self, other) :
        return Item(self.w+other.w, self.v+other.v)


    def __str__(self) :
        return str(self.w) + "," +str(self.v)

    def __lt__(self, other) :
        return self.v < other.v


class Knapsack :
    def __init__(self, dim, items) :
        self.dim = dim
        self.items = items
        self.matrix = dict()
        
        names = [0]+items.keys()
            
        for n in names :
            column = dict()
            
            for d in range(0, dim+1) :
                column[d] = Item(0,0)

            self.matrix[n] = column


            


    def compile(self) :
        names = self.items.keys()
        
        for n in names :
            column = self.matrix[n]
            item = self.items[n]
            
            for d in column.keys() :
                op = self.matrix[n-1][d]
                print item
                
                if item.w <= d :
                    if item > op :
                        op = item

                rem = self.matrix[n][d-op.w]
                self.matrix[n][d] = op.add(rem)
                



knapsack = Knapsack(50, {1 : Item(10,60), 2 : It em(20,100), 3:Item(30,120)})

knapsack.compile()

for n in knapsack.matrix.values() :
    for d in n.values() :
        print d
        
