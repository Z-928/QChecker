from qiskit import *
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
result = execute(circuit, backend, shots=1000).result()
counts  = result.get_counts(circuit)
print(counts)

'''
fix ver:


backend = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend, shots=1000).result()

# Get the statevector from result().

statevector = result.get_statevector(circuit)
print(statevector)

'''
