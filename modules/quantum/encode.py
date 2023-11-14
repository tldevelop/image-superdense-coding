def quantum_encode(qc,qubit,msg):
    #verify if msg is valid
    if len(msg) != 2 or not set(msg).issubset({"0","1"}):
        raise ValueError(f"message '{msg}' is invalid")
    if msg[0] == "1":
        qc.z(qubit)
    if msg[1] == "1":
        qc.x(qubit)
    return qc