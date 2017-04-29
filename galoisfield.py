def simplifyList(degree, A):
    temp1 = [0 for x in xrange(degree+1)]
    for x in xrange(degree+1):
        temp1[len(temp1)-1-x] = A[len(A)-1-x]
    return temp1

def reverse(A):
    return A[::-1]

def getDegree1(A):
    for i in range(len(A)):
        if i != 0 and A[i] == 1:
            return len(A) - 1 - i

def getDegree2(A):
    for i in range(len(A)):
        if A[i] == 1:
            return len(A) - 1 - i

def copyList(A):
    copy = []
    for i in range(len(A)):
        copy.append(A[i])
    return copy

def additionWithPrint(A,B,op):
    result = []
    A = reverse(A)
    B = reverse(B)
    if len(A) > len(B):
        result = addSupplement(A, B)
    else:
        result = addSupplement(B, A)
    result = reverse(result)
    A = reverse(A)
    B = reverse(B)

    m = getMaxLength(A, B, result)
    A = expandList(m, A)
    B = expandList(m, B)
    result = expandList(m, result)
    for x in range(len(A)):
        if A[x] == -1:
            print " ",
        else:
            print A[x],
    print
    B[0] = op
    for x in range(len(B)):
        if B[x] == -1:
            print " ",
        else:
            print B[x],
    print
    for x in xrange(2*m+1):
        print "_",
    print
    for x in range(len(result)):
        if result[x] == -1:
            print " ",
        else:
            print result[x],
    print

def additionWithPrint(A, B, op):
        A = reverse(A)
        B = reverse(B)
        if len(A) > len(B):
            result = addSupplement(A, B)
        else:
            result = addSupplement(B, A)
        result = reverse(result)
        A = reverse(A)
        B = reverse(B)

        m = getMaxLength(A, B, result)
        A = expandList(m, A)
        B = expandList(m, B)
        result = expandList(m, result)
        for x in range(len(A)):
            if A[x] == -1:
                print " ",
            else:
                print A[x],
        print
        B[0] = op
        for x in range(len(B)):
            if B[x] == -1:
                print " ",
            else:
                print B[x],
        print
        for x in xrange(2*m+1):
            print "_",
        print
        for x in range(len(result)):
            if result[x] == -1:
                print " ",
            else:
                print result[x],
        print

def addition(A, B):
    A = reverse(A)
    B = reverse(B)
    if len(A) > len(B):
        result = addSupplement(A, B)
    else:
        result = addSupplement(B, A)
    result = reverse(result)
    return result

def addSupplement(A, B):
    result = []
    for x in range(len(B)):
        result.append(A[x] ^ B[x])
    diff = len(A) - len(B)
    for u in xrange(diff):
        result.append(A[len(B)+u])
    return result

def plainmult(A, B):
    #max = len(A)+len(B)+1
    a = reverse(A)
    b = reverse(B)
    prod = [0 for x in xrange(len(A)+len(B)-1)]
    for i in range(len(b)):
        for j in range(len(a)):
            prod[i+j] = (prod[i+j] + (b[i] * a[j])) % 2
    prod = reverse(prod)


    #m = getMaxLength(A, B, prod)
    m = getMaxLength(A, B, prod)
    Aa = expandList(m, A)
    Bb = expandList(m, B)
    row = []
    for x in range(len(Aa)):
        if Aa[x] == -1:
            print " ",
        else:
            print Aa[x],
    print
    Bb[0] = "x"
    for x in range(len(Bb)):
        if Bb[x] == -1:
            print " ",
        else:
            print Bb[x],
    print
    for x in xrange(2*m+1):
        print "_",
    print
    a = reverse(A)
    b = reverse(B)
    for i in range(len(b)):
        for j in range(len(a)):
            row.append(a[j] * b[i])
        row = reverse(row)
        row += i*[-1]
        row = expandList(m, row)
        if (i==len(b)-1):
            row[0] = "+"
        for x in range(len(row)):
            if row[x] == -1:
                print " ",
            else:
                print row[x],
        print
        row = []
    for x in xrange(2*m+1):
        print "_",
    print
    pr = expandList(m, prod)
    for x in range(len(pr)):
        if pr[x] == -1:
            print " ",
        else:
            print pr[x],
    print
    return prod

