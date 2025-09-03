Day 2 - Client Options (Upload, List, Download, Exit)
1. Uploading Files
⦁	The client takes a file path from the user.
⦁	It reads the file in binary mode and sends the data to the server.
⦁	The server saves the file for future use.
2. Listing Files
⦁	The client asks the server for all stored files.
⦁	The server responds with a list of available file names.
⦁	This helps the client know what is already stored.
3. Downloading Files
⦁	The client requests a specific file from the server.
⦁	The server reads the file and sends the data back.
⦁	The client writes it locally, making a copy available to the user.
4. Exiting
⦁	Ends the client program safely.
⦁	No connection is left open, and the process stops cleanly.
---
How This is Useful in Our Project
⦁	These four options form the core of a Dropbox-like system.
⦁	Upload allows users to send files to the server (like storing in the cloud).
⦁	List helps keep track of files already available on the server.
⦁	Download allows retrieving files anytime, simulating how Dropbox gives access across devices.
⦁	Exit ensures the client program runs smoothly without leaving processes hanging.
Together, these operations show the basic functionality of a cloud storage system. In later days, we can extend this with user accounts, multiple clients, and synchronization features.
