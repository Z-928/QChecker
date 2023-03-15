import qiskit
from qiskit import *
from qiskit import IBMQ
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)

circuit.draw(output='mpl')
circuit.h(qr(0))


'''
fix ver:


qc.draw(output='mpl')
qc.h(0)


'''
