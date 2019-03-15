import argparse
import sys
import re
import subprocess

def q1(log_file):
    print("Giving output for Question 1....")
    subprocess.call("bash /Users/swrastog/Desktop/log_parser/q1.sh" + ' ' + log_file, shell=True)
    # lineformat = re.compile(r"""([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(?:\/[0-9]{1,2})?.*?([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(?:\/[0-9]{1,2})?))""")
    # with open(log_file) as logfile:
    #     next(logfile)
    #     for l in logfile.readlines():
    #         data = re.search(lineformat, l)
    #         ipdict = {}
    #         for ip in data[2]:
    #             if ip in ipdict:
    #                 ipdict[ip]+=1
    #             else:
    #                 ipdict[ip] = 1
    #             newdict = sorted(ipdict, key=lambda x:ipdict[x], reverse=True)
    #         print(newdict)
    # logfile.close()

def q2(log_file):
    print("Giving output for Question 2....")
    subprocess.call("bash /Users/swrastog/Desktop/log_parser/q2.sh" + ' ' + log_file, shell=True)

def q3(log_file):
    print("Giving output for Question 3....")
    subprocess.call("bash /Users/swrastog/Desktop/log_parser/q3.sh" + ' ' + log_file, shell=True)

def q4(log_file):
    print("Giving output for Question 4....")
    subprocess.call("bash /Users/swrastog/Desktop/log_parser/q4.sh" + ' ' + log_file, shell=True)

def question(i):
    if i == 1:
        q1(log_file)
    elif i == 2:
        q2(log_file)
    elif i == 3:
        q3(log_file)
    elif i == 4:
        q4(log_file)
    else:
        print("Invalid question number")

# def _load(logfile):
#     with open(logfile,'r') as f:
#         content = f.readlines()
#         content.pop(0)
#     return content

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", help="question_number(value should be in [1-4])", type=int)
    parser.add_argument("-i", help="input_file")
    args = parser.parse_args()
    if len(sys.argv) != 5:
        print("\nUsage: python logParser.py -q <question_number> -i <log_file_path>\n")
    else:
        # Reading arguments
        ques_no = int(sys.argv[2])
        log_file = sys.argv[4]
        try:
            question(ques_no)
        except Exception as e: print(e)

