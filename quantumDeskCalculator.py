import qiskit

from QuantumProject.functions.utils import bcolors, selectOperator, checkNumber, checkOperation, printResult
from QuantumProject.functions.utilsQubit import NQubit, initQubits
from QuantumProject.operations.operationsADVANCE import exponential, div
from QuantumProject.operations.operationsBASE import sub, multiply
from operations import *
from functions import *

if __name__ == "__main__":


    while True:

        print(bcolors.OKGREEN + '##################  Quantum Desk Calculator  ###################' + bcolors.ENDC)

        # take the operator and check
        operator = selectOperator()

        # take number
        input1 = -1
        input2 = -1
        input1, input2 = checkNumber(input1, input2, operator)

        # check if the operations is valid
        checkOperation(input1, input2, operator)

        first = '{0:{fill}5b}'.format(input1, fill='0')
        second = '{0:{fill}5b}'.format(input2, fill='0')
        len1 = len(first)
        len2 = len(second)

        # Making sure that 'first' and 'second' are of the same length
        # by padding the smaller string with zeros

        nqubit, len1, len2, first, second = NQubit(operator, len1, len2, first, second)
        print(bcolors.OKCYAN + '#'*150 + bcolors.ENDC)
        print('You want to perform the following operations:')
        print(f'{input1} {operator} {input2} = ...')

        # create the register based on the operations choosen

        # Add a qbit to 'a' and 'b' in case of overflowing results
        # (the result is only read on 'a' or 'accumulator', but since 'a' (or 'accumulator') and 'b'
        # should have the same lenght, we also add a qbit to 'b')
        a = qiskit.QuantumRegister(nqubit + 1, "a")
        b = qiskit.QuantumRegister(nqubit + 1, "b")
        accumulator = qiskit.QuantumRegister(nqubit + 1, "accumulator")
        cl = qiskit.ClassicalRegister(nqubit + 1, "cl")

        if operator == '+' or operator == '-' or operator == '*' or operator == '^':
            qc = qiskit.QuantumCircuit(a, b, cl, name="qc")
            # Flip the corresponding qubit in register a if a bit in the string first is a 1
            initQubits(first, qc, a, nqubit)
            # Flip the corresponding qubit in register b if b bit in the string second is a 1
            if operator == '+' or operator == '-':
                initQubits(second, qc, b, nqubit)

            if operator == '+':
                sum(a,b,qc)
                printResult(first, second, qc, a, cl, nqubit, operator)
            elif operator == '-':
                sub(a,b,qc)
                printResult(first, second, qc, a, cl, nqubit, operator)
            elif operator == '*':
                multiply(a,input2,b,qc)
                printResult(first, second, qc, b, cl, nqubit ,operator)
            elif operator == '^':
                exponential(a, first, input1, input2, operator, b, qc, cl, nqubit)
                #printResult(first, second, qc, a, cl, nqubit , operator)


        elif operator == '/':
            qc = qiskit.QuantumCircuit(a, b, accumulator, cl, name="qc")
            # Flip the corresponding qubit in register a and b if a,b bit in the string first,second is a 1
            initQubits(first, qc, a, nqubit)
            initQubits(second, qc, b, nqubit)

            div(a, b, accumulator, cl, qc, 0, nqubit, first, second)
            printResult(first, second, qc, accumulator, cl, nqubit, operator)

        print(bcolors.OKCYAN + '#'*150 + bcolors.ENDC)

        check = (input(bcolors.WARNING + "Vuoi fare ancora operazioni ?? [y/n] \n" + bcolors.WARNING ))
        if (check =='n' or check =='N' or check =='No' or check == 'NO' or check =='no'):
            break

