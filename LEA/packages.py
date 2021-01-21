import os
class PackageManager:
	def __init__(self,manager):
		self.manager = manager
		self.install_cmd = None
		self.delete_cmd = None

		if self.manager == "apt":
			self.install_cmd = "apt install"
			self.delete_cmd = "apt remove"
			self.update_cmd = "apt upgrade"
			self.update_all_cmd = "apt update && apt upgrade"
		if self.manager == "yum":
			self.install_cmd = "yum install -y"
			self.delete_cmd = "yum remove -y"
                


	def install(self,name):
		return os.system(self.install_cmd + " " + name)

	def remove(self,name):
		return os.system(self.delete_cmd + " " + name)

	def update(self,name):
		return os.system(self.update_cmd + " " + name)

	def update_all(self):
		return os.sytem(self.update_all_cmd)

			




