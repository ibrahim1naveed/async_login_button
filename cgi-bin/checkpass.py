#!/usr/bin/python
#import modules for CGI handling
import cgi, cgitb
import csv
print "Content-type:text/html\r\n\r\n"

# Create instance of FieldStorage 
form = cgi.FieldStorage()
form1 = form.value
#print "<h3>the form field is %s</h3>" % (form1)

list_of_both = form1.split("&")


# Get data from fields
username = list_of_both[0]
password  = list_of_both[1]

in_file = False
with open('../users.csv','rb') as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        if username in row and password in row:
            in_file = True


print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
#print "<h2> Your username is %s and password is %s</h2>" % (username,password)
if (in_file):
    print "<h2>Your Password Matches</h2>"
else:
    print"<h2>Wrong username or password</h2?"
print "</body>"
print "</html>"
