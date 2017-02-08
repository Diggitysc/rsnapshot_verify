# rsnapshot_verify
A simple script to check rsnapshot data captures

To utilize put the following line in the rsnapshot user crontab:

python /<location of script>/rsnapshot_verify.py /<base folder to check>

Example: 
python /opt/rsnapshot_verify.py /backups/web_server

If you have a MAILTO set up rsnapshot will email if:
------------------------------------------------------
1) Daily.0 does not exist

2) The current backup has an old verify date

3) Folders are backed up but the contents are not
