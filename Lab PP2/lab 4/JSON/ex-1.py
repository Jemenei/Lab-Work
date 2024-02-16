import json

data = json.loads(open('/Users/sulemmen/Desktop/Lab PP2/lab 4/JSON/sample_data.json').read())

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

for intf in data['imdata']:
    dn = intf['l1PhysIf']['attributes']['dn']
    desc = intf['l1PhysIf']['attributes']['descr']
    speed = intf['l1PhysIf']['attributes']['speed']
    mtu = intf['l1PhysIf']['attributes']['mtu']
    if not desc:
        desc = ' ' * 19
    if not speed:
        speed = 'inherit'
    if not mtu:
        mtu = 9150
    print(f"{dn}                                                 {desc}       {speed}     {mtu}")