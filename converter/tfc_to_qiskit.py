def tfc_to_qiskit():
    text = 'from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister\
from CongX.extensions.standard import cnx'
    file = str(filename) + ".txt"
    fileobj = open(file, "w", encoding = "utf_8")
    fileobj.write(text)
    1,2行目はライセンスなので無視
    3行目読む→レジスタ準備
    qc = QuantumCircuit(q)
    4行目読む→　入力変数リスト
    5行目読む→　出力変数リスト(oとolに注意)
    6行目読む  if c感知→進む
             if BEGIN感知　→進む
    変換
        tof,freからcnx呼ぶ作業に入る....
        END感知でターンエンド(キリッ)
    fileobj.close()

def prepare_register(line_qubit):    
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
        
def input_qubits(line_qubit):    
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

def output_qubits(line_qubit):    
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

    
def gt_to_cnx():
    tの後の数字は疲労意味なし
    アルファベットを数字に変換

# t3 c,d,b
# t4 a,b,c,d
# t2 c,a
# t1 b
# t1 c
# t2 a,d
# t3 b,d,c