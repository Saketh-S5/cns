import itertools
import string
import time
def bruteforce(target_pass,max_lengh):
    stime=time.time()
    charset=string.ascii_letters+string.digits+string.punctuation
    for lengh in range(1,max_lengh+1):
        for attempt in itertools.product(charset,repeat=lengh):
            attempt_pass=''.join(attempt)
            print(f"trying password{attempt_pass}")
            if attempt_pass==target_pass:
                etime=time.time()
                print("password found")
                print(f"password:{attempt_pass}")
                print(f"time taken:{etime-stime:.2f}seconds")
                return attempt_pass
target_pass=input("enter password:")
max_lengh=8
bruteforce(target_pass,max_lengh)            
#https://www.linkedin.com/in/saketh-?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

