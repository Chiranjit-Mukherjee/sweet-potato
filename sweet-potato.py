#!/usr/bin/env python
# This script find other domains on same ip address, based on the service of yougetsignal.com website.

import os
import sys
import requests, unicodedata, ast


def sweet_potato():
	os.system('clear')
	print "(*) Welcome To Reverse IP Lookup\n"
	site = raw_input("Enter the site: ")
	site = str(site)
	web = "http://domains.yougetsignal.com/domains.php?remoteAddress="
	url = web+site
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:47.0) Gecko/20100101 Firefox/47.0'}
	
	try:
		req = requests.post(url, headers)
	except:
		print("network unreachable...")
		#time.sleep(3)
		sys.exit(0)
		
	if req.status_code != 200:
		sys.exit(0)
		
	html = unicodedata.normalize('NFKD', req.text).encode('ascii','ignore')
	
	html_dict = ast.literal_eval(html)
	
	if html_dict['status'] == 'failure':
		print "[*] Error Occured."
		print html_dict['message']
		sys.exit(0)
		
	#print html_dict	
	serv_ip = ''
	
	if html_dict['status'] == 'Success':

		serv_ip = html_dict["remoteIpAddress"]	
		domains = html_dict["domainArray"]
		dom_count = html_dict["domainCount"]
	
		if not os.path.exists('data/'+serv_ip):
			os.makedirs('data/'+serv_ip)
	#------------------------------------------------------#
		print '*------------------------------------*'	
		print '(*) Status : Success'
		print '(*) Site Address : %s'%site
		print "(*) Server's IP : %s"%serv_ip
		print '(*) No of Domains : %s'%dom_count
		print '*------------------------------------*'
		print '[+] Domains on same server are :\n'
	#------------------------------------------------------#
		domsf = open('domains.txt','w')

		for i in domains:
			print i[0]
			domsf.write(i[0]+'\n')

		domsf.close()
		print "\n[*] All "+html_dict["domainCount"]+" domains are written to domains.txt file.  :)"
		
	#--------------------------------------------------------#



if __name__ == "__main__":
	sweet_potato()
