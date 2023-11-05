def crack_rsa(n, e, ciphertext):

  for d in range(2**n.bit_length()):
    plaintext = pow(int.from_bytes(ciphertext, byteorder='big'), d, n)
    if plaintext == int.from_bytes(b"This is a secret message.", byteorder='big'):
      return plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='big').decode("utf-8")

  return None


if name == "main":
  n = 1234567890123456789012345678901234567890123456789012345678901234
  e = 1234567890123456789012345678901234567890123456789012345678901234

  ciphertext = b"This is a secret message."

  plaintext = crack_rsa(n, e, ciphertext)

  if plaintext is not None:
    print(plaintext)
  else:
    print("The RSA key was not cracked.")