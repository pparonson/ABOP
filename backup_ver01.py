import os
import time

"""
1. The files and directories to be backed up are specified in a list.
	Example on Mac OS X:
"""
source = ["/users/pparonson/abop/notes"]
	# Note: Must us quotes inside the string for names with spaces

"""
2. The backup must be stored in a main backup directory
	Example on Mac OS X 
"""

target_dir = "/users/pparonson/abop/backup"

"""
3. The files are backed up into a zip file.

4. The name of the zip archive is the current date and time.
"""

target = target_dir + os.sep + \
time.strftime("%y%m%d%h%m%s") + '.zip'

"""
5. We use the zip command to put the files in a zip archive.
"""

zip_command = "zip -r {0} {1}" .format(target,''.join(source))

# Run the backup

print "Zip command is:"
print zip_command
print "Running:"

# Call .system method on imported os and pass var zip_command as parameter
if os.system(zip_command) == 0:
	print "Successful backup to", target
else:
	print "Backup Failed."