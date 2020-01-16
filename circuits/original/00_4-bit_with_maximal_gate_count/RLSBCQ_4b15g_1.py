# # (c) Copyright 2004-2011 Oleg Golubitsky and Dmitri Maslov
# # Distributing this file without an express written permission or erasing this note is prohibited.
# .v a,b,c,d
# .i a,b,c,d
# .o a,b,c,d
# BEGIN
# t2 a,c
# t2 c,d
# t2 d,a
# t3 b,d,c
# t2 a,b
# t3 c,d,b
# t4 a,b,c,d
# t2 c,a
# t1 b
# t1 c
# t2 a,d
# t3 b,d,c
# t3 b,c,a
# t3 a,c,b
# t1 c
# END

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from CongX.extensions.standard import cnx
q =  QuantumRegister(4)
# c = ClassicalRegister(0)
qc = QuantumCircuit(q)
qc.cx(0,2)
qc.cx(2,3)
qc.cx(3,0)
qc.ccx(1,3,2)
qc.cx(0,1)
qc.ccx(2,3,1)
qc.cnx(0,1,2,3)
qc.cx(2,0)
qc.x(1)
qc.x(2)
qc.cx(0,3)
qc.ccx(1,3,2)
qc.ccx(1,2,0)
qc.ccx(0,2,1)
qc.x(2)

qc.draw(output='mpl')