**Harpoon 2**

***Pre Alpha Release - Not Ready for Use***

**Description**
---------
This is a Django based rewrite of the Harpoon python-cli based application designed automatically send and/or monitor torrents and nzb files to a remote torrent/nzb client and monitor for completion and retrieve the completed files back to the local machine where automatic post-processing against specific clients can be initiated.

**Requirements**
----------
- LINUX only
- Python 3.8+
- Redis 5.0+
- pip
- pipenv
- rutorrent client (optional) (running remotely - ie.seedbox)
- sabnzbd client (optional) (running remotely - ie.seedbox)
- sonarr        (optional)
- radarr        (optional)
- lidarr        (optional)
- mylar         (optional)
- lazylibrarian (optional)
- sickrage      (optional)
- plex          (optional)

**Installation**
Install Python 3.8+, pip, pipenv and Redis 5.0+ (We used 5.0.7 in development, but your mileage may vary.)

Download Harpoon2:
`git clone https://github.com/DarkSir23/harpoon2`

Go to harpoon2 folder: `cd harpoon2`

Create pipenv environment:
`pipenv install`



