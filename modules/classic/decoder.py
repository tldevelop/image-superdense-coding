collection = []
clean = []

def getBits(file):
    #read file in binary
    with open(file,'rb') as f:
        #format into 0s and 1s
        for chunk in iter(lambda:f.read(1024), b''):
            collection.append((''.join(map('{:08b}'.format,chunk))))
    #clean array to make it a correct list
    for b  in collection[0]:
        clean.append(b)
    #create the list with pairs needed
    final = list(zip(clean,clean[1:]+clean[:1]))
    return final