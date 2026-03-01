"""import hashlib
target_pass=input("enter pass:")
target_hash=hashlib.md5(target_pass.encode()).hexdigest()
pass_list=['admin','password','password123','123456']
def check_hash(target_hash,dictionary):
    for password in dictionary:
          hashed_pass=hashlib.md5(password.encode()).hexdigest()
          if hashed_pass==target_hash:
               print(f"password found:{password}")
               return password
    print("password not found")
    return None
check_hash(target_hash,pass_list)"""



import hashlib
target_pass=input("enter the password:")
target_hash=hashlib.md5(target_pass.encode()).hexdigest()
password_list=["123","abc","admin"]
def crack_hash(target_hash,dictionary):
    for password in dictionary:
        hashed_pass=hashlib.md5(password.encode()).hexdigest()
        if hashed_pass==target_hash:
            print(f"password found\n{password}")
            return password
    print("password not found")
    return None
crack_hash(target_hash,password_list)
