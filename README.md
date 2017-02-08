# rsnapshot_verify
A script to check rsnapshot data backup folders 

To utilize rsnapshot_verify, put the following line in the rsnapshot user crontab:

python /<location of script>/rsnapshot_verify.py /<base folder to check>

Example: 
python /opt/rsnapshot_verify.py /backups/web_server

Rsnapshot will send an alert if:
------------------------------------------------------
1) Daily.0 does not exist

2) The most recent backup is stale (a day old)

3) Folders are backed up without any contents (empty sub-directory)
