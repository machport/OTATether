import os
import time
print("The Script Will Be Stuck On Waiting For Device If Successful.")
print("Press Enter To Boot")
raw_input()
os.system("cd ipwndfu_public; ./ipwndfu -p; python ./rmsigchks.py")
os.system("./irecovery -f ./firmware/ibss")
os.system("./irecovery -f ./firmware/ibec")
time.sleep(3)
os.system("chmod +x ./fetchshsh.sh; ./fetchshsh.sh")
os.system("./futurerestore -t firmware/blobs.shsh -s firmware/sep -m firmware/buildmanifest.plist -b firmware/baseband.bbfw -p firmware/buildmanifest.plist firmware/firmware.ipsw")