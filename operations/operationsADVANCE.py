import qiskit
from functions.utils import *
from functions.utilsQubit import *
from operations.operationsBASE import *

#DIVISION---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
def div(first, second, dividend, divisor, qc, nqubit, cl):

    result = 0
    while True:
        sub(dividend, divisor, qc)
        tmp, prob = collass(qc, dividend, cl, nqubit)

        numdividend = int(tmp, 2)
        numdivisor = int(second, 2)

        result = result + 1
        if numdividend >= numdivisor:

            numdividend = '{0:{fill}11b}'.format(numdividend, fill='0')
            numdivisor = '{0:{fill}11b}'.format(numdivisor, fill='0')

            len1 = len(numdividend)
            len2 = len(numdivisor)
            nqubit, len1, len2, newnum, second = NQubit("/", len1, len2, numdividend, numdivisor)

            dividend = qiskit.QuantumRegister(nqubit + 1, "a")
            divisor = qiskit.QuantumRegister(nqubit + 1, "b")
            cl = qiskit.ClassicalRegister(nqubit + 1, "cl")
            qc = qiskit.QuantumCircuit(dividend, divisor, cl, name="qc")
            initQubits(numdividend, qc, dividend, nqubit)
            initQubits(numdivisor, qc, divisor, nqubit)

        else:
            break

    return int(first, 2), numdivisor, result, prob


#EXPONENTIAL------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
def exponential(a, firstDecBinary, firstDec, secondDec, result, qc, cl, nqubit):

    for x in range(secondDec - 1):

        multiply(a, firstDec, result, qc)
        tmp, prob = collass(qc, result, cl, nqubit)

        firstDec = int(tmp, 2)

        if x < (secondDec - 2):
            a = qiskit.QuantumRegister(nqubit + 1, "a")
            b = qiskit.QuantumRegister(nqubit + 1, "b")
            cl = qiskit.ClassicalRegister(nqubit + 1, "cl")
            qc = qiskit.QuantumCircuit(a, b, cl, name="qc")
            initQubits(firstDecBinary, qc, a, nqubit)

    if secondDec == 0:
        firstDec = 1
        prob = 100
    elif secondDec == 1:
        firstDec = int(firstDecBinary, 2)
        prob = 100

    return int(firstDecBinary, 2), secondDec, firstDec, prob
