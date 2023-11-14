#create bell pair and initialize circuit

def create_bell(circuit):
    qc = circuit(2)
    qc.h(1)
    qc.cx(1,0)
    return qc