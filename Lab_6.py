class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def zero_matrix(self, m, n):
        out = list()  # Creates a list of object, used to store multiple items
        for i in range(self.m):
            row = list()
            for j in range(self.n):
                row.append(0.0)
            out.append(row)
        return out

    '''Not part of lab task but tests to see if we are dealing with a matrix'
    def is_matrix(self):
        if isinstance(self, list):
            row_length = len(self[0])
            for row in self:
                if not row_length == len(row):
                    return False
        else:
            False
        return True'''

    # Shape method should return a tuple of the shape of the matrix
    def shape(self):
        m = self.m
        n = self.n
        print(m, n)
        return m, n

    'Alternative below:'
    # def shape(self):
    '''print('Row: '+str(self.m) +' Column: '+str(self.n))
        '''

    # Transpose method should return a new matrix instance
    def transpose(self):
        m, n = self.shape(self)
        M_out = self.zero_matrix(self, m, n)
        for i in range(self.m):
            for j in range(self.n):
                M_out[j][i] = self[i][j]
        return M_out

    'Alternative below'

    # print(numpy.transpose(self))

    # Row and column methods to return nth row and column
    # nth row
    def row(self):
        for i in range(self.m):
            if i == self.m:
                print(i)
        return i

    # nth column
    def column(self):
        for j in range(self.n):
            if j == self.n:
                print(j)
        return j

    # to_list function returns matrix as a list of list

    # block methos to return 2-by-2 of [n0 m0],[n1 m1]


A = Matrix(5, 1)
A.zero_matrix(5, 1)
A.shape()
A.column()
