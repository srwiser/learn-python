## Encode a Key:Value pair using Base64

# Given a file with strings in key:value format
# Encode and write a new file where values are base64 encoded.

##########*************##################**************################

import base64
import argparse
import sys


def encodeBase64(s):
    return base64.b64encode(s.encode('ascii'))


def finalStr(k,v):
    return "{}: {}".format(k,v)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-dfile", help="decoded file path")
    parser.add_argument("-efile", help="endoded file path")
    args = parser.parse_args()
    if len(sys.argv) != 5:
        print("\nUsage: python encodebase64.py -dfile <decoded file path> -efile <encoded file path>\n")
    else:
        # Reading arguments
        dfile = sys.argv[2]
        efile = sys.argv[4]
        try:
            l = []
            data = {k: v for k, v in (l.split(':', 1) for l in open(dfile, 'r'))}
            for key in data:
                l.append(finalStr(key, encodeBase64(data[key])))
            with open(efile, 'w') as f:
                for item in l:
                    f.write("%s\n" % item)
        except Exception as e: print(e)