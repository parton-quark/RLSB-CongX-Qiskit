# # (c) Copyright 2004-2011 Oleg Golubitsky and Dmitri Maslov
# # Distributing this file without an express written permission or erasing this note is prohibited.
# .v a,b,c,d
# .i a,b,c,d
# .o a,b,c,d
# BEGIN
# t1 d
# t2 d,c
# t4 a,c,d,b
# t3 a,d,c
# t3 b,d,a
# t3 c,d,b
# t3 b,c,d
# t3 a,d,b
# t2 a,d
# t1 a
# t1 b
# t1 c
# t4 b,c,d,a
# t2 b,c
# t3 a,d,c
# END

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from CongX.extensions.standard import cnx
q =  QuantumRegister(4)
# c = ClassicalRegister(0)
qc = QuantumCircuit(q)
qc.x(3)
qc.cx(3,2)
qc.cnx(0,2,3,1)
qc.ccx(0,3,2) 
qc.ccx(1,3,0)
qc.ccx(2,3,1)
qc.ccx(1,2,3) 
qc.ccx(0,3,1)
qc.cx(0,3)
qc.x(0)
qc.x(1)
qc.x(2)
qc.cnx(1,2,3,0)
qc.cx(1,2)
qc.ccx(0,3,2)