import time
import progressbar
from qiskit import *

class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

def selectOperator():
    valid_operators = ["+", "-", "*", "/", "^"]
    operator = input("\nSelect one operator [+ addition, - subtraction, * multiplication, / division, ^ exponential]: ")
    
    # Check valid operator
    while not(operator in valid_operators):
        print(bcolors.FAIL + f"Invalid operator, you can choose between these: {valid_operators}" + bcolors.ENDC)
        operator = input("\nSelect one operator valid [+ addition, - subtraction, * multiplication, / division, ^ exponential]: ")

    return operator

def checkNumber(operator):
    # check the inputs

    input1 = -1
    input2 = -1
    while (input1 < 0 or input1 > 2000) or (input2 < 0 or input2 > 2000):
        if (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
            if input1 < 0 or input1 > 2000:
                input1 = int(input("Enter a first positive integer between 0 and 2000:\n"))

            if input2 < 0 or input2 > 2000:
                input2 = int(input("Enter a second positive integer between 0 and 2000:\n"))
        elif operator == '^':
            if input1 < 0 or input1 > 2000:
                input1 = int(input("Enter a first positive integer between 0 and 2000:\n"))

            if input2 < 0 or input2 > 2000:
                input2 = int(input("Enter with esponential:\n"))

    return input1, input2

def checkOperation(input1, input2, operator):
    if operator == '-' and input1 < input2:
        print(bcolors.FAIL + f"Invalid operation, you are trying to subtract a larger number from a smaller one" + bcolors.ENDC)
        quit()
    
    if operator == '/' and input2 == 0:
        print(bcolors.FAIL + f"Invalid operation, division by 0 is not allowed" + bcolors.ENDC)
        quit()

# Collass the circuit and print result of operation
def printResult(first, second, qc, result, cl, n, operator):
    # Execute using the local simulator
    print(bcolors.BOLD + bcolors.OKCYAN + 'Create and Connecting to local simulator...' + bcolors.ENDC)

    # Measure qubits
    for i in range(n+1):
        qc.measure(result[i], cl[i])

    # Set chosen backend and execute job and get result
    num_shots = 100 #Setting the number of times to repeat measurement
    job_stats = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=num_shots).result().get_counts()

    # Take the result and value of job
    for key, value in job_stats.items():
        res = key
        prob = value

    for i in progressbar.progressbar(range(100)):
        time.sleep(0.005*n)

    #print(bcolors.BOLD + bcolors.OKGREEN + f'\n{first} {operator} {second} = {res} with a probability of {prob}%' + bcolors.ENDC)
    print(bcolors.BOLD + bcolors.OKGREEN + f'\n{int(first, 2)} {operator} {int(second,2)} = {int(res, 2)} with a probability of {prob}%' + bcolors.ENDC)

    # Print circuit
    #print(qc.decompose().draw())

# Print result, because the in operation we go collass operation for temporaly result
def printResultADVANCE(prtFirst, prtSecond, prtResult, prtProb, operator, nqubit):
    print(bcolors.BOLD + bcolors.OKCYAN + 'Create and Connecting to local simulator...' + bcolors.ENDC)

    for i in progressbar.progressbar(range(100)):
        time.sleep(0.005 * nqubit)

    print(bcolors.BOLD + bcolors.OKGREEN + f'\n{prtFirst} {operator} {prtSecond} = {prtResult} with a probability of {prtProb}%' + bcolors.ENDC)


