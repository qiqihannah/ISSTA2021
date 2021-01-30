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
    s = s.zfill(11)
    return s


def inverse(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '0':
            s_list[i] = '1'
        else:
            s_list[i] = '0'
    s = "".join(s_list)
    return s


def Decrement(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./Decrement_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def Decrement_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.cnot(q[6], q[0])  # M1

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./Decrement_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def Decrement_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.swap(q[6], q[0])  # M2

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./Decrement_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def Decrement_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    qc.cnot(q[6], q[0])  # M3

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./Decrement_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def Decrement_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    qc.swap(q[6], q[0])  # M4

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./Decrement_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def Decrement_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    qc.cswap(q[5], q[8], q[0])  # M5

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./Decrement_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def Decrement_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    q = QuantumRegister(11)
    qc = QuantumCircuit(q)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.h(q[2])
    qc.p(math.pi / 4, q[2])

    qc.barrier(q)

    qc.x(q[0])
    for i in range(1, 11):
        qc.mct(list(range(i)), i)

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = Decrement_specification(input)
    for i in range(2048):
        pt.append(abs(t[i]) ** 2)
    return pt
