# RLSB-OpenQASM
Reversible Logic Synthesis Benchmarks in OpenQASM2.0

[Reversible Logic Synthesis Benchmarks Page](https://webhome.cs.uvic.ca/~dmaslov/) is a useful quantum programms for benchmarking reversible/quantum circuit optimization. The original contents are written in machine-readable format (.tfc file) and developed and maintained by Dmitri Maslov. 

This is a rewriting of Reversible Logic Synthesis Benchmarks in OpenQASM by [Shin Nishio](https://scholar.google.com/citations?user=gZNt8twAAAAJ&hl=ja)(a.k.a. parton). 

# How to use ?
1. git clone git@github.com:parton-quark/RLSB-OpenQASM.git
2. compile circuits by your compiler
3. **Post your Record to this page!**

# Contents
Quantum circuits and recording optimization results
## Contents from Original RLSB 
To be released after approval of the original author
## Additional Circuits 
Newly written circuit for RLSB-OpenQASM.

|Algorithm|circuits|image|Quantum Cost|Quantum Cost(Limited topology(2D,LNN))|record depth|record T|# of Qubit|
|---------|--------|-----|------------|--------------------------------------|------------|---------------|---|
|ex)Quantum Walk on complete graph|circuit|image|cost|cost|depth|T counts|qubits|

Quantum Cost is given as follows.
$C=C_s+C_c$$\times$ $10$ where $C_s$ is a number of Single-Qubit gates, and $C_c$ is a number of Two-Qubit Gates.

## Parameters to optimize
The hardware and system software (including quantum error correction) of the state-of-the-art quantum information processing system define the work that the quantum compiler should do and the method of evaluating its performance.

If you think there is more metric to add to this benchmark, please build an Issue.

# Contact and citation
Feel free to contact me via issues for this repository or send email to parton@sfc.wide.ad.jp .
Please cite as follows when you write a paper using this program.

**To Be Announced** in .bib format.

# See also
[CongX](https://github.com/parton-quark/CNX_compilation) is a controlled gate exansion set for Qiskit. Includes some generalized(biary controlled) Tofolli gate and compilers for them. Made by Shin Nishio.

[RevKit](http://www.revlib.org/)is an open source toolkit for reversible circuit design by Group of Computer Architecture
of the University of Bremen. 

[RevLib](http://www.revlib.org/)is an online resource for benchmarks within the domain of reversible and quantum circuit design by Group of Computer Architecture of the University of Bremen.