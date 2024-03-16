import csv
def readFile(namefile):
    device = []
    with open(namefile,'r') as file:
     reader = csv.DictReader(file, delimiter='*')
     for device in reader:
        device.append({'Company': device['Company'], 'Product': device['Product'], 'TypeName': device['TypeName'], 'Inches': device['Inches'], 'Cpu': device['Cpu'], 'Ram': device['Ram'],'Memory': device['Memory'], 'Gpu': device['Gpu'], 'Price': device['Price']})
    return device


    






