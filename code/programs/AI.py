import math

from qiskit import (
    # IBMQ,
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)


def dec2bin(n):
    a = 1
    list = []
    while a > 0:
        a, b = divmod(n, 2)
        list.append(str(b))
        n = a
    s = ""
    for i in range(len(list) - 1, -1, -1):
        s += str(list[i])
    s = s.zfill(10)
    return s


def AI(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.cn

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AI_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AI_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.cnot(a[6], a[0])  # M1

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AI_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AI_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.swap(a[6], a[0])  # M2

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AI_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AI_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    qc.ccx(a[5], a[6], a[0])  # M3

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AI_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AI_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    qc.barrier(a)

    qc.cnot(a[6], a[0])  # M4

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AI_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AI_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    qc.barrier(a)

    qc.cswap(a[5], a[8], a[0])  # M5

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AI_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AI_specificAIon(input):
    simulator = Aer.get_backend('statevector_simulator')
    a = QuantumRegister(11)
    b = QuantumRegister(2)
    qc = QuantumCircuit(a, b)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])
    qc.barrier(a)

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    qc.barrier(b)

    for i in range(10):
        control = []
        control.append(b[0])
        for j in range(10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(9):
        control = []
        control.append(b[1])
        for j in range(1, 10 - i):
            control.append(a[j])
        qc.mct(control, a[10 - i])
    qc.cnot(b[1], a[1])

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = AI_specificAIon(input)
    for i in range(2048):
        temp = 0
        for j in range(4):
            temp += abs(t[i + j * 2048]) ** 2
        pt.append(temp)
    return pt
