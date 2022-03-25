import subprocess as sp


class ManageGroup:
    def __init__(self, admin_user, admin_password, cloud_ip):
        self.admin_user = admin_user
        self.admin_pass = admin_password
        self.ip = cloud_ip

    def get_groups(self, user):
        api_str = f'curl http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user}/groups'
        res = sp.getoutput(api_str)
        return res

    def add_to_group(self, group, user):
        api_str = f'curl -X POST http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user}/groups -d groupid="{group}"'
        res = sp.getoutput(api_str)
        return res

    def rem_group(self, user, group):
        api_str = f'curl -X DELETE http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/users/{user}/groups -d groupid="{group}"'
        res = sp.getoutput(api_str)
        return res

    def get_groups(self, user):
        api_str = f'curl http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/groups?search={user}'
        res = sp.getoutput(api_str)
        return res

    def add_group(self, group_name):
        api_str = f'curl -X POST http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/groups -d groupid="{group_name}"'
        res = sp.getoutput(api_str)
        return res

    def get_users(self, group):
        api_str = f'curl http://http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/groups/{group}'
        res = sp.getoutput(api_str)
        return res

    def delete_group(self, group):
        api_str = f'curl -X DELETE http://{self.admin_user}:{self.admin_pass}@{self.ip}/ocs/v1.php/cloud/groups/{group}'
        res = sp.getoutput(api_str)
        return res
