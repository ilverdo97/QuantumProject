'''
qc: input quantum circuit
reg: input register to execute QFT
n: n-th qbit to apply hadamard and phase rotation
pie: pie number
'''

def executeQFT(qc, reg, n, pie):
    # Executes the QTF of reg, one qubit a time
    # Apply one Hadamard gate to the n-th qubit of the quantum register reg, and
    # then apply repeated phase rotations with parameters being pi divided by
    # increasing powers of two

    qc.h(reg[n])
    for i in range(0, n):
        # cp(theta, control_qubit, target_qubit[, …])
        qc.cp(pie / float(2 ** (i + 1)), reg[n - (i + 1)], reg[n])

    #print(qc.draw())

'''
qc: input quantum circuit
reg_a: first input register to execute QFT
reg_b: second input register to execute QFT
n: n-th qbit to apply hadamard and phase rotation
pie: pie number
'''

def evolveQFTStateSum(qc, reg_a, reg_b, n, pie):
    # Evolves the state |F(psi(reg_a))> to |F(psi(reg_a+reg_b))> using the QFT
    # conditioned on the qubits of the reg_b.
    # Apply repeated phase rotations with parameters being pi divided by
    # increasing powers of two.

    l = len(reg_b)
    for i in range(n + 1):
        if (n - i) > l - 1:
            pass
        else:
            # cp(theta, control_qubit, target_qubit[, ...])
            qc.cp(pie / float(2 ** (i)), reg_b[n - i], reg_a[n])

'''
qc: input quantum circuit
reg_a: first input register to execute QFT
reg_b: second input register to execute QFT
n: n-th qbit to apply hadamard and phase rotation
pie: pie number
'''

def evolveQFTStateSub(qc, reg_a, reg_b, n, pie):
    # Evolves the state |F(ψ(reg_a))> to |F(ψ(reg_a+reg_b))> using the quantum
    # Fourier transform conditioned on the qubits of the reg_b.
    # Apply repeated phase rotations with parameters being pi divided by
    # increasing powers of two.

    l = len(reg_b)
    for i in range(n + 1):
        if (n - i) > l - 1:
            pass
        else:
            qc.cp(-1 * pie / float(2 ** (i)), reg_b[n - i], reg_a[n])

'''
qc: input quantum circuit
reg: input register to execute QFT
n: n-th qbit to apply hadamard and phase rotation
pie: pie number
'''

def inverseQFT(qc, reg, n, pie):
    # Executes the inverse QFT on a register reg.
    # Apply repeated phase rotations with parameters being pi divided by
    # decreasing powers of two, and then apply a Hadamard gate to the nth qubit
    # of the register reg.

    for i in range(n):
        # cp(theta, control_qubit, target_qubit[, ...])
        qc.cp(-1 * pie / float(2 ** (n - i)), reg[i], reg[n])
    qc.h(reg[n])