# Currency Hashing

### Instructions
* Write a Python script that will do the following:
    * Accept a transaction (in the form of a string) as an argument
    * Accept a target (in the form of an integer) as an argument
    * Pick a random starting nonce
    * Compute hashes until the hash is less than the given target
    * Return the hash

### Note
* Restricted script is used to limit target input to a minimum difficulty.
* Smaller Target = High Difficulty
* Try 10^75 as proof of concept