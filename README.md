# RemoteMonitor
Allows monitoring of a remote computer's hardware through a web interface


## Version 0.2.1
This application is not ready for use.

- Established connection between the clients and servers with v0.2.0
- Data is now stored in the user database as of v0.2.1


## Current Plans
(The following list is in no particular order)

- Automate client data collection
- Sanitize input before insertion into database


## Future Possibilities
(The following list is in no particular order)

- I am probably going to split RMUserDatabase into a RMDatabase class (removing the responsibility for user specific data and allowing any multitude of tables) and several *DataManager class, much like the current ClientDataManager
