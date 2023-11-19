#create bell pair and initialize circuit

def create_bell(circuit,qreg,creg):
    qc = circuit(qreg,creg)
    qc.h(1)
    qc.cx(1,0)
    return qc