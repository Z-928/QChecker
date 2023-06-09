from qiskit import QuantumCircuit
from qiskit.circuit import Gate
qc = QuantumCircuit(3)
qc.append(Gate('my_custom_3q_gate', 3, []), [0,1,2])
qc.h(0)
qc.sdg(0)
qc.y(1)
...

qc.add_calibration('my_custom_3q_gate', (0,1,2), my_custom_3q_gate_schedule)

qc = transpile(qc, backend, basis_gates=['u1', 'u2', 'u3', 'cx', 'my_custom_3q_gate'])
sched = schedule(qc, backend)


'''
qc.add_calibration('my_custom_3q_gate', (0,1,2), my_custom_3q_gate_schedule)
NameError: name 'my_custom_3q_gate_schedule' is not defined


CLASSGate(name, num_qubits, params, label=None)
'''

