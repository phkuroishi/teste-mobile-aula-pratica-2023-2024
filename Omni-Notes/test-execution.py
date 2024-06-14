import os
import sys
import time
import subprocess

print("Building project")
#os.system("./gradlew clean build")

n = int(sys.argv[1]) if len(sys.argv) > 0 else sys.exit(0)

if(n > 0):

	if(not os.path.exists('outputs/')):
		os.system('mkdir outputs')

	p = subprocess.Popen(["adb devices"], shell=True, stdout=subprocess.PIPE)
	stdout, stderr = p.communicate()

	value = True if 'emulator' in stdout.decode().split('\n')[1] else False

	if(value):
		for i in range(1):
			print("------ Executing Test Run #" + str(i) + "------")
			os.system('./gradlew cAT > outputs/file-' + str(i))
			time.sleep(2)

			os.system('adb uninstall it.feio.android.omninotes.alpha')
			os.system('adb uninstall it.feio.android.omninotes.alpha.test')

			time.sleep(2)