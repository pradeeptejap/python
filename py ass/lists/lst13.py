devices = {
    'keyboard': 'Input Device',
    'mouse': 'Input Device',
    'monitor': 'Output Device',
    'printer': 'Output Device',
}

device = input("Enter the device name to lookup: ")
if device in devices :
    usage = devices.get(device)
    print(f"{device} - {usage}")
else :
    print("doesn't have one")
