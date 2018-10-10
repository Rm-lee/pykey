
This script will configure a second keyboards keys to either write a block of text on a keypress or execute a python command on key press. All keys actions are defined by you in .pykey.conf file created on first launch.


 Usage:  ./pykey_main.py or ./pykey_main.py -h for help text

	This program will remap key presses to execute commands or write 
	blocks of text specified by you in the .pykey.conf config file 
       
	For this program to work you need to make sure the 
	user running it is a member of the GROUP owning the files in /dev/input 
	Current mappable keys
  
       
	'ESC', '1', '2', '3', '4', '5', '6', '7', '8',

    	'9',  '0', '-', '=',  'BKSP',  'TAB',  'Q',  'W',  'E', 'R',

    	'T',  'Y',  'U',  'I',  'O',  'P',  '[', ']',  'CRLF',  'LCTRL',

    	'A',  'S',  'D',  'F',  'G',  'H',  'J',  'K',  'L',  ';',

    	'"',  '`',  'LSHFT',  '\',  'Z',  'X',  'C',  'V',  'B',  'N',

    	'M', ',',  '.',  '/',  'RSHFT',  'LALT',  'RALT'
	Depending on keyboard layout.

	The program will create a default .pykey.conf file populated with examples    
	of uses in the directory pykey.py is located.
    
	Config should be laid out as follows CAPITALIZE key to be remapped followed 
	by  periods until the the first 7 characters are filled if you want to write a block of text. If
    
	you want a command to be executed CAPITALIZE key to be remapped followed 
	by periods until the first 6 characters are filled 7th character will be a capital C, then immediatly then                   immediately followed by the python command to be executed.   
  
	The end of text or command is terminated by two carrots ^^ 
	format of .pykey.conf should look as follows
  
  
	A......will write this text when you press the a key^^    
	B.....Cprint("this just ran a command when you pressed the b key")^^ 
	
	Pressing the 'A' key will write text, Pressing the 'B' key will execute the print command.  
  

	White space inside of text block is also preserved so if you write 
	A......var i;
 
    	for (i=1; i<sumnum; i++) {
 
 
    	}^^
    
	the block is written just the way you write it preserving the newlines inside
  
  
  Features to come..
  
   -adding hotkeys as an action so a single key can be used to initiate keypress combinations..
    
![screenshot from 2018-10-10 14-58-23](https://user-images.githubusercontent.com/43976537/46759473-80f0da00-cc9d-11e8-94d9-5cc365ac651f.png)

The conf file

![screenshot from 2018-10-10 15-09-16](https://user-images.githubusercontent.com/43976537/46759926-8b5fa380-cc9e-11e8-99f3-f629b713b074.png)

