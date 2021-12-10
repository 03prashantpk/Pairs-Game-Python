

from urllib.request import Request, urlopen

req = Request('https://flevar.in/PairGame/WhatsNew.txt', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req,timeout=10).read()

print(webpage)