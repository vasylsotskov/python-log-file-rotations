import os
import shutil
import sys

if len(sys.argv) < 4:
    print(f"{sys.argv[0]} Missing required positional arguments: \n"
          f"python script.py log.txt 5 4 \n"
          f"where 5 is size log file in kilobytes \n"
          f"and 4 it is history of log file")
    exit(1)

logFileName = sys.argv[1]
logSizeLimit = int(sys.argv[2])
numberLogFile = int(sys.argv[3])

if os.path.isfile(logFileName):
    logFileSize = os.stat(logFileName).st_size
    logFileSize = logFileSize // 1024

    if logFileSize >= logSizeLimit:
        if numberLogFile > 0:
            for currentFileNum in range(numberLogFile, 1, -1):
                src = logFileName + "_" + str(currentFileNum - 1)
                dst = logFileName + "_" + str(currentFileNum)
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print(f"Copied {src} to {dst}")

            shutil.copyfile(logFileName, logFileName + "_1")
            print(f"Copied {logFileName} to {logFileName}_1")
        doWrite = open(logFileName, "w")
        doWrite.close()
