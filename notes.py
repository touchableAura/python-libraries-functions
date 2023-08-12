# additional string methods 
index() / Rindex() # retun value of index where it was found in string, Rindex return place for last instance in string
Join() # joins all values entered inside the parenthresi as a single string, quick way to create csv file
Strip() / Lstrip() / Rstrip() # removes white space from strings
Split() # separates string into a list, often set comma as optional separator
Count()

# Tuples are collections that are ordered and uneditable / unmutable
# Lists and sets store data
# dictionaries use key value pairs 

# on file handling
# open file 
file_var = open("name_of_text.txt", mode)
modes = { 'r' : 'read (default), open in read-only mode',
          'w' : 'write (clears the file first)',
          'a' : 'append mode, better for non-destructive editing',
          'r+/w+/a+' : 'read + write',
          'x' : "exclusive write - creates a file if it doesn't exist and error if it does",
          '+b' : 'binary mode (instead of text)'} 

.read()      # to read number of byte specified
.readline()  # reads in file one line at a time 
.readlines() # reads file to specified bite count and drops into a series of lists

.write()     # will add content to start of the file
             # every .write() file will add after the end of the existing content
.writeline() # will write all the content of the list in the file 

# in summary
data_types = [numbers, strings,], ['lists', 'sets', 'tuples', 'dict']
file_handinling = ['open', 'read', 'write', 'remove']
subprocess = []
encryption_and_hashing = []

# sys - needs to be imported
# https://docs.python.org/3/library/sys.html
# actions that let you interact with the interpreter 
.argv    #lets you access any cmd line args when starting the script
.path    # list of everything loaded into the path environment var of the
         # os. path0 is the current working directory 
.stderr  # alerts you when any part of the script has an issue / error so it can be addressed
.version # (Version_info)


# os - interact with operating system
.open 
.close    # interact with files on server 
.remove   # interact with files on server
.getcwd   # gets current working directory 
.getpid   # gets current process id
.system   # subprocess   # alllows you to run cmdline functions 


# regular expressions (regex)
# pattern recognition
# searching and manipulating strings 
# useful for indicator of compromise, log check
# regular expressions syntax
ordinary characters
metacharacters
special sequences 

r"the tool costs $3000"

\d\d*: will return ['3000']
\d\d?: will return ['30'.'00']
\d\d+: will return ['3000']   

# + requires 1 or more 
r'the tool costs $3'

\d\d* : will return ['3']
\d\d? : will return ['3']
\d\d+ : will return []

.compile()   # when you're using a pattern in multiple areas - write funtion once, assign vairbale
.search()    # looks for pattern anywhere in a string (but only first match)
.match()     # starts at the beginning of string and only returns the first match
.findall()   # returns all the matchs of the pattern


# PSUtil
.net_connections # gives you all open socket connections 
                 # stored as tuples
                 # includes local ports, remote ip, and pid for open sockets
.process         # returns info on the process that called it 
    .oneshot     # context manager that can put all details back in one call
.cpu_
.disk_
.virtual_memory_



# cryptography 

# useful links:
# https://cryptography.io/en/latest/
# https://pypi.org/project/cryptography/

# last thing you want to try and roll on your own

# fernet encryption is provided in the cryptography library 
# which guarentees content cannot be uncrypted without the key 

# fernet module uses fernet cl ss ( case sensitive )
.generate_key() # summetric encryption uses same key for encrypt/ decrypt
                # managing this key is very important 

. Fernet()      # the Fernet class, when assigned to a variable 
.encrypt        # using the generated key, can encrypt and decrypt a binary
.decrypt

# Scrypt comes from same cryptography library
# less complicated, but the scrypt class requires 
# additional parameters to develop the key
# because it was built to be attack resistant 

Scrypt(salt, length, n, r, p)
# salt is a random string added to the password to prevent hashed passwords 
# from matching up in the event that two users set the same password 
# lergth is the desired length of the key that is derived from the function 
# n is the CPU impact that slows the attack down (should be set to level of 2)
# r controls the block size (reccomended to be set at 8)
# p controls the parallelization (reccomended to be set at 1)


