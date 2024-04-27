from qiskit import QuantumCircuit, execute
from numpy.random import randint
import numpy as np
from qiskit.providers.aer import AerSimulator

num_qubits = 15  # Adjusted to fit within the coupling map constraints

alice_basis = np.random.randint(2, size=num_qubits)
alice_state = np.random.randint(2, size=num_qubits)
bob_basis = np.random.randint(2, size=num_qubits)

print(f"Alice's State:\t {np.array2string(alice_state)}")
print(f"Alice's Bases:\t {np.array2string(alice_basis)}")
print(f"Bob's Bases:\t {np.array2string(bob_basis)}")

def bb84_circuit(state, basis, measurement_basis):
    num_qubits = len(state)
    circuit = QuantumCircuit(num_qubits)

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

    circuit.measure_all()

    return circuit

circuit = bb84_circuit(alice_state, alice_basis, bob_basis)
backend = AerSimulator()
job = backend.run(circuit, shots=1)
result = job.result()
key = list(result.get_counts().keys())[0][::-1]  # Get the key from the result counts
encryption_key = ''
for i in range(num_qubits):
    if alice_basis[i] == bob_basis[i]:
         encryption_key += str(key[i])
print(f"Key: {encryption_key}")
