import qiskit as qk
qc.mcx([0,1],2)
qk.QuantumCircuit.from_qasm_str(qc.qasm())
qk.QuantumCircuit.from_qasm_str(qc.qasm()) == qc
True
qc = qk.QuantumCircuit(4)
qc.mcx([0,1,2], 3)
print(qc.qasm())
'''
OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
mcx_gray q[0],q[1],q[2],q[3];
qk.QuantumCircuit.from_qasm_str(qc.qasm())
'''

'''
<fixed ver>
circ = qiskit.QuantumCircuit(3, 3)
'''