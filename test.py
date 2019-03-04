'''

Example to show how Certificate Generator can be integrated into existing projects.

The "config.txt" file needs to be setup according to the needs.
Documentation for editing the config file can be found here https://github.com/gdsoumya/certificate-generator .

'''

from certificate_generator import Certificate
ct = Certificate("John Doe","Green Earth Initiative","1st Jan, 2019","outputcertificate.png")
ct.create()