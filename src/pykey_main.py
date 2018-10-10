#!/usr/bin/env python3
import sys
import os
import subprocess
import grp, pwd
import getpass
 
#find the group that /dev/input events belong too
gid = os.stat('/dev/input/event0').st_gid
neededGroup = grp.getgrgid(gid)[0]
ready = ""
 
#find current user
user = getpass.getuser()
 
#list groups user belongs too
groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
gid = pwd.getpwnam(user).pw_gid
groups.append(grp.getgrgid(gid).gr_name)
 
#if user does not belong to the needed group warn user then exit program
if neededGroup not in groups:
    print("\n\nGroups user {} belongs too \n{}".format(user,groups))
   
    print("Your user is not in the {} group! Script will fail if you are not in this group!\nAdd {} to input group to continue. \n\nExiting...".format(neededGroup, user))
    exit()
 
#if there was an argument passed to script and that was -h show the help text
if len(sys.argv) > 1:
    if sys.argv[1] == "-h":
        print('''
        Usage:  ./pykey.py

\tThis program will remap key presses to execute commands or write 
\tblocks of text specified by you in the .pykey.conf config file 
       
\tFor this program to work you need to make sure the 
\tuser running it is a member of the GROUP owning the files in /dev/input 
\tCurrent mappable keys
  
       
\t'ESC', '1', '2', '3', '4', '5', '6', '7', '8',

    \t'9',  '0', '-', '=',  'BKSP',  'TAB',  'Q',  'W',  'E', 'R',

    \t'T',  'Y',  'U',  'I',  'O',  'P',  '[', ']',  'CRLF',  'LCTRL',

    \t'A',  'S',  'D',  'F',  'G',  'H',  'J',  'K',  'L',  ';',

    \t'"',  '`',  'LSHFT',  '\\',  'Z',  'X',  'C',  'V',  'B',  'N',

    \t'M', ',',  '.',  '/',  'RSHFT',  'LALT',  'RALT'
\tDepending on keyboard layout.

\tThe program will create a default .pykey.conf file populated with examples
    
\tof uses in the directory pykey.py is located
    
\tConfig should be laid out as follows CAPITALIZE key to be remapped followed 
\tby  periods until the the first 7 characters are filled if you want to write a block of text. If
    
\tyou want a command to be executed CAPITALIZE key to be remapped followed 
\tby periods until the first 6 characters are filled 7th char will be a C then immediatly 
followed by the python command.
    
\tThe end of text or command is terminated by two carrots ^^ 
\tformat should look as follows
\tA......will write this text when you press the a key^^
    
\tB.....Cprint("this just ran a command when you pressed the b key")^^

\tWhite space inside of text block is also preserved so if you write 
\tA......var i;
 
    \tfor (i=1; i<sumnum; i++) {
 
 
    \t}^^
    
\tthe block is written just the way you write it preserving the newlines inside''')
   
        exit()
   
else:
    #try to import modules if not installed ask if we can install them
    try:
        
        import autopy
        from evdev import InputDevice, categorize, ecodes
        
    except:
 
 
        carryon = input("We can't see that you have the required modules installed.\nCan we install the following.. keyboard, autopy, evdev? Continue(y/n)")
        if carryon != "y":
           exit()
        neededPacakages = ["keyboard", "autopy", "evdev"]
        def install (package):
          subprocess.call([sys.executable, "-m", "pip", "install", package])
        for i in neededPacakages:
            install(i)
 
    
    import autopy
    from evdev import InputDevice, categorize, ecodes
   
    #try to open conf file if does not exist create file with example data
    fn = ".pykey.conf"
    try:
        file = open(fn, 'r')
        file.close()
    except IOError:
        file = open(fn, 'w')
        file.write('''A.....Cprint('hello')^^
B......this is b test^^
C......var i;
 
for (i=1; i<sumnum; i ++) {
 
 
}^^
D......this is a test^^
E.....Csubprocess.Popen(['/usr/bin/firefox'])^^
F......this is a test^^''')
        file.close()
 
    print("\n\n\n\n\n\n\n")
    print(ready)
    print("__________________________________________________________________")    
    print("\nChoose device from list below to remap.\n")
    choice = ""
 
    scancodes = {  # Scancode: ASCIICode
        0: None,
        1: u'ESC',
        2: u'1',
        3: u'2',
        4: u'3',
        5: u'4',
        6: u'5',
        7: u'6',
        8: u'7',
        9: u'8',
        10: u'9',
        11: u'0',
        12: u'-',
        13: u'=',
        14: u'BKSP',
        15: u'TAB',
        16: u'Q',
        17: u'W',
        18: u'E',
        19: u'R',
        20: u'T',
        21: u'Y',
        22: u'U',
        23: u'I',
        24: u'O',
        25: u'P',
        26: u'[',
        27: u']',
        28: u'CRLF',
        29: u'LCTRL',
        30: u'A',
        31: u'S',
        32: u'D',
        33: u'F',
        34: u'G',
        35: u'H',
        36: u'J',
        37: u'K',
        38: u'L',
        39: u';',
        40: u'"',
        41: u'`',
        42: u'LSHFT',
        43: u'\\',
        44: u'Z',
        45: u'X',
        46: u'C',
        47: u'V',
        48: u'B',
        49: u'N',
        50: u'M',
        51: u',',
        52: u'.',
        53: u'/',
        54: u'RSHFT',
        56: u'LALT',
        100: u'RALT',
        }

    #print input devices
    for i in os.listdir("/dev/input/by-id"):
        output = os.readlink("/dev/input/by-id/"+i)+"    ===="+i
        print(output[3:])
 
 
    while not choice.isdigit():
        choice=input("\n\nEnter the (Event NUMBER) of USB keyboard to reconfigure:   ")
 
    dev=InputDevice("/dev/input/event"+choice)
       
       
    print("/dev/input/event"+choice + " has been modified according to .pykey.conf\n\nPress any key to test:   ")
       
 
     
    def keycatch():   
 
        #isthere refers to scancode. example-- the scancode 30 is assigned to 'A' so it isthere
        isthere = False
       
        dev.grab()
        with open('.pykey.conf') as myFile:
                    text = myFile.read()
                       
                    result = text.split('^^')
 
                    result = [s.strip() for s in result]
                   
        #look at keys pressed on second keyboard and find which key it was
        for event in dev.read_loop():
           
            if event.type == ecodes.EV_KEY:
                c = categorize(event)
               
                #if event is a keydown event
                if c.keystate == c.key_down:
 
                    # Lookup or return UNKNOWN:XX
                    key_lookup = scancodes.get(c.scancode) or u'UNKNOWN:{}'.format(c.scancode)  
                   
                    #READ conf file and
                    #do something if a certain key is pressed
 
                   
                    for line in result:
                           
                            if line.startswith(key_lookup):
                               
                                if line[6] == 'C':
                                   
                                    exec(line[7:])
                                    isthere = True                                
                                else:
                                    autopy.key.type_string(line[7:])
                                    isthere = True
                           
 
                    if isthere != True:
                        print(key_lookup)
keycatch()
