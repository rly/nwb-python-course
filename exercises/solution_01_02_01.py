# Create a datetime object representing the current time
from datetime import datetime
from dateutil.tz import tzlocal
start_time = datetime.now(tzlocal())

# Import the NWBFile class
from pynwb import NWBFile

nwbfile = NWBFile(session_description='A description for this session',
                  identifier='Mouse10-Day1',
                  session_start_time=start_time)
print('Session ID:', nwbfile.identifier)
