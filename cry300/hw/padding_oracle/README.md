# Padding Oracle Attack

### Instructions
* There is a padding oracle living at 172.19.5.133, on port 5000.  The attached ciphertext was encrypted with the following command (key redacted):
    * openssl aes-128-cbc -in plain.txt -K ************** -iv 85D4856F1735F596B7266C93A4836C8C -out cipher.txt
* Note that the ciphertext is 48 bytes. 
* The original message was 32 bytes, but an entire 16-byte (128-bit) block was added as padding.
* Use the IV, ciphertext, and padding oracle to recover the entire 32-byte message.  
* For verification, the decrypted message is five random common English words.  

### Note
* Script is very specific to server response. Relies on a "Hello" response.