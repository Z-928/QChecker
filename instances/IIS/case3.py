import qiskit
from qiskit import IBMQ
from qiskit.providers.aer import QasmSimulator

# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3, 2)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure([0, 1, 2], [0, 1 ,2])

# Construct an ideal simulator
sim = QasmSimulator()

# Perform an ideal simulation
result_ideal = qiskit.execute(circ, sim).result()
counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)
# Counts(ideal): {'000': 493, '111': 531}

# Construct a noisy simulator backend from an IBMQ backend
# This simulator backend will be automatically configured
# using the device configuration and noise mode
provider = IBMQ.load_account()
vigo_backend = provider.get_backend('ibmq_vigo')
vigo_sim = QasmSimulator.from_backend(vigo_backend)

# Perform noisy simulation
result_noise = qiskit.execute(circ, vigo_sim).result()
counts_noise = result_noise.get_counts(0)

print('Counts(noise):', counts_noise)
# Counts(noise): {'000': 492, '001': 6, '010': 8, '011': 14, '100': 3, '101': 14, '110': 18, '111': 469}


'''
<fixed ver>
circ = qiskit.QuantumCircuit(3, 3)
'''