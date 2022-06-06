from functions.utilsQFT import *
import math
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