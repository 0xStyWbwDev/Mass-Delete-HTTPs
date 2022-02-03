#Powered By : Setyo Wibowo ID

banner = """ 

Mass Delete http atau https By Setyo Wibowo ID

"""

print banner

def http(url):

	try:		htt = (url)

		x = htt.replace('http://', '').replace('https://', '')

		open('done.txt','a').write(x+'\n'); print('Deleted http' + ' '+url)

	except: pass

site = raw_input('List Site : ')

ht = open(site, 'r').readlines()

for i in ht:

	try:

		siten = i.strip()

		data=http(siten)

	except: pass