# RemoteMonitor
Allows monitoring of a remote computer's hardware through a web interface


## Version 0.2.1
This application is not ready for use.

- Established connection between the clients and servers with v0.2.0
- Data is now stored in the user database as of v0.2.1


## Current Plans
(The following list is in no particular order)

- Sanitize input before insertion into database


## Possible Future Changes
(The following list is in no particular order)

- Move the responsibility of timing update requests to the client (requires the server to accept API requests from the client; this would be in addition to the client accepting API requests from the server to allow manual submission of requests)
- I am probably going to split RMUserDatabase into a RMDatabase class (removing the responsibility for user specific data, and allowing any multitude of tables) and several *DataManager class, much like the current ClientDataManager