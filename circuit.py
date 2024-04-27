from qiskit import QuantumCircuit, Aer, transpile, assemble
from numpy.random import randint
import numpy as np

num_qubits = 5

alice_basis = np.random.randint(2, size=num_qubits)
alice_state = np.random.randint(2, size=num_qubits)
bob_basis = np.random.randint(2, size=num_qubits)

print(f"Alice's State:\t {np.array2string(alice_state)}")
print(f"Alice's Bases:\t {np.array2string(alice_basis)}")
print(f"Bob's Bases:\t {np.array2string(bob_basis)}")

def bb84_circuit(state, basis, measurement_basis):
    num_qubits = len(state)
    circuit = QuantumCircuit(num_qubits, num_qubits)

    # Sender prepares qubits
    for i in range(len(basis)):
        if state[i] == 1:
            circuit.x(i)
        if basis[i] == 1:
            circuit.h(i)

    # Measuring action performed by Bob
    for i in range(len(measurement_basis)):
        if measurement_basis[i] == 1:
            circuit.h(i)

    circuit.measure(range(num_qubits), range(num_qubits))

    return circuit

circuit = bb84_circuit(alice_state, alice_basis, bob_basis)
print("BB84 Quantum Circuit:")
print(circuit)