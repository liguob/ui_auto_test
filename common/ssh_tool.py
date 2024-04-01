# encoding=utf-8
"""
============================
Author:何凯
Time:2021/12/23 11:22
============================
"""
import paramiko


class SshTool:
    """linux服务器处理类"""

    def __init__(self, hostname, username, password, port=22):
        self.sftp = None
        self.host = hostname
        self.user = username
        self.pwd = password
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 通过公共方式进行认证 (不需要在known_hosts 文件中存在)
        self.ssh.connect(hostname=self.host, username=self.user, password=self.pwd, port=port)  # 建立链接

    def sftp_client(self):
        trans = self.ssh.get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(trans)
        return self.sftp

    def exec_cmd(self, cmd):
        """执行linux命令
        @param cmd:
        @return: 返回标准输入，标准输出，标准错误
        """
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = {"stdin": stdin, "stdout": stdout, "stderr": stderr}
        return output

    def put_file(self, remote_path, local_path):
        """
        上传文件
        @param remote_path: 远端地址
        @param local_path: 本地地址
        """
        try:
            sftp = self.sftp_client()
            sftp.put(localpath=local_path, remotepath=remote_path)
        except IOError as e:
            raise e("文件路径应为绝对路径")

    def get_file(self, remote_path, local_path):
        """
       下载文件
       @param remote_path: 远端地址
       @param local_path: 本地地址
       """
        try:
            sftp = self.sftp_client()
            sftp.get(localpath=local_path, remotepath=remote_path)
        except IOError as e:
            raise e("文件路径应为绝对路径")

    def file_stat(self, filepath):
        """
        检查远程服务器文件状态
        :param filepath:文件绝对路径
        """
        trans = self.ssh.get_transport()
        sftp = paramiko.SFTPClient.from_transport(trans)
        return sftp.stat(filepath)

    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    sshtool = SshTool(hostname="192.168.0.120", username="root", password="dreamsoft")
    file_stat = sshtool.file_stat(filepath="/mnt/log.log.2021-09-16")
