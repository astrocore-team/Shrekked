import subprocess

def set_master_volume(self, widget):
    val = self.volume
    val = float(int(100))
    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()