# (c) Copyright 2020 Shin Nishio, parton@sfc.wide.ad.jp 

def tfc_to_qiskit(tfc_path):
    tfc_file = open(tfc_path, "r", encoding = "utf_8")
    # convert tfc_file into list of lines 
    tfc_lines = tfc_file.readlines()
    # prepare .py file
    tfc_path_left = tfc_path.split('.')
    py_file_name = "RLSBCQ_" + str(tfc_path_left[0]) + ".py"
    py_file = open(py_file_name, "w", encoding = "utf_8")
    # py_file.write(text)で書き込める
    _write_head(py_file)
    
    tfc_line_number = 0
    for tfc_line in tfc_lines:
        tfc_line_number += 1
        if tfc_line.startswith('t'):
            _gt(py_file, tfc_line, valiables_dict)
        elif tfc_line.startswith('f'):
            _gf(py_file, tfc_line, valiables_dict)
        elif tfc_line.startswith('#'):
            _write_comment(py_file, tfc_line)
        elif tfc_line.startswith('.v'):
            # get list of valiables
            valiables_dict = _valiables(py_file, tfc_line)
            # make_register
            _prepare_register(py_file, valiables_dict)
        elif tfc_line.startswith('.i'):
            # get inputs
            input_dict = _inputs(py_file, tfc_line, valiables_dict)
        elif tfc_line.startswith('.o'):
            # get outputs
            output_dict = _outputs(py_file, tfc_line, valiables_dict)
        elif tfc_line.startswith('.ol'):
            # get outputs list
            ol_dict = _outputs_list(py_file, tfc_line, valiables_dict)
        elif tfc_line.startswith('.c'):
            # get constants
            constants_ = _constants(py_file, tfc_line, valiables_dict)
        elif tfc_line.startswith('BEGIN'):
            py_file.write('# BEGIN\n')
        elif tfc_line.startswith('END'):
            py_file.write('# END\n')
            py_file.close()
        else:
            print("The first letter of the" + tfc_line_number + "line of the input is strange.")
    #終わり
    tfc_file.close()
    return
    
def _write_head(py_file):
    lisences = _license_info()
    # import SDKs
    import_qiskit = 'from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister\n'
    import_CongX = 'from CongX.extensions.standard import cnx\n'
    # Comments from RLSB-CongX-Qiskit
    comments_from_RLSB_CongX_Qiskit = '# Can be run by installing Qiskit and CongX.\n' + '# !pip install qiskit\n' + '# !pip install CongX\n'
    py_file.write(lisences)
    py_file.write(import_qiskit)
    py_file.write(import_CongX)
    py_file.write(comments_from_RLSB_CongX_Qiskit)
    
def _license_info():
    original_lisence = '# LISENCE\n'
    congx_lisence = '# This file is converted by RLSB-CongX-Qiskit. RLSB-CongX-Qiskit is written by Shin Nishio. bib file is https://github.com/parton-quark/RLSB-CongX-Qiskit/blob/master/RLSB-CongX-Qiskit.bib \n'
    license_info = original_lisence + congx_lisence
    return license_info

def _prepare_register(py_file, valiables_dict):  
    num_qubits = len(valiables_dict)
    q = 'q =  QuantumRegister(' + str(num_qubits) + ')\n'
    # c = ClassicalRegister(0)
    qc = 'qc =  QuantumCircuit(q)\n'
    py_file.write(q)
    py_file.write(qc)
        
def _write_comment(py_file, tfc_line):
    # Write as it is
    py_file.write(tfc_line)


def _gt(py_file, tfc_line, valiables_dict):
    '''
    e.g. 
    input t3 b,c,d 
          {b:1, c:2, d:3}
    output qc.cnx(valiables_dict[b],valiables_dict[c],valiables_dict[d])
    '''
    # delete tn
    tfc_line = tfc_line.lstrip('t')
    # Delete the head number
    tfc_line = tfc_line.strip()
    tfc_line = tfc_line.strip(' ')
    operand_number = int(tfc_line[0])
    tfc_line = tfc_line[2:]
    # make valuable list
    val_list = tfc_line.split(',')
    operand_list = []
    for i in val_list:
        operand = valiables_dict[str(i)]
        operand_list.append(operand)
    operand_str = ', '.join(map(str, operand_list))
    cnx = "qc.cnx(" + operand_str + ")"
    py_file.write(cnx)
    py_file.write('\n')
    
