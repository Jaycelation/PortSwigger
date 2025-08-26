openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

tldr openssl

openssl rsa -in private_key.pem -pubout -out public_key.pem

echo '[+] Gen public/private key done!'