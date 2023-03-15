from qiskit.aqua.algorithms import VQE
from qiskit.circuit.library import TwoLocal

num_qubits = 1
tl_circuit = TwoLocal(num_qubits, ['h', 'ry'], 'cz',
                      entanglement='Linear', reps=2, parameter_prefix = 'th')
callback = Callback()

#backend = Simulator.aer_manhattan_simulator
backend = Aer.get_backend('qasm_simulator')
anothor_solver = VQE(var_form = t1_circuit, optimazor=SPSA(maxiter=250),callback=callback,
                    quantum_instance = QuantumInstance(backend, shot=2048))

tl_circuit.draw()

'''
<fixed ver>
from qiskit.aqua.algorithms import VQE
from qiskit.circuit.library import TwoLocal

num_qubits = 4
tl_circuit = TwoLocal(num_qubits, ['h', 'rx'], 'cz',
                      entanglement='full', reps=3, parameter_prefix = 'y')

tl_circuit.draw(output = 'mpl')

another_solver = VQE(var_form = tl_circuit,
                     quantum_instance = QuantumInstance(BasicAer.get_backend('statevector_simulator')))
'''