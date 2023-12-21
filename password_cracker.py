import hashlib

def read_add(file_name, arr):
  #read password
  with open("file_name", "rb") as f:
            line = f.readline().strip()
            while line:
              arr.append(line)
              line = f.readline().strip()
              
def crack_sha1_hash(hash, use_salts = False):
  passwords_arr =[]
  read_add ("top-1000000.txt", passwords_arr)

  #putting a flag for salts
  if use_salts:
    top_salt_passwors ={}
    top_salt = []
    read_add ("top-salts.txt", top_salt)
    for bsalt in top_salt:
      for bpassword in passwords_arr:
        prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
        appended = hashlib.sha1(bpassword + bsalt).hexdigest()
        top_salt_passwors[prepended] = bpassword.decode('utf-8')
        top_salt_passwors[appended] = bpassword.decode('utf-8')

    if hash in top_salt_passwors:
      return top_salt_passwors[hash]

  password_dict = {}
  #using hashlib to crack password
  for p in passwords_arr:
    hash_line = hashlib.sha1(p).hexdigest()
    password_dict[hash_line] = p.decode('utf-8')

  if hash in password_dict:
   return password_dict[hash]
    

           


  return "PAASWORD NOT IN DATABASE"
  

    