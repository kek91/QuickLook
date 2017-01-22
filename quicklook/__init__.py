from subprocess import Popen
from fman import DirectoryPaneCommand, show_alert
import platform

class QuickLook(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			if platform.system() == "Windows":
				Popen('"seer" "%s"' % file_under_cursor, shell=True)
			elif platform.system() == "Linux":
				show_alert("Not implemented")
			elif platform.system() == "Darwin":
				Popen('qlmanage -p "%s"' % file_under_cursor, shell=True)
