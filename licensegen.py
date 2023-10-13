import csv
import random
import string
import os

filecount = len([name for name in os.listdir('.') if os.path.isfile(name)])

def random_char():
    return random.choice(string.ascii_uppercase + string.digits)

def ranstring():
    return f"{random_char()}{random_char()}{random_char()}{random_char()}-{random_char()}{random_char()}{random_char()}{random_char()}-{random_char()}{random_char()}{random_char()}{random_char()}-{random_char()}{random_char()}{random_char()}{random_char()}"
keys = int(input("License key count\n > "))


# Make sure there's no duplicate entries
data = set()
while len(data) < keys:
    data.add(ranstring())

fname = f'licensekeys_{filecount}.csv'
with open(fname, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvfile.write(row + ',\n')

print(f"{keys} license key(s) has been generated and saved into {fname}")