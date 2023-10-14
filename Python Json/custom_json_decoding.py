import json

def asComplex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

res = json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook = asComplex) 
print(res)
print(type(res))