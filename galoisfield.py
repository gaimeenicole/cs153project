import os
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

def getLastIndex(list):
    ind = 0
    for i in range(len(list)):
        if list[i] == 1:
            ind = i
    return ind
def printList (list):
    lastIndex = getLastIndex(list)
    for i in range(len(list)):
        if list[i] == 1:
            if (i != len(list)-1):
                print "x^"+str(((-i-1)%(len(list)+1))-1),
            else:
                print str(1),
            if i != lastIndex:
                print "+",

def additionWithPrint(A,B,op):
    aDeg = getDegree2(A)
    bDeg = getDegree2(B)
    pDeg = getDegree2(P)

    '''if aDeg >= pDeg:
        print "The degree of A is greater than or equal to P so it needs to be reduced."
        aaa = multModulo(A, P)
        while getDegree2(aaa) >= getDegree2(P):
            aaa = multModulo(aaa, P)
    if bDeg >= pDeg:
        print "The degree of A is greater than or equal to P so it needs to be reduced."
        bbb = multModulo(B, P)
        while getDegree2(bbb) >= getDegree2(P):
            bbb = multModulo(bbb, P)

    A = copyList(aaa)
    B = copyList(bbb)'''
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
    r = copyList(result)
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
    

'''def additionWithPrint(A, B, op):
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
'''
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

def plainmult(A, B, mode):
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
    if mode != "div":
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
        if mode != "div":
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
    if mode != "div":
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

def multiplication(A, B, mode):
    '''prod = []
    if len(A) < len(B):
        prod = plainmult(B, A)
    else:'''
    prod = plainmult(A, B, mode)
    diff = len(prod) - len(P)
    if (diff < 0):
        return prod
    else:
        print "\nSince the degree of the product", printList(prod), "is greater than or equal to the degree of the irreducible polynomial", printList(P), ", modulo reduction is needed. Using the irreducible polynomial,\n"

        prod = multModulo(prod, P)
        while getDegree2(prod) >= getDegree2(P):
            prod = multModulo(prod, P)
        print "The final answer is:",
        printList(prod)
        return prod

def multModulo(prod, P):
    qDegree = 0
    prodcopy = copyList(prod)
    diff = len(prod) - len(P)
    coeffs = []
    qDegree = getDegree1(P)
    for i in xrange(diff+1):
        prodcopy[i] = 0
        coeffs.append(prod[i])
    coeffs = reverse(coeffs)

    for i in range(len(coeffs)):
        if coeffs[i] == 1:
            temp2 = [0 for x in xrange(qDegree+i+1)]
            temp1 = simplifyList(qDegree, P)
            print "x^"+str(getDegree2(P) + i), "=",
            for j in range(len(temp1)):
                temp2[j] = temp1[j]
            printList(temp2)
            print
            prodcopy = addition(prodcopy, temp2)
    print "\nWe substitute the equations above to and perform usual addition. \n"
    prodDeg = getDegree1(prodcopy)
    prodcopy = simplifyList(prodDeg, prodcopy)

    return prodcopy

def reduceList(list, P):
    l = copyList(list)
    qDegree = getDegree2(P)
    #while getDegree2(l) >= getDegree2(P):
    l = copyList(l)
    print l
    coeffs = []
    diff = len(l) - len(P)
    print diff
    for i in xrange(diff+1):
        coeffs.append(l[i])
        l[i] = 0

        #print l[i]
    coeffs = reverse(coeffs)
    print coeffs
    for i in range(len(coeffs)):
        if coeffs[i] == 1:
            temp2 = [0 for x in xrange(qDegree+i+1)]
            temp1 = simplifyList(qDegree, P)
            print "temp1",temp1
            #print "x^"+str(getDegree2(P) + i), "=",
            for j in range(len(temp1)):
                temp2[j] = temp1[j]
            print "temp2",temp2
            print l
            printList(temp2)
            #print

            l = addition(l, temp2)

    #print l

def division(P, B):
    S = copyList(P)
    R = copyList(B)
    V = [0]
    U = [1]
    while getDegree2(R) != 0:
        print
        delta = getDegree2(S) - getDegree2(R)
        if (delta < 0):
            temp = copyList(S)
            S = copyList(R)
            R = copyList(temp)
            temp = copyList(V)
            V = copyList(U)
            U = copyList(temp)
            delta = -(delta)
        print "R(x) = ",
        printList(R)
        print
        print "S(x) =",
        printList(S)
        print
        print "U(x) = ",
        printList(U)
        print
        print "V(x) = ",
        printList(V)
        print

        xRaisedToDelta = [0 for x in xrange(delta+1)]
        xRaisedToDelta[0] = 1
        prod = plainmult(xRaisedToDelta, R, "div")
        summ = addition(S, prod)
        S = simplifyList(getDegree2(summ), summ)
        prod = plainmult(xRaisedToDelta, U, "div")
        summ = addition(V, prod)
        V = simplifyList(getDegree2(summ), summ)
    print
    print "R(x) = ",
    printList(R)
    print
    print "S(x) =",
    printList(S)
    print
    print "U(x) = ",
    printList(U)
    print
    print "V(x) = ",
    printList(V)
    print
    print "\nThe inverse of", printList(B), "is", printList(U), ". Then, we multiply the inverse to A, which is,", printList(A), "."
    return multiplication(A, U, "mult")

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


#def main():
os.system('cls' if os.name == 'nt' else 'clear')

A = raw_input("A(x): ")
B = raw_input("B(x): ")
P = raw_input("P(x): ")

A = A.split()
B = B.split()
P = P.split()

try:
    A = simplifyList(getDegree2([int(a) for a in A]), [int(a) for a in A])
    B = simplifyList(getDegree2([int(b) for b in B]), [int(b) for b in B])
    P = simplifyList(getDegree2([int(p) for p in P]), [int(p) for p in P])
    print "Pasado"
except ValueError:
    print "Input must only contain integers."
print A,B,P
#multiplication(A, B, "mult")
print
print "[a] Addition"
print "[s] Subtraction"
print "[m] Multiplication"
print "[d] Division"
print "[q] Quit"
choice = raw_input("Choose operation: ")
while choice != "q":

    if choice == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        print " ============= ADDITION ============="
        additionWithPrint(A, B, "+")
    if choice == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        print " ============= SUBTRACTION ============="
        additionWithPrint(A, B, "-")
    if choice == 'm':
        os.system('cls' if os.name == 'nt' else 'clear')
        print " ============= MULTIPLICATION ============="
        multiplication(A, B, "mult")
    if choice == 'd':
        os.system('cls' if os.name == 'nt' else 'clear')
        print " ============= DIVISION ============="
        division(P,B)
    print
    print
    print "[a] Addition"
    print "[s] Subtraction"
    print "[m] Multiplication"
    print "[d] Division"
    print "[q] Quit"
    print
    choice = raw_input("Choose operation: ")
