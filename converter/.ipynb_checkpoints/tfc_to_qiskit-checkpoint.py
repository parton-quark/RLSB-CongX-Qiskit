def tfc_to_qiskit(tfc_path):
    tfc_file = open(tfc_path, "r", encoding = "utf_8")
    # convert tfc_file into list of lines 
    tfc_lines = tfc.readlines()
    # prepare .py file
    py_file_name = "RLSBQC" + str(tfc_path) + ".py"
    py_file = open(py_file_name, "w", encoding = "utf_8")
    # py_file.write(text)で書き込める
    _write_head(py_file)
    
    tfc_line_number = 0
    for tfc_line in tfc_lines:
        tfc_line_number += 1
        if tfc_lines.startswith('t'):
            _gt(py_file, tfc_line, valiable_list)
        elif tfc_lines.startswith('f'):
            _gf(py_file, tfc_line, valiable_list)
        elif tfc_lines.startswith('#'):
            _write_comment(py_file, tfc_line)
        elif tfc_lines.startswith('.v'):
            # get list of valiables
            _valiables(py_file, tfc_line)
        elif tfc_lines.startswith('.i'):
            # get inputs
            _inputs(py_file, tfc_line)
        elif tfc_lines.startswith('.o'):
            # get outputs
            outputs
        elif tfc_lines.startswith('.ol'):
            # get outputs list
        elif tfc_lines.startswith('.c'):
            # get constants
        elif tfc_lines.startswith('BEGIN'):
            py_file.write('# BEGIN')
        elif tfc_lines.startswith('END'):
            py_file.write('# END')
            py_file.close()
        else:
            print("The first letter of the" + tfc_line_number + "line of the input is strange.")
    #終わり
    tfc_file.close()
    

    
def _write_head(py_file):
    lisences = _license_info()
    # import SDKs
    import_qiskit = 'from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister'
    import_CongX = 'from CongX.extensions.standard import cnx'
    # Comments from RLSB-CongX-Qiskit
    comments_from_RLSB_CongX_Qiskit = '""\n' + 'なんかコメントするよん qiskit, congxをインポートしてね!' + '"""'
    py_file.write(lisences)
    py_file.write(import_qiskit)
    py_file.write(import_CongX)
    py_file.write(comments_from_RLSB_CongX_Qiskit)
    
def _license_info:
    original_lisence = ''
    congx_lisence = 'This file is converted by RLSB-CongX-Qiskit. RLSB-CongX-Qiskit はpartonによって書かれたソフトウェアです。→bib fileのアドレス'
    # (c) Copyright 2020 Shin Nishio, parton@sfc.wide.ad.jp 入れるか考える
    
def _prepare_register(line_qubit):    
    line_qubit = line_qubit.replace(' ', '')
    line_qubit = line_qubit.replace('　', '')
#     line_qubit = line_qubit.replace('.', '')
    if line_qubit[0:2] == '.v':
        line_qubit = line_qubit.lstrip('.v')
        num_qubit = _count_num_qubits(line_qubit) + 1
        return num_qubit
    else:
        print('error, prepare_register() have some problem')
        print(line_qubit)
        
def _input_qubits(line_qubit):    
    line_qubit = line_qubit.replace(' ', '')
    line_qubit = line_qubit.replace('　', '')
#     line_qubit = line_qubit.replace('.', '')
    if line_qubit[0:2] == '.i':
        line_qubit = line_qubit.lstrip('.i')
        i_qubits = abcを数字のリストに直したやつ
        return num_qubits
    else:
        print('error, input_qubits() have some problem')
        print(line_qubit)

def _output_qubits(line_qubit):    
    line_qubit = line_qubit.replace(' ', '')
    line_qubit = line_qubit.replace('　', '')
#     line_qubit = line_qubit.replace('.', '')
    if line_qubit[0:2] == '.o':
        line_qubit = line_qubit.lstrip('.o')
        o_qubits = abcを数字のリストにしたやつ
        return o_qubits
    else:
        print('error, output_qubits() have some problem')
        print(line_qubit)
        
def _count_num_qubits(qubit_str):
    alphabets = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    if qubit_str[0] == 'a':
        num = alphabets[qubit_str[-1]]
        return num
    else: 
        print('error, count_num_qubits() have some problem')
        print(qubit_str)

    
def _write_comment(py_file):
    コメント来た時の対処
    コメントとして書き込む
    
    
