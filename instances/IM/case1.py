qr = QuantumRegister(3)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr,cr)
qc.reset(range(3))
qc.h(1)
qc.cx([1,0],[2,1])
qc.h(0)
qc.measure([0,1], [0,1])
qc.z(2).c_if(cr, 1)
qc.x(2).c_if(cr, 2)
qc.draw('mpl')


'''
fix ver:

qc.measure(0, 0)
qc.measure(1, 1)
qc.z(2).c_if(cr, 4)

'''
