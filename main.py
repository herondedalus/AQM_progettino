import pip
def install(package):
   pip.main(['install', package])
install('IBMQuantumExperience')
from IBMQuantumExperience import IBMQuantumExperience
#import Qconfig
#import pycuda
#import libMHCUDA
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import qiskit
import random
import time

api = IBMQuantumExperience("4b65ef27ae0a250c7749e78ec0f09718792090f417fc64e8764cad21d32e93b4c71bff4c8f4d2b06ae9c99a95292bfb7d7fb1b47b59f3cdcbb41bc52bc9f6e96", config = {"url": 'https://quantumexperience.ng.bluemix.net/api'}, verify=False)
print('')
#print(api.available_backends())

from qiskit import QuantumProgram, QISKitError, RegisterSizeError
start = time.clock()
qp = QuantumProgram()
qr = qp.create_quantum_register('qr',19)
cr = qp.create_classical_register('cr',19)
qc = qp.create_circuit('Test',[qr],[cr])
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])
qc.h(qr[7])
qc.h(qr[10])
qc.h(qr[18])
qc.cx(qr[0], qr[1])
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])
qc.measure(qr[2], cr[2])
qc.measure(qr[3], cr[3])
qc.measure(qr[4], cr[4])
qc.measure(qr[5], cr[5])
qc.measure(qr[6], cr[6])
qc.measure(qr[7], cr[7])
qc.measure(qr[8], cr[8])
qc.measure(qr[9], cr[9])
qc.measure(qr[10], cr[10])
qc.measure(qr[11], cr[11])
qc.measure(qr[12], cr[12])
qc.measure(qr[13], cr[13])
qc.measure(qr[14], cr[14])
qc.measure(qr[15], cr[15])
qc.measure(qr[16], cr[16])
qc.measure(qr[17], cr[17])
qc.measure(qr[18], cr[18])

result = qp.execute('Test')
print(result.get_counts('Test'))
print(time.clock() - start)