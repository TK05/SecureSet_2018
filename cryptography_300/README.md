# Cryptography 300

![alt text](../images/cry300wc.jpg "Aggregated From Lesson Files")


### Topics
------

* Onion Routing
* Tor
* SSLStrip
* Cryptocurrencies
    * Decentralization, Mining, Security Problems
* RSA
* Segments of Memory
* Heartbeat (OpenSSL)
* Heartbleed (Exploit)
* Heartleech (Tool)
* AES and CBC Review
* Padding (PKCS #7)
* Padding Oracles
* POODLE
* RC4
* WEP
* FMS Attack


### Scripts
-----
* [currency_hash (Python)] - POC Cryptocurrency Miner
* [currency_hash_restricted (Python)] - POC Cryptocurrency Miner w/ Minimum Difficulty
* [pad_attack (Python)] - Padding Oracle Attack
* [wep_attack (Python)] - TODO

[currency_hash (Python)]: https://github.com/TK05/SecureSet_2018/tree/master/cryptography_300/currency_hash
[currency_hash_restricted (Python)]: https://github.com/TK05/SecureSet_2018/tree/master/cryptography_300/currency_hash_restricted
[pad_attack (Python)]: https://github.com/TK05/SecureSet_2018/tree/master/cryptography_300/padding_oracle
[wep_attack (Python)]: https://github.com/TK05/SecureSet_2018/tree/master/cryptography_300/wep_attack

### Assignments
------

* Successfully execute SSLStrip.
* Learn about the Bitcoin algorithm and how to adjust target difficulties.
* Use Heartleech to exploit the Heartbleed vulnerability on a vuilnerable server.
* Question a padding oracle to recover a plaintext message.
* Construct a FMS Attack to crack a key a listening server is holding.


### Tools
------

* Python
* SSLStrip
* dsniff
* arpspoof
* OpenSSL
* Heartleech                


### Command Line Things
------

* SSLStrip
* dsniff
* iptables
* /proc/sys/net/ipv4/ip_forward
* arpspoof
* openssl