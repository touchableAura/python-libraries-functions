import sys 

# sys.stderr = open('out-err.log', 'w')
# sys.stdout = open('out.log', 'w')

# sys.stdout.write("Print Out - STDOUT 1\n")
# sys.stderr.write("ERROR: fatal error - STDERR1\n")

# sys.stdout.write("Print Out - STDOUT 2\n")
# sys.stderr.write("ERROR: fatal error - STDERR 2\n")

# sys.stdout.write("Print Out - STDOUT 3\n")
# sys.stderr.write("ERROR: fatal error - STDERR3\n")





### demmo 2: argv ###

# if len(sys.argv) > 1:
#     uname = sys.argv[1]
# else:
#     uname = input('Enter Name: ')

# print('hello', uname)




### demo 3: .path ####

print("\nPath:", sys.path[0])
print("\nFull Path:", sys.path)
print("\nVersion:", sys.version)
print("\nVersion_Info:", sys.version_info)


