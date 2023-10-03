from pn7150 import PN7150

pn7150 = PN7150()

text = pn7150.read_once()
print(f"Read NFC Text: {text}")
