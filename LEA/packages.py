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
		if self.manager == "pacman":
			self.install_cmd = "pacman -S"
			self.delete_cmd = "pacman -Rsn"
			self.update_cmd = "pacman -Syu"
			self.update_all_cmd = "pacman -Syu"

		#TODO: Add more package managers from other distros

	def install(self,name):
		return os.system(self.install_cmd + " " + name)

	def remove(self,name):
		return os.system(self.delete_cmd + " " + name)

	def update(self,name):
		return os.system(self.update_cmd + " " + name)

	def update_all(self):
		return os.sytem(self.update_all_cmd)

			