def multiplication(A, B):
    '''prod = []
    if len(A) < len(B):
        prod = plainmult(B, A)
    else:'''
    prod = plainmult(A, B)
    diff = len(prod) - len(P)
    if (diff < 0):
        return prod
    else:
        print "\nSince the degree of the product", prod, "is greater than or equal to the degree of the irreducible polynomial", P, ", modulo reduction is needed. Using the irreducible polynomial,\n"
        prod = multModulo(prod, P)

        return prod

def multModulo(prod, P):
    qDegree = 0
    prodcopy = copyList(prod)
    diff = len(prod) - len(P)
    coeffs = []
    qDegree = getDegree1(P)
    print "x^"+ str(len(P)-1), "="
    for i in xrange(diff+1):
        prodcopy[i] = 0
        coeffs.append(prod[i])
    coeffs = reverse(coeffs)
    for x in range(len(coeffs)):
        print x, coeffs[x]
    for i in range(len(coeffs)):
        #print "x ^", len(prod) - 1 - i, "=",
        if coeffs[i] == 1:
            temp2 = [0 for x in xrange(qDegree+i+1)]
            temp1 = simplifyList(qDegree, P)
            print temp1
            for j in range(len(temp1)):
                pos = (j - i ) % len(temp1)
                temp2[pos] = temp1[j]
            print temp2
            prodcopy = addition(prodcopy, temp2)
    prodDeg = getDegree1(prodcopy)
    prodcopy = simplifyList(prodDeg, prodcopy)
    return prodcopy

def division(P, B):
    S = copyList(P)
    R = copyList(B)
    V = [0]
    U = [1]
    while getDegree2(R) != 0:
        delta = getDegree2(S) - getDegree2(R)
        if (delta < 0):
            temp = copyList(S)
            S = copyList(R)
            R = copyList(temp)
            temp = copyList(V)
            V = copyList(U)
            U = copyList(temp)
            delta = -(delta)
        xRaisedToDelta = [0 for x in xrange(delta+1)]
        xRaisedToDelta[0] = 1
        prod = plainmult(xRaisedToDelta, R)
        summ = addition(S, prod)
        S = simplifyList(getDegree2(summ), summ)
        prod = plainmult(xRaisedToDelta, U)
        summ = addition(V, prod)
        V = simplifyList(getDegree2(summ), summ)
    return multiplication(A, U)

A = raw_input("A(x): ")
B = raw_input("B(x): ")
P = raw_input("P(x): ")

A = A.split()
B = B.split()
P = P.split()

A = simplifyList(getDegree2([int(a) for a in A]), [int(a) for a in A])
B = simplifyList(getDegree2([int(b) for b in B]), [int(b) for b in B])
P = simplifyList(getDegree2([int(p) for p in P]), [int(p) for p in P])

def getMaxLength(A, B, r):
    maxLength = 0
    if len(A) > maxLength:
        maxLength = len(A)
    if len(B) > maxLength:
        maxLength = len(B)
    if len(r) > maxLength:
        maxLength = len(r)
    return maxLength


def expandList(max, list):
    expanded = [-1 for x in xrange(2*max+1)]
    l = copyList(list)
    for x in range(len(l)):
        expanded[(2*x)+(2*(max-len(list)+1))] = l[x]
    return (expanded)

print
print "============ Addition ============\n\n"
additionWithPrint(A, B, "+")
print
print "============ Subtraction ============\n\n"
additionWithPrint(A, B, "-")
print
print "============ Multiplication ============\n\n"
print multiplication(A, B)
