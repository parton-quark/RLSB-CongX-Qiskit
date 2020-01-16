# (c) Copyright 2004-2011 Oleg Golubitsky and Dmitri Maslov
# Distributing this file without an express written permission or erasing this note is prohibited.
.v a,b,c,d
.i a,b,c,d
.o a,b,c,d
BEGIN
t1 b
t2 b,a
t3 a,b,c
t3 a,d,b
t2 c,d
t4 b,c,d,a
t4 a,b,c,d
t2 a,c
t2 c,b
t3 b,d,c
t1 a
t1 b
t2 c,d
t2 d,a
t3 a,b,c
END