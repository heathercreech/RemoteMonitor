# RemoteMonitor
Allows monitoring of a remote computer's hardware through a web interface


##Using RemoteMonitor

(Because this is a work in progress, you will be unable to do some of these steps)

1. Install all files from the client folder on the client computer and run "rmon_client.py"
2. Register at [insert url address]
3. Add your computer's IP to your account (note: ip registration is not currently implemented)
4. Return to the homepage and view your computer's stats


## Current Plans
(The following list is in no particular order)

- Sanitize input before insertion into database


## Future Possibilities
(The following list is in no particular order)

- I am probably going to split RMUserDatabase into a RMDatabase class (removing the responsibility for user specific data and allowing any multitude of tables) and several *DataManager class, much like the current ClientDataManager
