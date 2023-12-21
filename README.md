# SHA-1-Passoword-cracker
SHA-1 password cracker python
Created a function that takes in a SHA-1 hash of a password and returns the password if it is one of the top 10,000 passwords used. If the SHA-1 hash is NOT of a password in the database, return "PASSWORD NOT IN DATABASE".
The function should take an optional second argument named use_salts. If set to true, each salt string from the file known-salts.txt should be appended AND prepended to each password from top-10000-passwords.txt before hashing and before comparing it to the hash passed into the function.
