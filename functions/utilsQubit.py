from qiskit import *

def initQubits(str, qc, reg, n):
    # Flip the corresponding qubit in register if a bit in the string is a 1
    for i in range(n):
        if str[i] == "1":
            qc.x(reg[n-(i+1)])

def NQubit(operator, len1, len2, first, second):
    if operator == '+' or operator == '-' or operator == '/':
        if len2>len1:
            first,second = second, first
            len2, len1 = len1, len2
        second = ("0") * (len1 - len2) + second
        tmpnqubit = len1
    elif operator == '*' or operator == '^':
        # Padding 'first' the same lenght of 'result'
        # since result can have at max len(first) + len(second) bits when multiplying
        first = ("0") * (len2) + first
        tmpnqubit = len1 + len2

    return tmpnqubit, len1, len2, first, second

def collass(qc, measure, cl, nqubit):

    # Measure qubits
    for i in range(nqubit + 1):
        qc.measure(measure[i], cl[i])

    job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=100)
    # Get results of program
    job_stats = job.result().get_counts()

    for key, value in job_stats.items():
        tmp = key
        prob = value

    return tmp, prob