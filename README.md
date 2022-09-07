# Splatnet-for-PC
## Description and Setup

Intro tips : create a new directory and put the main.exe file inside it because the app will download some images

Hello this project is a PC app (in .exe), the objective is to have a Nintendo Switch Online like application but only for Splatoon2.

To get started you juste have to download the main.exe file

-When launched, it will download tha maps images in the directory it's in

-Then, it will open 2 things:

	-a terminal window that contain the informations to follow for the setup
	
	-an internet window like this
	
![readme](https://user-images.githubusercontent.com/85625458/188690806-5cd576f5-58a2-4187-96db-c73529d05729.png)

	-Log in, right click the "Select this account" button, copy the link address, and paste it in the terminal window
	
	-Then the app will try to generate cookies and close, you just have to re-open it and normaly, it should run 
	
## Buttons

### Home

	-Shows the first gear in the splatnet application
	
	-Shows the recap from the last game you played
	
	-I'm also plannig to add something on the right side
	
### Stats

	-Select a number from 1 to 50 (1 being the last game you played and 50 the oldest)
	
	-Wait for the app to load the results (can take 10 to 20 seconds)
	
### Splatnet

	-Shows all the informations about the gears that are currently available in the app
	
### Widget

	-Create a little window that shows information such as you current power, your kda on the last game, 
	the amount of power you gained/loose (starting when the widget was created) and you can update it using the blue button.
	
![image](https://user-images.githubusercontent.com/85625458/188693810-f0cdd353-ecf8-43e2-b113-fe339e028b6b.png)
	
### maps

	-Shows the current and next rotation of the gamemode select (regular is turf war, gachi is ranked and league is league)
	
### resize

	-Update the window to scale the font size and some images
	
### refresh

	-Update the informations (it's pretty slow)
	
## Credits

The main credit goes to [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink), i use it to get the informations from the Switch online app 
(i modified some code in the splanet2statink file and commented the part that were not used in the app, including the part that upload the game info to 
[stat.ink](https://stat.ink/) 

WARNING : splatnet2statink is released under the GPL v3 license, which requires attribution: you must disclose the source of any code you're using as a 
basis, i.e. give credit, explicitly state any significant changes, and also release your project under the same terms.
	
If you want to make any modification on the code that is not from splatnet2statink, you can.

Else please reach out to the creators of splatnet2statink.

Here are the files that are from splatnet2statink : dbs.py , iksm.py , salmonrun.py , splatnet2statink.py
	
also used [customtkinter](https://github.com/TomSchimansky/CustomTkinter) to create the interface
	
## License used by splatnet2statink 

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
