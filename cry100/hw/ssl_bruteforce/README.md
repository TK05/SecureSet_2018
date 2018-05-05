# SSL Bruteforce
###### results depend openssl version

### Instructions
* I encrypted a file with the following command (on Ubuntu 16.04):
    * $ openssl aes-256-cbc -in plain.txt -a
* And this was the output:
    * U2FsdGVkX18P/WqjJdbVKh89RLJ3IHfRriYFT2O2CbIrojlovWCJ82kkLw3R2DsM
* If you are cracking this on Kali Linux (I've found that OpenSSL derives the key and iv differently), use the following ciphertext:
    * U2FsdGVkX188Qqsioj21AU5tPpjkZGQJk6Lw9dVeu8fSVYEmyIyXR9X4JwRGLEuv
* When prompted for the aes-256-cbc encryption password, I entered three characters (selected from lower case letters, upper case letters, and digits).  
* Please use a brute-force attack to guess my password and tell me the password as well as the decrypted message.  