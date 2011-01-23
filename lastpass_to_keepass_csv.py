

# LastPass CSV mapping -- 
#   0 - url,
#   1 - username,
#   2 - password,
#   3 - extra,
#   4 - name,
#   5 - grouping,
#   6 - fav
# KeePass  CSV mapping -- 
#   0 - Account,
#   1 - Login Name,
#   2 - Password,
#   3 - Web Site,
#   4 - Comments

print """
  This Python script converts passwords from LastPass for importing into KeePass version 1.x
  The KeePass password database can be used as an encrypted, offline backup of the LastPass passwords.

  Use LastPass to export to a CSV file called 'lastpass.csv'.  Save the file in
  the same folder as this script.
  Use this script to convert the exported CSV file for use with KeePass
  Use KeePass to import 'lastpass_export.csv' as a CSV file
  """
fileIn = 'lastpass.csv'
fileOut = 'lastpass_export.csv'

fileRead = open(fileIn, 'r')
fileLines = fileRead.readlines()
fileRead.close()
print 'Read lastpass.csv\n'

fileOut = open(fileOut, 'w')
print 'Open lastpass_export.csv\n'

print 'Processing:\n'
for line in fileLines:
  line = line[:-1]                    #strip end of line character
  lpCols = line.split(',')            #split into columns
  if lpCols[0] == 'url':
    kpCols = []
    kpCols.append(u'Account')         # name to Account
    kpCols.append(u'Login Name')      # username to Login Name
    kpCols.append(u'Password')        # password to Password
    kpCols.append(u'Web Site')        # url to Web Site
    kpCols.append(u'Comments')        # extra to Comments
  else:
    kpCols = []
    kpCols.append(unicode(lpCols[4]).replace('"',''))  # name to Account -- convert to unicode and remove double quotes from LastPass CSV
    kpCols.append(unicode(lpCols[1]).replace('"',''))  # username to Login Name
    kpCols.append(unicode(lpCols[2]).replace('"',''))  # password to Password
    kpCols.append(unicode(lpCols[0]).replace('"',''))  # url to Web Site
    kpCols.append(unicode(lpCols[3]).replace('"',''))  # extra to Comments
  tmpStr = ''
  for column in kpCols:
    tmpStr = tmpStr + '"' + column + '",'
  print kpCols[0] + "...",
  fileOut.write(tmpStr[:-1] + '\n')

fileOut.close()
print '\n\nConversion to lastpass_export.csv complete.\n'
print 'Do not forget to remove the two CSV files used for the conversion after import into KeePass!'
print 'Leaving unprotected CSV files with all your passwords defeats using LastPass and KeePass.'
