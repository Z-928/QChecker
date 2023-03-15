p = QuantumCircuit(8)
p.x(0)
q = QuantumCircuit(8)
q.x(0)

adder = circuit.library.arithmetic.adders.cdkm_ripple_carry_adder.CDKMRippleCarryAdder(8)
adder.compose(p, [1,2,3,4,5,6,7,8], inplace=True, front=True)
adder.compose(q, [9,10,11,12,13,14,15,16], inplace=True, front=True)

backend = Aer.get_backend('statevector_simulator')
job = backend.run(adder)


'''
fix ver:
backend = Aer.get_backend('statevector_simulator')
transpiled_adder = transpile(adder, backend)
job = backend.run(transpiled_adder)
'''
