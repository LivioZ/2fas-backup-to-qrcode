# 2FAS to QR Codes
This Python script generates QR Codes and a list of TOTP links of 2FA codes starting from an unencrypted 2FAS Authenticator App exported backup file.

# Usage
```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install qrcode
```

Open file `2fas-to-qrcodes.py` and change the variable `twofas_file` to the backup file location.

```
python 2fas-to-qrcodes.py
```
