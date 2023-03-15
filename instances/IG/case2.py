
from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit

test_gate = Gate('test',num_qubits=1,params=[])
test_qasm = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n\nqreg q[2];\ncreg cr[2];\ntest q[0];\n'

test_circ = QuantumCircuit.from_qasm_str(test_qasm)



'''
qiskit.qasm.exceptions.QasmError: "Cannot find gate definition for 'test', line 6 file "

defining a python Gate object in qiskit, but the definition for that gate is not included the qasm string passed to QuantumCircuit.from_qasm_str, leading to the error.

Problem:User-defined Gate objects are not properly being exported to qasm as opaque gates.
Solution:Can declare a custom opaque gate using the opaque statement,or a non-opaque gate using the gate statement


'''
