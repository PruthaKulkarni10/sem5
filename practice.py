def generate_hamming(data_bits, parity):
    n = len(data_bits)
    m = 0

    while (2**m ) < (m+n+1):
        m+=1

    hamming = [None] *(m+n)
    j = 0

    for i in range(len(hamming)):
        if (i+1) & i:
            hamming[i] = int(data_bits[j])
            j+=1

    for i in range(m):
        parity_index = (2**i) - 1
        parity_sum = sum(hamming[k] for k in range(len(hamming)) if (k+1) & (parity_index+1) and hamming[k] is not None)
        hamming[parity_index] = 0 if parity_sum % 2 == (0 if parity_type == 'even' else 1) else 1

    return ''.join(map(str, hamming))

def detect_and_correct(data, parity_type):
    hamming = list(map(int, data))
    n = len(hamming)
    m = 0

    while (2**m ) < (m+n+1):
        m+=1

    error_pos = 0
    for i in range(m):
        parity_index = (2**i) - 1
        parity_sum = sum(hamming[k] for k in range(n) if (k+1) & (parity_index+1))
        if parity_sum % 2 != (0 if parity_type == 'even' else 1):
            error_pos+= 2 ** i

    if error_pos:
        hamming[error_pos-1]^=1 

    return ''.join(map(str, hamming)), error_pos
    
data_bits = input("enter data")
parity_type = input("enter even or odd type of parity")

hamming = generate_hamming(data_bits, parity_type)
print(f"generated hamming code: {hamming}")

transmitted = input("enter transmitted msg")
corrected_code, error_pos = detect_and_correct(transmitted, parity_type)
if error_pos:
    print(f"error at pos: {error_pos}")
else:
    print("no error")