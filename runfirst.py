import os
import time
os.system("cd ./ipwndfu_public/; ./ipwndfu -p; python ./rmsigchks.py")
time.sleep(3)
os.system("pwd")
os.system("./irecovery -f ./firmware/ibss")
os.system("./irecovery -f ./firmware/ibec")
