def generate_hamming(data_bits, parity_type):
    n = len(data_bits)
    m = 0
    while (2 ** m) < (n + m + 1): 
     m += 1
    hamming = [None] * (n + m)
    j = 0

    # Place data bits in positions not power of 2
    for i in range(len(hamming)):
        if (i + 1) & i:
            hamming[i] = int(data_bits[j])
            j += 1

    # Calculate parity bits
    for i in range(m):
        parity_index = (2 ** i) - 1
        parity_sum = sum(hamming[k] for k in range(len(hamming)) if (k + 1) & (parity_index + 1) and hamming[k] is not None)
        hamming[parity_index] = 0 if parity_sum % 2 == (0 if parity_type == "even" else 1) else 1

    return ''.join(map(str, hamming))

def detect_and_correct(data, parity_type):
    hamming = list(map(int, data))
    n = len(hamming)
    m = 0
    while (2 ** m) < n: 
        m += 1
    error_pos = 0

    # Detect parity errors
    for i in range(m):
        parity_index = (2 ** i) - 1
        parity_sum = sum(hamming[k] for k in range(n) if (k + 1) & (parity_index + 1))
        if parity_sum % 2 != (0 if parity_type == "even" else 1):
            error_pos += 2 ** i

    # Correct error if any
    if error_pos:
        hamming[error_pos - 1] ^= 1

    return ''.join(map(str, hamming)), error_pos


# Example Usage
data_bits = input("Enter 4-bit or 5-bit data: ")
parity_type = input("Enter parity type (even/odd): ")
if parity_type in ["even", "odd"]:
    hamming_code = generate_hamming(data_bits, parity_type)
    print("Generated Hamming Code:", hamming_code)

    transmitted = input("Enter transmitted Hamming code: ")
    corrected_code, error_pos = detect_and_correct(transmitted, parity_type)
    if error_pos:
        print(f"Error detected and corrected at position: {error_pos}")
    else:
        print("No error detected.")
    print("Corrected Hamming Code:", corrected_code)
else:
    print("Invalid parity type. Use 'even' or 'odd'.")
print(f"corrected hamming code: {corrected_code}")