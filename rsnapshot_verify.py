import sys
import os
import datetime
from datetime import timedelta


def main():
    '''
        Description: rsnapshot_verify checks the creation date of daily.0 and
        if it is empty for a given folder path. An error is generated if the
        creation date is older than a day or if there are no folders outside of
        the "installed" folder

        rsnapshot will always grab an installed folder on execution
        resulting in a path directory size of 1. Path depth is used instead of
        file size due to the cost of determining raw file size and file size
        results can be deceptive (as folder objects are always 4096 bytes)

        Execution: python rsnapshot_verify.py /path/to/folder

    '''
    # grab input path, folder name  and create pointer for daily.0
    input_path = sys.argv[1]
    folder_path = "{0}{1}".format(input_path, '/daily.0')
    folder_name = input_path.split('/')[-1]

    # Get folder time stamp or toss error if daily.0 doesnt exist
    # daily.0 will always create if rsnapshot executes
    try:
        folder_timestamp = os.stat(folder_path).st_mtime
    except OSError:
        sys.exit("Rsnapshot ERROR daily.0 does not exist for {0}".format(
            folder_name))

    # cast write_date, set write window to -1 day
    # feel free to narrow down the time window based on estimate time of backup
    write_date = datetime.datetime.fromtimestamp(folder_timestamp)
    late_date_window = datetime.datetime.now() - timedelta(days=1)

    # print error listing last time daily.0 had a write
    # this indicates rsnapshot is offline or the backup target is offline
    print_date = str(write_date).split('.')[0]
    if (write_date < late_date_window):
        sys.exit(
            "Rsnapshot ERROR backup: {0} last written at {1}".format(
                folder_name, print_date))

    # check folder path depth
    walk_path = "{0}/{1}".format(folder_path, folder_name)
    if (len(os.listdir(walk_path)) <= 1):
        sys.exit(
            "Rsnapshot ERROR System folders not backed up {1}".format(
                folder_name, walk_path))

if __name__ == '__main__':
    main()
