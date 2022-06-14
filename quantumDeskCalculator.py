from operations.operationsADVANCE import *
from operations.operationsBASE import *

if __name__ == "__main__":

    while True:

        print(bcolors.OKGREEN + '##############################  Quantum Desk Calculator  ###############################' + bcolors.ENDC)

        # take the operator and check
        operator = selectOperator()

        # take and check number
        input1, input2 = checkNumber(operator)

        # check if the operations is valid
        checkOperation(input1, input2, operator)

        # covert number in binary for register
        first = '{0:{fill}5b}'.format(input1, fill='0')
        second = '{0:{fill}5b}'.format(input2, fill='0')
        len1 = len(first)
        len2 = len(second)

        # Calculate the correct number of qubit for operations
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
        cl = qiskit.ClassicalRegister(nqubit + 1, "cl")
        qc = qiskit.QuantumCircuit(a, b, cl, name="qc")

        # Flip the corresponding qubit in register a if a bit in the string first is a 1
        initQubits(first, qc, a, nqubit)
        # Flip the corresponding qubit in register b if b bit in the string second is a 1
        if operator == '+' or operator == '-' or operator == '/':
            initQubits(second, qc, b, nqubit)

        # Program switch in operation

        # BASE
        if operator == '+':
            sum(a,b,qc)
            printResult(first, second, qc, a, cl, nqubit, operator)
        elif operator == '-':
            sub(a,b,qc)
            printResult(first, second, qc, a, cl, nqubit, operator)
        elif operator == '*':
            multiply(a,input2,b,qc)
            printResult(first, second, qc, b, cl, nqubit ,operator)

        # ADVANCE
        elif operator == '/':
            prtFirst, prtSecond, prtResult, prtProb = div(first, second, a, b, qc, nqubit, cl)
            printResultADVANCE(prtFirst, prtSecond, prtResult, prtProb, operator, nqubit)
        elif operator == '^':
            prtFirst, prtSecond, prtResult, prtProb = exponential(a, first, input1, input2, b, qc, cl, nqubit)
            printResultADVANCE(prtFirst, prtSecond, prtResult, prtProb, operator, nqubit)

        print(bcolors.OKCYAN + '#'*150 + bcolors.ENDC)

        # Select a new operation or close program
        check = (input(bcolors.WARNING + "Would you like insert another operations ? ?? [y/n] \n" + bcolors.WARNING ))
        if (check =='y' or check =='Y' or check =='Yes' or check == 'YES' or check =='yes'):
            True
        elif (check =='n' or check =='N' or check =='No' or check == 'NO' or check =='no'):
            break

