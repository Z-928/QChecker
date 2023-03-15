from qiskit import *
from qiskit.circuit.library import XGate
qr = QuantumRegister(36, "qr")
cr = ClassicalRegister(36, 'cr')
qc = QuantumCircuit(qr, cr)
for i in range(8, 12):
    qc.h(i)
gate = XGate().control(num_ctrl_qubits=4, ctrl_state='1111')
qc.append(gate, [8,9,10,11]+[4])
qc.barrier()
for i in range(36):
    qc.measure(i, i)
qc.draw(output='mpl', filename='out')
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim, shots=1024)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc)
res = []
for i in counts.keys():
    res.append(i)
print(res)

'''
ERROR:  [Experiment 0] Insufficient memory to run circuit circuit-0 using the statevector simulator.
'''


'''
fix var:


from qiskit.providers.aer import AerSimulator
backend_sim = AerSimulator(method='matrix_product_state')
'''
