from qiskit import *

qr = QuantumRegister(3)
cr = ClassicalRegister(3)
qc = QuantumCircuit(qr,cr)


qc.h(1)
qc.cx(1,2)

qc.measure(qr,cr) #let this be right.
