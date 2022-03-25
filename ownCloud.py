from ownCloudGroup import ManageGroup as MG
from ownCloudUser import ManageUser as MU

admin_usr = input("Enter Admin username: ")
admin_pass = input("Enter Admin pass")
ip = input("Cloud IP: ")

ch = -1
while(1):
    print("\t\t\t\tWelcome to ownCloud Management Console")
    print("#################################################")
    print("1.Manage Users\n2.Manage Groups\n0.Exit")
    print("#################################################")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        mu = MU(admin_usr, admin_pass, ip)
        print("1.Add user\n2.Delete user\n3.Edit user\n4.Get user")
        print("#################################################")
        usr_ch = int(input("Enter valid input: "))
        usr = input("Input username: ")
        if(usr_ch == 1):
            passw = input("Input pass: ")
            grp = input("Input grp: ")
            usr_res = mu.add_user(usr, passw, grp)
            print(usr_res)
        elif(usr_ch == 3):
            print("1.Update mail ?\n2.Update quota ?")
            key = int(input("Input 1 or 2: "))
            if key == 1:
                data = input("Input email: ")
                up_res = mu.edit_users(key, data, usr)
            else:
                data = input("Quota in format 1MB/1GB: ")
                up_res = mu.edit_users(key, data, usr)
            print(up_res)
        elif(usr_ch == 2):
            del_res = mu.delete_user(usr)
            print(del_res)
        else:
            get_res = mu.get_user(usr)
            print(get_res)
    elif ch == 0:
        exit(0)
    else:
        mg = MG(admin_usr, admin_pass, ip)
        res = ""
        print("1.List Groups\n2.Add User to Group\n3.Remove Group\n4.List Groups\n5.Create Group\n6.Get users from group\n7.Delete Group")
        print("#################################################")
        ch = int(input("Enter valid input: "))
        if ch == 1:
            usr = input("Enter username: ")
            res = mg.get_groups(usr)
        elif ch == 2:
            usr = input("Enter username: ")
            grp = input(f"Enter groupname for {usr}")
            res = mg.add_to_group(grp, usr)
        elif ch == 3:
            usr = input("Enter username: ")
            grp = input(f"Enter groupname for {usr}: ")
            res = mg.rem_group(usr, grp)
        elif ch == 4:
            usr = input("Input username: ")
            res = mg.get_groups(usr)
        elif ch == 5:
            grp_name = input("Input groupname: ")
            res = mg.add_group(grp_name)
        print(res)
