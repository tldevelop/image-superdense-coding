def quantum_decode(qc):
    qc.cx(1,0)
    qc.h(1)
    return qc