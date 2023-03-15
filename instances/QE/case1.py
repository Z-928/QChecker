from qiskit import QuantumCircuit, Aer, compile, execute
backend = Aer.get_backend('qasm_simulator_py')

qasm = '''OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
creg c[1];
measure q -> c;'''
qc = QuantumCircuit()
qc.from_qasm_str(qasm)

print( qc.qasm() )




# fix ver:

# from qiskit import *


# qasm = '''OPENQASM 2.0;
# include "qelib1.inc";
# qreg q[1];
# creg c[1];
# measure q -> c;'''
# qc = QuantumCircuit.from_qasm_str(qasm)

# print( qc.qasm() )



'''
The from_qasm_str() method is a static constructor, it operates off the class to return a circuit object based on the input qasm.
In the example , creating a blank circuit with "qc = QuantumCircuit()",
then creating a new circuit based on the qasm with "qc.from_qasm_str(qasm)" but never doing anything with it so it's not saved.
Then you go back and try to use "qc" which is the blank circuit you created.
'''
