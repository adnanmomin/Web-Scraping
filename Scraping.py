import urllib
from bs4 import BeautifulSoup

page = urllib.urlopen('http://www.naukri.com/c-plus-plus-html-javascript-ajax-jquery-jobs')

content = BeautifulSoup(page)
row = content.find_all('div', class_= 'row')
file_out = open('jobs.txt', 'w')

for data in row:
	try:
		desig = data.find_all('span', class_= 'desig')
		org = data.find_all('span', class_= 'org')
		exp = data.find_all('span', class_= 'exp')
		loc = data.find_all('span', itemprop= 'jobLocation')
		skill = data.find_all('span', class_= 'skill')
		salary = data.find_all('span', class_= 'salary')
		for d in desig:
			print "Designation:\t", d.string
			file_out.write("Designation:\t"+d.string+"\n")
		for o in org:
			print "Company:\t", o.string
			file_out.write("Company:\t\t"+o.string+"\n")
		for e in exp:
			print "Experience:\t", e.get_text()
			file_out.write("Experience:\t\t"+e.get_text()+"\n")
		for l in loc:
			print "Location:\t", l.string
			file_out.write("Location:\t\t"+l.string+"\n")
		for s in skill:
			print "Keyskills:\t", s.string
			file_out.write("Keyskills:\t\t"+s.string+"\n")
		for sa in salary:
			file_out.write("Salary:\t\t\t"+sa.get_text()+"\n\n")
			print "Salary:\t     ", sa.get_text(), "\n"
	except Exception as error:
		print "\nERROR Occured\n########################################################################################\n"
		print type(error),"\n"
		print error,"\n"
		print "########################################################################################\nProgram Terminated"
		break

file_out.close()
