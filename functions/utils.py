from qiskit import *
import math
import time
import progressbar

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def selectOperator():
    valid_operators = ["+", "-", "*", "/"]
    operator = input(bcolors.WARNING + "\nSelect one operator [+ addition, - subtraction, * multiplication, / division]:  " + bcolors.ENDC)
    
    # Check valid operator
    if not(operator in valid_operators):
        print(bcolors.FAIL + f"Invalid operator, you can choose between these: {valid_operators}" + bcolors.ENDC)
        quit()

    return operator

def checkNumber(input1, input2):
    # check the inputs
    while (input1 < 0 or input1 > 2047) or (input2 < 0 or input2 > 2047):
        if input1 < 0 or input1 > 2047:
            #print(bcolors.FAIL + "Invalid first input number" + bcolors.ENDC)
            input1 = int(input(bcolors.WARNING + "Enter a first positive integer between 0 and 2047:\n" + bcolors.ENDC))

        if input2 < 0 or input2 > 2047:
            #print(bcolors.FAIL + "Invalid second input number" + bcolors.ENDC)
            input2 = int(input(bcolors.WARNING + "Enter a second positive integer between 0 and 2047:\n" + bcolors.ENDC))

    return input1, input2

def checkOperation(input1, input2, operator):
    if operator == '-' and input1 < input2:
        print(bcolors.FAIL + f"Invalid operation, you are trying to subtract a larger number from a smaller one" + bcolors.ENDC)
        quit()
    
    if operator == '/' and input2 == 0:
        print(bcolors.FAIL + f"Invalid operation, division by 0 is not allowed" + bcolors.ENDC)
        quit()

def printResult(first, second, qc,result, cl, n, operator):
    # Measure qubits
    for i in range(n+1):
        qc.measure(result[i], cl[i])

    # Execute using the local simulator
    print(bcolors.BOLD + bcolors.OKCYAN + 'Connecting to local simulator...' + bcolors.ENDC)

    # Set chosen backend and execute job
    num_shots = 100 #Setting the number of times to repeat measurement
    #print(bcolors.BOLD + bcolors.OKCYAN + 'Connect!' + bcolors.ENDC)
    #print(bcolors.BOLD + bcolors.OKCYAN + f'Running the experiment on {num_shots} shots...' + bcolors.ENDC)
    job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=num_shots)

    for i in progressbar.progressbar(range(100)):
        time.sleep(0.02)

    # Get results of program
    job_stats = job.result().get_counts()

    for key, value in job_stats.items():
        res = key
        prob = value
    print(bcolors.BOLD + bcolors.OKGREEN + f'\n{first} {operator} {second} = {res} with a probability of {prob}%' + bcolors.ENDC)

def initQubits(str, qc, reg, n):
    # Flip the corresponding qubit in register if a bit in the string is a 1
    for i in range(n):
        if str[i] == "1":
            qc.x(reg[n-(i+1)])
