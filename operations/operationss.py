#ADDICTION--------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
import math
from qiskit import *
from functions.utilsQFT import *

pie = math.pi

def sum(a, b, qc):
    n = len(a) - 1
    # Compute the Fourier transform of register a

    for i in range(n + 1):
        executeQFT(qc, a, n - i, pie)

    # Add the two numbers by evolving the Fourier transform F(ψ(reg_a))>
    # to |F(ψ(reg_a+reg_b))>
    for i in range(n + 1):
        evolveQFTStateSum(qc, a, b, n - i, pie)

        # Compute the inverse Fourier transform of register a
    for i in range(n + 1):
        inverseQFT(qc, a, i, pie)

#SUBTRACTION------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
def sub(a, b, qc):
    n = len(a)

    # Compute the Fourier transform of register a
    for i in range(0, n):
        executeQFT(qc, a, n - (i + 1), pie)
    # Add the two numbers by evolving the Fourier transform F(ψ(reg_a))>
    # to |F(ψ(reg_a-reg_b))>
    for i in range(0, n):
        evolveQFTStateSub(qc, a, b, n - (i + 1), pie)
        # Compute the inverse Fourier transform of register a
    for i in range(0, n):
        inverseQFT(qc, a, i, pie)

#MULTIPLICATION---------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

def multiply(a, secondDec, result, qc):
    n = len(a) - 1
    # Compute the Fourier transform of register 'result'
    for i in range(n + 1):
        executeQFT(qc, result, n - i, pie)

    # Add the two numbers by evolving the Fourier transform F(ψ(reg_a))>
    # to |F(ψ((second * reg_a))>, where we loop on the sum as many times as 'second' says,
    # doing incremental sums
    for j in range(secondDec):
        for i in range(n + 1):
            evolveQFTStateSum(qc, result, a, n - i, pie)

    # Compute the inverse Fourier transform of register a
    for i in range(n + 1):
        inverseQFT(qc, result, i, pie)

#DIVISION---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
def div(dividend, divisor, accumulator, c_dividend, circ, cl_index):
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

    sub(accumulator, d, circ)