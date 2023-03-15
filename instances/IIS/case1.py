from qiskit import *

def get_circuit(n):
    creg = ClassicalRegister(n)
    dreg = ClassicalRegister(1)
    
    qreg = QuantumRegister(n)
    mreg = QuantumRegister(1)
    
    circ = QuantumCircuit(qreg, mreg, creg, dreg)
    
    
    for i in range(n):
        circ.measure(qreg[0], creg[i])
    
    circ.x(mreg[0]).c_if(creg, 0)
    circ.measure(mreg[0], dreg[0])

    return circ


sim_basic_aer = BasicAer.get_backend('qasm_simulator')
sim_aer = Aer.get_backend('qasm_simulator')
circ72 = get_circuit(6)
circ48 = get_circuit(48)


print("72 clbits (Aer)       : ", execute(circ72, sim_aer).result().get_counts())
print("72 clbits (Basic Aer) : ", execute(circ72, sim_basic_aer).result().get_counts())
print("")
print("48 clbits (Aer)       : ", execute(circ48, sim_aer).result().get_counts())
print("48 clbits (Basic Aer) : ", execute(circ48, sim_basic_aer).result().get_counts())