from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import Aer, compile
from qiskit.backends.jobstatus import JOB_FINAL_STATES

n_qubits = 5
qc_list = []
for i in range(n_qubits):
    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_qubits)
    qc = QuantumCircuit(qr, cr)
    qc.x(qr[i])
    qc.measure(qr, cr)
    qc_list.append(qc)

backend = Aer.get_backend('qasm_simulator')
qobj_list = [compile(qc, backend) for qc in qc_list]
job_list = [backend.run(qobj) for qobj in qobj_list]

while job_list:
    for job in job_list:
        if job.status() in JOB_FINAL_STATES:
            job_list.remove(job)
            print(job.result().get_counts())



'''
DeprecationWarning: qiskit.compile() is deprecated and will be removed in Qiskit Terra 0.9.
Please use qiskit.compiler.transpile() to transform circuits and qiskit.compiler.assemble() to produce a runnable qobj. DeprecationWarning)
'''



'''
fix ver:


from qiskit import *
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import Aer

from qiskit.compiler import transpile, assemble

n_qubits = 5
qc_list = []

for i in range(n_qubits):
    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_qubits)
    qc = QuantumCircuit(qr, cr)
    qc.x(qr[i])
    qc.measure(qr, cr)
    qc_list.append(qc)

backend = Aer.get_backend('qasm_simulator')
transpiled_circs = transpile(qc_list, backend=backend)
qobjs = assemble(transpiled_circs, backend=backend)
job_info = backend.run(qobjs)
for circ_index in range(len(transpiled_circs)):
    print(job_info.result().get_counts(transpiled_circs[circ_index]))
'''
