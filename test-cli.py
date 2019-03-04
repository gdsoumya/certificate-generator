'''

A simple CLI script to run the certificate generator.

The "config.txt" file needs to be setup according to the needs.
Documentation for editing the config file can be found here https://github.com/gdsoumya/certificate-generator .

'''

from certificate_generator import Certificate
import argparse 
import sys

parser = argparse.ArgumentParser(description = "Dynamic Course/Event Certificate Generator. Use Quotes while specifying Name/Event/Date/Output with spaces inbetween.")

parser.add_argument("-n", "--name", type = str, nargs = 1, 
                        metavar = "recipient_name", default = None, 
                        help = "Name of the certificate recipient.",required=True)
parser.add_argument("-e", "--event", type = str, nargs = 1, 
                        metavar = "event_name", default = None, 
                        help = "Name of the Event/Course the certificate is being issued for.",required=True)
parser.add_argument("-d", "--date", type = str, nargs = 1, 
                        metavar = "date_of_issue", default = None, 
                        help = "Date of Issue of the Certificate.",required=True)
parser.add_argument("-o", "--output", type = str, nargs = 1, 
                        metavar = "output_file", default = None, 
                        help = "Name of Certificate Output File (Must be an Image).",required=True)

args = parser.parse_args()

print("\n** DATA TO BE USED **")
print("\n>> NAME : "+args.name[0])
print(">> EVENT : "+args.event[0])
print(">> DATE : "+args.date[0])
print(">> OUTPUT FILE : "+args.output[0])
x = input("\n!! Is the Information Correct [y/n] :")
if x=='y' or x=='Y':
	ct = Certificate(args.name[0],args.event[0],args.date[0],args.output[0])  
	ct.create()
else:
	print("\n!! TRY AGAIN !!\n")