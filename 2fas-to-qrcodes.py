import qrcode, json, urllib.parse
from pathlib import Path

twofas_file = ""
links_list = []

with open(twofas_file) as f:
    backup = json.load(f)

if backup["schemaVersion"] != 4:
    print("error: 2FAS backup schema version not 4")
    exit()

Path("./qrcodes/").mkdir(parents=True, exist_ok=True)

for service in backup["services"]:
    service_name = urllib.parse.quote_plus(service["name"], safe='')
    account = urllib.parse.quote_plus(service["otp"]["account"], safe='')
    secret = urllib.parse.quote_plus(service["secret"], safe='')
    issuer = urllib.parse.quote_plus(service["otp"]["issuer"], safe='')
    algorithm = urllib.parse.quote_plus(service["otp"]["algorithm"], safe='')
    digits = service["otp"]["digits"]
    period = service["otp"]["period"]

    link = f'otpauth://totp/{service_name}:{account}?secret={secret}&issuer={issuer}&algorithm={algorithm}&digits={digits}&period={period}'
    img = qrcode.make(link)
    filename = f'{service["name"]}:{service["otp"]["account"]}'
    img.save("./qrcodes/" + "".join(c for c in filename if c.isalnum()) + ".png")
    links_list.append(link)

with open("./links.txt", "w") as f:
    f.write("\n".join(links_list))