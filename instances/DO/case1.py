from qiskit import *
circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.measure(0, 0)
circuit.cx(0,1)
circuit.iden(0)
print(circuit)
