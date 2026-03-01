"""def bruteforce(pass_list,target_pass):
    for password in pass_list:
        print(f"trying password{password}")
        if password==target_pass:
            print(f"password found{password}")
            return True
    print("password not found")
    return False
if __name__=='__main__':
    pass_list=['123456','password','admin','password123']
    target_pass=input("enter password:")
    print("bruteforce started")
    success=bruteforce(pass_list,target_pass)
    if success:
        print("bruteforce successful")
    else:
        print("bruteforce failed")"""


def brtfrs(pass_lst,targt_pass):
    for password in pass_lst:
        print(f"trying pass{password}")
        if password==targt_pass:
            print(f"pass found{password}")
            return True 
    print("pass not found")
    return False
if __name__== '__main__':
    pass_lst=['12345','admin']
    targt_pass=input("enter pass")
    print("trying bruteforce")
    success=brtfrs(pass_lst,targt_pass)
    if success:
        print("successfull")
    else:
        print("unsuccessful")
