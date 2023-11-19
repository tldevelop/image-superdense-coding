def vector_simulator (qc,bkend,trsp,svec):
    tqc= trsp(qc,bkend)
    job = bkend.run(tqc)
    result = job.result()
    psi_qc = result.get_statevector(tqc,4)
    return svec(psi_qc)