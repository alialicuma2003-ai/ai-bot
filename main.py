import subprocess
import os

# ضيف التوكن تبعك هون
os.environ["BOT_TOKEN"] = "8058635927:AAHcCDJaTF_yspGQnMKZA1X2dMca1ixGSHw"

# اسم الملف تبعك
FILE_TO_RUN = "mytool.py"

if __name__ == "__main__":
    subprocess.run(["python", FILE_TO_RUN])
