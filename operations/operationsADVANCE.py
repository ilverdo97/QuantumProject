#ADDICTION--------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
import math

import time
import progressbar
import qiskit
from qiskit import *

from functions.utils import printResult, bcolors
from functions.utilsQFT import *
from functions.utilsQubit import initQubits

#DIVISION---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
from operations.operationsBASE import *


def div(dividend, divisor, accumulator, c_dividend, circ, cl_index, nqubit, first, second):
    d = QuantumRegister(1)
    circ.add_register(d)
    circ.x(d[0])

    c_dividend_str = '0'

    while c_dividend_str[0] == '0':
        sub(dividend, divisor, circ)
        sum(accumulator, d, circ)

        for i in range(len(dividend)):
            circ.measure(dividend[i], c_dividend[i])

        result = execute(circ, backend=Aer.get_backend('qasm_simulator'), shots=10).result()

        counts = result.get_counts("qc")
        # print(counts)
        c_dividend_str = list(counts.keys())[0]  # .split()[0]

        a = qiskit.QuantumRegister(nqubit + 1, "a")
        b = qiskit.QuantumRegister(nqubit + 1, "b")
        cl = qiskit.ClassicalRegister(nqubit + 1, "cl")
        qc = qiskit.QuantumCircuit(a, b, cl, name="qc")

        initQubits(first, qc, a, nqubit)
        initQubits(second, qc, b, nqubit)

    sub(accumulator, d, circ)

#EXPONENTIAL------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def exponential(a, firstDecBinary, firstDec, secondDec, operator, result, qc, cl, nqubit):

    for x in range(secondDec - 1):

        #print(firstDecBinary, firstDec)
        multiply(a, firstDec, result, qc)

        # Measure qubits
        for i in range(nqubit + 1):
            qc.measure(result[i], cl[i])

        job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=100)

        # Get results of program
        job_stats = job.result().get_counts()

        for key, value in job_stats.items():
            tmp = key
            prob = value

        firstDec = int(tmp, 2)
        #print(firstDec)

        if x < (secondDec - 2):
            a = qiskit.QuantumRegister(nqubit + 1, "a")
            b = qiskit.QuantumRegister(nqubit + 1, "b")
            cl = qiskit.ClassicalRegister(nqubit + 1, "cl")
            qc = qiskit.QuantumCircuit(a, b, cl, name="qc")
            initQubits(firstDecBinary, qc, a, nqubit)

    print(bcolors.BOLD + bcolors.OKCYAN + 'Create and Connecting to local simulator...' + bcolors.ENDC)

    for i in progressbar.progressbar(range(100)):
        time.sleep(0.005*nqubit)

    if secondDec == 0:
        firstDec = 1
        prob = 100
    elif secondDec == 1:
        firstDec = int(firstDecBinary, 2)
        prob = 100

    print(bcolors.BOLD + bcolors.OKGREEN + f'\n{int(firstDecBinary, 2)} {operator} {secondDec} = {firstDec} with a probability of {prob}%' + bcolors.ENDC)
