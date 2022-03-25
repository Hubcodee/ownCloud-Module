import subprocess as sp


class ManageUser:
    def __init__(self, admin_user, admin_password, cloud_ip):
        self.admin_user = admin_user
        self.admin_pass = admin_password
        self.ip = cloud_ip

    def add_user(self, user, password, group):
        api_str = f'curl -X POST http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users \
   -d userid="{user}" \
   -d password="{password}" \
   -d groups[]="{group}"'
        res = sp.getoutput(api_str)
        return res

    def delete_user(self, user):
        api_str = f"curl -X DELETE http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user}"
        res = sp.getoutput(api_str)
        return res

    def edit_users(self, key, data, user):
        if key == "email":
            api_str_email = f'curl -X PUT http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user} \
    -d key="email" \
    -d value="{data}"'
            res = sp.getoutput(api_str_email)
        else:
            api_str_quota = f'curl -X PUT http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user} \
    -d key="quota" \
    -d value="{data}"'
            res = sp.getoutput(api_str_quota)
        return res

    def get_user(self, user):
        api_str = f'curl http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user}'
        res = sp.getoutput(api_str)
        return res
