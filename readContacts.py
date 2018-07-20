import urllib.request as urllib2
import xml.etree.ElementTree as etree
access_token = "ya29.Glv1BY7Utanwh0iO6e4aG2k4gMRabcqdEPxnzGZ33yVmbsDhByFGPUQGGetQ2crwXImcNy2TZ_EXVj907fFZfZiz_RTIhGxcbrZXBZmE7bDkNatMHQBfan4GcLWh"

url = 'https://www.google.com/m8/feeds/contacts/default/full' + '?access_token=' + access_token
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
contacts = urllib2.urlopen(req).read()  
contacts_xml = etree.fromstring(contacts)

emails_list = []
contacts_list = []

for entry in contacts_xml.findall('{http://www.w3.org/2005/Atom}entry'):
    for address in entry.findall('{http://schemas.google.com/g/2005}email'):
        email = address.attrib.get('address')
        emails_list.append(email)
    for address in entry.findall('{http://schemas.google.com/g/2005}phoneNumber'):
        contacts_list.append(address.text)
print("emails list")
print(emails_list)
print("contacts list")
print(contacts_list)
