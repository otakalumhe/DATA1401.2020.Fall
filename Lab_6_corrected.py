class Matrix:
    def __init__(self, m, n, init=True, data=None):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
        self._data = []
        self.data = data
       
    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def _set_data(self, data=None): 
        """Sets the data stored in the matrix""" 
        if data is not None: 
            self._data = [list(row) for row in data] 
            self._nrow = len(self._data) 
            if self._nrow > 0: 
                self._ncol = max(len(row) for row in self._data) 
            else: 
                self._ncol = 0 
            for row in self._data: 
                if len(row) < self._ncol: 
                    row.extend([0]*(self._ncol-len(row))) 

    def _get_data(self): 
        """Returns the data stored in the matrix as a list of lists""" 
        return [list(row) for row in self._data] 
    data = property(_get_data, _set_data) 
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return rep
    
    def zeroMatrix(self):
        """ create new Zero Matrix """
        out = list()
        for i in range(self.m):
            row=list()
            for j in range(self.n):
                row.append(0.)
            out.append(row)
        return out
    
    def shape(self):
        """ Matrix Shape """
        return self.m,self.n

    def transpose(self):
        """ Transpose the matrix. Changes the current matrix """  
        m, n = self.n, self.m
        mat = Matrix(m,n)
        mat.rows = [list(item) for item in zip(*self.rows)]
        return mat
    
    def row(self,n):
        return self.__getitem__(n)
    
    def column(self,m):
        return self.__getitem__(m)
    
    def to_list(self):
        return self._get_data()

A = Matrix(2,3)
print(A.shape())
print(A.zeroMatrix())
print(A.transpose())
print(A.row(0))
print(A.column(0))
print(A.to_list())
                     

    