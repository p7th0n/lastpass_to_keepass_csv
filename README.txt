# LastPass to KeePass Export

This is a simple Python script to help export LastPass passwords for KeePass v1.xx.
LastPass has a feature to export to a CSV format.  The LastPass CSV format
cannot be imported by the KeePass CSV import feature.

This script arranges the fields in the order that KeePass expects and adds double 
quotes around each field.

The script came from several requests for a secure way to store LastPass passwords
offline.  Personally I use KeePass and KeePassX on Windows and OSX.  KeePass v2 
hasn't been a good option because of its dependency on .Net and Mono.

LastPass has a lot of good features but there is always a concern for keeping
valuable data only in the cloud.  The workflow is easier to manage secure behavior
online.  Like backups if the process can be made easier it is more likely to be 
done right.

To Do:
  * Make the script more intuitive to use
  * Cleanup the CSV files with the passwords when the process is done.