def _gf(py_file, tfc_line, valiables_dict):
    message = 'Generalized Fredkin is under construction\n'
    return message
    
def _valiables(py_file, tfc_line):
    '''
    e.g. 
    input .v a,b,c,d
    output {'a':0, 'b':1, 'c':2, 'd':3}
    '''
    # delete str = '.v'
    tfc_line = tfc_line.lstrip('.v ')
    # remove whitespace
    tfc_line = tfc_line.strip()
    tfc_line = tfc_line.strip(' ')
    # make valuable list
    val_list = tfc_line.split(',')
    num_qubit = len(val_list)
    qubit_list = [i for i in range(num_qubit)]
    # make valuable_list and qubit_list to dict
    valiables_dict = dict(zip(val_list,qubit_list))
    py_file.write('# valuables' + str(valiables_dict) + '\n')
    return valiables_dict

def _inputs(py_file, tfc_line, valiables_dict):
    '''
    e.g. 
    input i. a,b,c,d
    output {'a':0, 'b':1, 'c':2, 'd':3}
    '''
    # delete str = '.v'
    tfc_line = tfc_line.lstrip('.i')
    # remove whitespace
    tfc_line = tfc_line.strip()
    # make valuable list
    input_list = tfc_line.split(',')
    qubit_list = []
    for i in input_list:
        qubit_number = valiables_dict[i]
        qubit_list.append(qubit_number)
    # make valuable_list and qubit_list to dict
    input_dict = dict(zip(input_list,qubit_list))
    py_file.write('# inputs' + str(input_dict) + '\n')
    return input_dict

def _outputs(py_file, tfc_line, valiables_dict):
    '''
    e.g. 
    input o. a,b,c,d
    output {'a':0, 'b':1, 'c':2, 'd':3}
    '''
    # delete str = '.v'
    tfc_line = tfc_line.lstrip('.o')
    # remove whitespace
    tfc_line = tfc_line.strip()
    # make valuable list
    output_list = tfc_line.split(',')
    qubit_list = []
    for i in output_list:
        qubit_number = valiables_dict[i]
        qubit_list.append(qubit_number)
    # make valuable_list and qubit_list to dict
    output_dict = dict(zip(output_list,qubit_list))
    py_file.write('# outputs' + str(output_dict) + '\n')
    return output_dict

def _outputs_list(py_file, tfc_line, valiables_dict):
    '''
    e.g. 
    input   .ol b1,b2,b3,b4,b5,b6,b7,b8,b9
    output {'a':0, 'b':1, 'c':2, 'd':3}
    '''
    # delete str = '.v'
    tfc_line = tfc_line.lstrip('.ol')
    # remove whitespace
    tfc_line = tfc_line.strip()
    # make valuable list
    ol_list = tfc_line.split(',')
    qubit_list = []
    for i in ol_list:
        qubit_number = valiables_dict[i]
        qubit_list.append(qubit_number)
    # make valuable_list and qubit_list to dict
    ol_dict = dict(zip(ol_list, qubit_list))
    py_file.write('#' + str(ol_dict) + '\n')
    return ol_dict

def _constants(py_file, tfc_line):
    '''
    e.g. 
    input   .c 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    output {'c0':0, 'c1':0, 'c2':2, 'c3':3....}
    '''
    # delete str = '.c'
    tfc_line = tfc_line.lstrip('.c')
    # remove whitespace
    tfc_line = tfc_line.strip()
    # make valuable list
    contstants = tfc_line.split(',')
    py_file.write('#' + str(contstants) + '\n')
    return contstants