Yara 
# https://pypi.org/project/yara/
# https://yara.readthedocs.io/en/stable/yarapython.html
# designed to find patterns of malware to detect/ hunt 
Rule(rule name) # what do we call it once detected
{
    # add on data about the rule 
    meta: {
        created = ''
        modified = ''
        author = ''
        vendor = ''
    }
    # string and condition sections are the heart of the rule 
    # strings allows you to define any variable which
    # contain the pattern to be identified 
    # think about regular expressions:
    # you can have defined text, hex, 
    # or pull out the regular expression sequences and define the pattern
    strings: {
        $variable: ''
    }
    # condition holds expressions that returns a bolean response 
    # based on whether or not the expression has been met 
    and compare the files you want to check against the rules 
    condition: {
        (condition to be met to kick off rule)
    }
}

# before you can scan a file - you must first compile 
.compile
# the rules into a binary that can be pulled into a match function 
.match 

# these are used to detect


## sockets allow communications to flow between processes
# running different or same network on machines 
## TCP layer knows which application is listening for that data
# https://docs.python.org/3/library/socket.html
# used with communication back to dashboard and penetration tests

# Socket functions
.socket()  # creates new socket
.bind()    # runs on the server side and connects it 
            # to an IP and port on the server
.listen()  # you have a socket and a port assigned on a server
            # we can now listen for traffic on that binded port
.accept()  # once packets are received on the new socket
            # accept function formally accepts the connection
            # tells your code who the IP address talking to it on the other end is
.connect() # sits on the client siide 
            # tells the socket to make a TCP connection (can be UDP with alt config)
            # with the remote server vis host and port 
.send() / sendall ()  # the command to send a packet 
                      # send is limited in size
                      # sendall can handle larger packet sizes
                      # by breaking packet into chunks and using send cmd 
                      # over and over until everything has been sent
.recv()    # process packets as they come in
.close()   # close the socket once transmission complete

# Scapy is a packet manipulation library
# it can capture and read packets
# it can also can, test, and attack
# can be used for wireless testing and valid framing and injection attacks 
# primary use: network packets crafting / sniffing 
# needs to be pip installed 
conf()       # provides insight in the config of scapy
sr() / sr1() # part of send/receive module, sends packets at layer 3 
             # parameters allow yo to make changes on the fly
             # 1 in sr1 is bc only first response packet is returned
             # whereas with sr all response packets are returned 
send(IP/TCP/DNS) # you control the details of the packet 
.sniff()  # monitors packets that pass your various network interface 
.show()   # extends sniff() and allows you to look deeper at various packet details 

## Requests ##

# urls: https:/pypi.org/project/requests/

.get()   # retrieve information from a server
.post()  # send information to a server
.status_code()  # important to track any issues, 
                # check code is operating as expected
.text()    # access the response (usually in the form of source code)
           # returns the information in formatted Unicode
.content() # returns in bytes with all the new line chars, 
            # harder to read but easier for tools to work with
.header()  # reveals useful information 
# if not locked down, the header can expose what type of server your on
# along with the version 

# information leakage is one of the OWASP top 10 items 
# you'll want to look for with this tool
# requsts mimics all the functions your standard web browser handles for you

                
# Beautifulsoup4
# python library for retreiving elements
# from an HTML and XML documents using a parser
# this allows your to scrape and extract data from a file 
# or modify the file using python code
# then writing it back to a new HTML file with your modifications

# https://pypi.org/project/beautifulsoup4/

Beautifulsoup(web, parser) # can provide local html file
# Requests.get to pull in external
# by default bs4 works with the built-in Python standard HTML pareser
# lisf of parsers 
html.parser
lxml
lxml-XML    
htmltlib
# it's recommended that you use lxml for speed
# especially on older versions of python
# the built-in parser is not very good 
# lxml and html5lib are installed with pip separately 

# bs4 is a library of functions that are specialized for specific tasks
.find()     # returns the value found 
.find_all() # list containing all the results
.find_parent()
.find_next()
.find_previous()
# if serching for data leakage, 
# you could search for all comment braket patterns
# or in the header, is it disclosing server information?











