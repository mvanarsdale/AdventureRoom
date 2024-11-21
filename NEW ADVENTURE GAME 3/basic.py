###########################################################################################
# Name: Mercedes VanArsdale 
# Description: A basic GUI Room Adventure game to show its mechanics and gameplay.
###################################################################################


###########################################################################################
# import libraries
from tkinter import *
from functools import partial
import pygame

###########################################################################################
# constants
VERBS = ["go", "look", "take", "give"]  # the supported vocabulary verbs
QUIT_COMMANDS = ["exit", "quit", "bye"]  # the supported quit commands


###########################################################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, image, description, exits (e.g., south), exit locations (e.g., to the
        # south is room n), items (e.g., table), item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []
        self.is_locked = False
        self.key_required = None

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)
    
    ####ADD ONS#####
    def enter(self):
        if self.is_locked:
            print("You can't enter this area yet.")
        else:
            print("You enter {}. {}".format(self.name, self.description))

    def unlock(self):
        print("Nice job! You made it through.")
        self.is_locked = False

    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table 
    #  Exits: east south 
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        return s


###########################################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # a list of rooms will store all of the rooms
        # r1 through r4 are the four rooms in the "mansion"
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        Game.rooms = []

        # first, create the room instances so that they can be referenced below
        r1 = Room("An unfamiliar world ", "room1.png")
        r2 = Room("A sufficating pathway", "room2.png")
        r2b = Room("Tall dark grass", "room2b.png") # still need to add this image
        r3 = Room("An uncomfortbale space", "room3.png")
        r4 = Room("A dimly lit pathway", "room4.png")
        r5 = Room("An axiety inducing space", "room5.png")
        r6 = Room("An_unsettling_room", "room6.png")
        r7 = Room("An illuminated pathway", "room7.png")
        r8 = Room("Main hall", "room8.png")
        r9 = Room("A quiet room", "room9.png")
        r9b = Room("You're stuck", "bad_ending.png")
        r10 = Room("A chaotic Room", "room10.png")
        r10b = Room("The vault", "room10b.png")
        r11 = Room("A brightly lit room", "room11.png")
        r11b = Room("Human World", "good_ending.png")

        # Room 1
        # Changed room descriptions and added items + grabbables 
        r1.description = "\nYou analyze your surroundings and see that you are in a small room where both the walls and floors are made of \nold, smelly wood.\n"
        r1.addExit("north_east", r2)
        r1.addItem("candle", "You see a small wooden table on it, rests a candle.\n\nIt is a long wick candle that appears to have been \nburning for some time. You hold the candle by its metal stand and remember the warm feeling it brings to your \nhand. \n\nYou close your eyes to savor the warm feeling when \nsuddenly you are teleported to another room.\n\nYou feel the strong urge to keep your eyes closed and \nattempt to analyze the room with your eyes shut.\n\nYou're sitting with your legs crossed on a hard floor \ncovered by a rug; the room feels frigid.\n\nAs you listen closer to the sounds around you, you \nnotice the sound of someone breathing right next to you.\n\n'Remember to keep your eyes closed.' The voice says.\n\nThe abrupt sound startles you, and against all warnings, \nyou reflexively open your eyes to find yourself \nback in the room you had woken up in.\n--------------")
        Game.rooms.append(r1)

        # Room 2
        r2.description = "\nYou're outside and surrounded by tall grass.\nUnderneath your feet lies a dirt path.\n"
        r2.addExit("south_west", r1)
        r2.addExit("north_east", r3)
        r2.addExit("south_east", r2b)
        r2.addItem("tall_grass", "You look closely into the grass and see something shiny,\nbut it's too far out to reach...\n\nMaybe if you got something to cut down the grass a bit you could reach it...\n-----------------")
        Game.rooms.append(r2)
        
        # Room 2b (the tall grass)
        r2b.description = "\nYou step into the tall grass.\n"
        r2b.is_locked = True
        r2b.key_required = "shears"
        r2b.addExit("north_west", r2)
        r2b.addItem("ground", "You look at the ground beneath your feet and realize \nthat the *key_of_light* is within reach!\n----------------")
        r2b.addGrabbable("key_of_light")
        Game.rooms.append(r2b)

        # Room 3
        r3.description = "\nThe room is similar in both exterior and interior to \nthe room you began in.\n"
        r3.addExit("north", r4)
        r3.addExit("south_west", r2)
        r3.addItem("rug", "You look down to get a closer look at the rug.\nIt looks familiar but appears to be overdue for a wash.\n---------------")
        r3.addItem("hairclip", "The large wooden table appears to have a pair of \nscissors and a hairclip resting on it.\n\nThe hairclip seems familiar, and as you look at it,\na flash of memory comes to mind.\n\nIn the memory, you appear next to a girl who's fairly \nsmaller than yourself.\n\nYou can't get a good look at her face but can clearly \nsee the butterfly-shaped hair clip that is holding \nher light brown hair back.\n\nYou can sense that the hairclip is special not only to \nthe girl but you as well.\n----------------")
        Game.rooms.append(r3)

        # Room 4
        r4.description = "\nYou find yourself on a path outside that's surrounded \nby tall stocks of grass.\n"
        r4.addExit("north", r5)
        r4.addExit("south", r3)
        r4.addItem("crow", "You look up to see a crow perched up on a tall \nnearby tree.\n---------")
        r4.addItem("grass", "Large stocks of grass overwhelm you from all directions.\n----------------")
        Game.rooms.append(r4)
        
        # Room 5
        r5.description = "\nThis room appears to be the same as the first.\nThe only difference between the two being a \nstrong smell of tuna that fills the room.\n"
        r5.addExit("north", r6)
        r5.addExit("west", r7)
        r5.addExit("south", r4)
        r5.addGrabbable("shears")
        r5.addItem("shrine", "An empty shrine sits to the right of the room.\nOn it rests some *shears*...perfect for cutting grass.\n----------")
        Game.rooms.append(r5)
    
        # Room 6
        r6.description = "\nYou're not alone in the room you have just entered.\nThere is a mage and black cat accompying this space \nas well.\n"
        r6.addExit("south", r5)
        r6.addGrabbable("key_shaped_tag")
        r6.addItem("cat", "A black cat sits to the right of you wearing a \ncolar with a *key_shaped_tag*.\n\nFor a moment, you wonder if the cat belongs to the mage but you remember it belongs to her, the girl with the \nbutterfly-shaped hairclip.\n\nYou can recall several memories of the girl calling out for the missing kitty.\n\nIt's as if her voice is in the same room as you as she \ncalls out for her cat, Ame.\n-----------")
        r6.addItem("mage", "The mage that sits in front of you appears to be \nholding a note.\n\nHer face is covered along with the rest of her body \nwith a plum-colored cloak.\n\nYou can see her long dark hair spilling out the sides \nof the hooded cloth.\n\nShe doesn't appear to be willing to communicate.\n---------") 
        Game.rooms.append(r6)
        
        # Room 7
        r7.description = "\nYou step outside and are surrounded by tall stocks \nof grass.To the west of you appears to be a large \ncastle made of stone.\n"
        r7.addExit("west", r8)
        r7.addExit("east", r5)
        r7.addItem("crumpled_note","You pick up a crumpled note and look at what it \nhas to say.\n\nYou take note to the snake that is carefully drawn in \nthe top right hand side of the paper.\n\nThe note reads: \n\n'If this world is to much, seek the red_door. There you will be able to leave this world without consequence.'\n--------")
        r7.addItem("moon", "Though your situation is less than ideal, the \nmoon continues to shine beautifully.\n-------------")
        r7.addItem("grass", "Large stocks of grass overwhelm you from all directions.\n------------")
        Game.rooms.append(r7)
    
        # Room 8
        r8.description = "\nYou enter a castle hallway with multiple exits \nsurrounding you from all different directions.\n\nThe interior of the hallway is similar to the \npreviously visited rooms; however, a strange sound \nemits from one of the doors.\n"
        r8.is_locked = True
        r8.key_required = "key_of_light"
        r8.addExit("north", r11)
        r8.addExit("east", r7)
        r8.addExit("south", r10)
        r8.addExit("west", r9)
        r8.addItem("skull", "You notice a skull sitting in the corner of the room.\nYou watch a spider crawl out of one of the eye sockets.\n--------------")
        r8.addItem("weeping_door", "You put your ear up to the door the \nsound is coming from.\n\nYou can hear a girl crying, and when you call out to \nher, the crying seems to come to a stop.\n------------")
        Game.rooms.append(r8)

        # Room 9
        r9.description = "\nThis room is different than the ones you had visited \nbefore.\n\nThe interior appears to be more up-to-date with \ngrey wallpaper encasing the walls and a modern wood \nfloor that lies underneath your feet.\n"
        r9.addExit("east", r8)
        r9.addExit("red_door", r9b)
        r9.addItem("wall", "A *polaroid_picture* is pinned onto one of the walls,\nand you decide to take a closer look.\n\nIt's a picture of you and the butterfly girl.\n-----------------")
        r9.addGrabbable("polaroid_picture")
        Game.rooms.append(r9)
        
        # Room9b
        r9b.description = "\nOh no! You walked through the red_door and are now \ntrapped here forever!\n"
        Game.rooms.append(r9b)
        
        # Room 10
    
        r10.description = "\nThe room is filled with stones all around, both its \nfloor and walls.\n\nPhotographs featuring the items you had previously \nseen are spread out across the floor.\n"
        r10.addItem("cat_photo", "You examine the photo of the Ame, this is her cat.\n\nYou can recall the day in which the two of you had \nsaved the cat.\n\nIt was a rainy afternoon and the two of you had heard a faint cry coming from a nearby ally.\n\nYou went to investigate the sound and found a \nblack kitten tangled up in some trash.\n\nYou removed the trash and the butterfly girl took \nthe small cat into her arms as the two of \nyou walked home.\n----------" )
        r10.addItem("hair_clip_photo", "You pick up a photo of the girl facing away from \nthe camera.\n\nThe butterfly_clip is visable in the photo and you \nremember the day you gave it to her.\n\nYou spent many hours crafting the clip to be perfect \nfor her.\n--------------" )
        r10.addItem("candle_photo", "It's a photo of the candle you had seen when you first \narrived in this world.\n\nThe candle is sitting in the middle of a room you had \nspent most of your time in.\n\nIt reminds you how you got here.\n\nSuddenly a rush of memories comes flooding back, and \nyou are reminded of why you are here.\n\nYou and your friend had decided to partake in a silly \nritual the two of you found online.\n\nYou remember that during your turn to participate,\nyou had been startled and accidentally opened your eyes,\nwhich led you to where you are now.\n----------")
        r10.addExit("north", r8)
        r10.addExit("south", r10b)
        Game.rooms.append(r10)
    
        # Room 10b (the vault)
        r10b.description = "\nYou step into a room that seems to be made of crystals.\nIn the middle of the room lays a photo_book\n"
        r10b.addItem("photo_book","You briefly pick up a large photo album, it's full of \npictures featuring you and the girl.\n\nA *heartwarming_photo* falls out of the book.\n-----------")
        r10b.addExit("north", r10)
        r10b.is_locked = True
        r10b.key_required = "key_shaped_tag"
        r10b.addGrabbable("heartwarming_photo")
        Game.rooms.append(r10b)

        # Room 11
        r11.description = "\nYou enter a room that seems to be brighter than all the spaces you have previously encountered.\nIn the center of the room is a girl who is on her knees sobbing into her hands.\n"
        r11.is_locked = True
        r11.key_required = "heartwarming_photo"
        r11.addItem("the_girl", "The girl looks up and lunges herself into your arms \nfrom off the floor.\n\nShe immediately wraps her arms around your neck \nfor a hug.\n\nShe reaches out for your hand ready to return back to \nyour original world.\n-----------")
        r11.addExit("back_home", r11b)
        Game.rooms.append(r11)
        
        # Room11b
        r11b.description = "\nYou saved both you and your friend from being stuck in \nthis strange world.\n"
        Game.rooms.append(r11b)

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []

        # sets up the GUI

    def setupGUI(self):
        # initialize pygame
        pygame.init()
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        
        # make the background black
        self.configure(bg="black")

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process() in the class
        # bind the tab key to the function complete() in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="black")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2, height=HEIGHT // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="black", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=TOP, fill=Y)
        text_frame.pack_propagate(False)
        
        
        # Creating a canvas for the bottom half to easily navigate between rooms
        canvas = Frame(self, width=WIDTH // 2, height=HEIGHT // 2, bg = "black")
        
        # Red_door exit
        Game.red_doorimage = PhotoImage(file="red_door.png")
        Game.red_door = Button(canvas, image=Game.red_doorimage, command=partial(self.runCommand, "go red_door"))
        Game.red_door.grid(row=1, column=0, sticky=SW)
        
        # go_home exit
        Game.back_homeimage = PhotoImage(file="back_home.png")
        Game.back_home = Button(canvas, image=Game.back_homeimage, command=partial(self.runCommand, "go back_home"))
        Game.back_home.grid(row=1, column=4, sticky=NE)
        
        # image of compass 
        Game.pix_compassimage = PhotoImage(file="pix_compass.png")
        Game.pix_compass = Label(canvas, image=Game.pix_compassimage)
        Game.pix_compass.grid(row = 1, column = 2)
        
        # East Arrow
        Game.eastimage = PhotoImage(file="east.png")
        Game.east = Button(canvas, image=Game.eastimage, command=partial(self.runCommand, "go east"))
        Game.east.grid(row=1, column=3, sticky=E)

        # West Arrow
        Game.westimage = PhotoImage(file="west.png")
        Game.west = Button(canvas, image=Game.westimage, command=partial(self.runCommand, "go west"))
        Game.west.grid(row=1, column=1, sticky=W)

        # North Arrow
        Game.northimage = PhotoImage(file="north.png")
        Game.north = Button(canvas, image=Game.northimage, command=partial(self.runCommand, "go north"))
        Game.north.grid(row=0, column=2, sticky=S)

        # South Arrow
        Game.southimage = PhotoImage(file="south.png")
        Game.south = Button(canvas, image=Game.southimage, command=partial(self.runCommand, "go south"))
        Game.south.grid(row=2, column=2, sticky=N)

        # North_East ast Arrow
        Game.north_eastimage = PhotoImage(file="north_east.png")
        Game.north_east = Button(canvas, image=Game.north_eastimage, command=partial(self.runCommand, "go north_east"))
        Game.north_east.grid(row=0, column=3, sticky=S)

        # South_east Arrow
        Game.south_eastimage = PhotoImage(file="south_east.png")
        Game.south_east = Button(canvas, image=Game.south_eastimage, command=partial(self.runCommand, "go south_east"))
        Game.south_east.grid(row=2, column=3, sticky=N)

        # South_West Arrow
        Game.south_westimage = PhotoImage(file="south_west.png")
        Game.south_west = Button(canvas, image=Game.south_westimage, command=partial(self.runCommand, "go south_west"))
        Game.south_west.grid(row=2, column=1, sticky=N)
        
        # North_West Arrow
        Game.north_westimage = PhotoImage(file= "north_west.png")
        Game.north_west = Button(canvas, image=Game.north_westimage, command=partial(self.runCommand, "go north_west"))
        Game.north_west.grid(row=0, column=1, sticky=S)
        
        canvas.pack(side=TOP, fill=Y)
        canvas.pack_propagate(False)

    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom.name == "red_door"):
            # if dead, set the skull image
            Game.img = PhotoImage(file="bad_ending.png")
        elif (Game.currentRoom == None):
            # The good ending image
            Game.img = PhotoImage(file="good_ending.png")
        else:
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "Nice! You saved your friend and returned home!\n")
        elif (Game.currentRoom == "red_door"):
#             pygame.mixer.music.load("bad_ending.mp3")
#             pygame.mixer.music.play(1)
            # dead
            Game.text.insert(END, "Oh no! You walked through the red_door and are now \n trapped here forever!")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
        Game.text.config(state=DISABLED)

        # support for tab completion
        # add the words to support
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables

    # play the game
    def play(self):
        # create the room instances
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus("Welcome To: Don't Look Behind You!")

    # processes the player's input
    def process(self, event, action=""):
        self.runCommand()
        Game.player_input.delete(0, END)

    def runCommand(self, action=""):
        if not action.startswith("go"):
#             pygame.init()
#             pygame.mixer.music.load("treasure.mp3")
#             pygame.mixer.music.play(1)
            # grab the player's input from the input at the bottom of the GUI
            action = Game.player_input.get()
            # set the user's input to lowercase to make it easier to compare the verb and noun to known values
            action = action.lower().strip()
          

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)
        
        
        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None) or (Game.currentRoom.name == "red_door"):
            # clear the player's input
            Game.player_input.delete(0, END)
            return


        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()

            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # plays sound when player moves
                    pygame.mixer.music.load("click.mp3")
                    pygame.mixer.music.play(1)
                    # set a default response
                    response = "You can't go in that direction."
                    # check if the noun is a valid exit
                    if (noun in Game.currentRoom.exits):
                        # get its index
                        i = Game.currentRoom.exits.index(noun)
                        item = Game.currentRoom.exitLocations[i].key_required
                
                        ### Added on ###
                        #Puts locks on certain doors throughout the map#
                        if Game.currentRoom.exitLocations[i].is_locked and Game.currentRoom.exitLocations[i].key_required:
                            # Check if the player has the required key
                            if Game.currentRoom.exitLocations[i].key_required in Game.inventory:
                                Game.currentRoom = Game.currentRoom.exitLocations[i]
                                # response to player if the player has the key
                                response = "Nice! You've unlocked this area."
                                # drop the item after used 
                                #Game.inventory.remove(item)
                            else:
                                # response to player if they don't have the key 
                                response = "You can't enter this area yet.\nYou need {} to progress.".format(Game.currentRoom.exitLocations[i].key_required)
                                # when room is locked play an erorr sound 
                                pygame.mixer.music.load("error.mp3")
                                pygame.mixer.music.play(1)
                        else:
                            # Continue if the room is not locked 
                            Game.currentRoom = Game.currentRoom.exitLocations[i]
                            # Response to room if it's not locked  
                            response = "You continue through the walkway."   
                # the verb is: look
                elif (verb == "look"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid item
                    if (noun in Game.currentRoom.items):
                        # get its index
                        i = Game.currentRoom.items.index(noun)
                        # set the response to the item's description
                        response = Game.currentRoom.itemDescriptions[i]
                        # checks for right room
                        if Game.currentRoom.name == "An_unsettling_room":
                        # checks for right noun
                            if noun == "cat":
                                # plays a meow noise when player looks at cat
                                pygame.mixer.music.load("cat_meow.mp3")
                                pygame.mixer.music.play(1)
                        # checks for right room
                        if Game.currentRoom.name == "A dimly lit pathway":
                        # checks for right noun
                            if noun == "crow":
                                # plays crow sound when player looks at crow
                                pygame.mixer.music.load("crow.mp3")
                                pygame.mixer.music.play(1)
                        # checks for right room
                        if Game.currentRoom.name == "An illuminated pathway":
                        # checks for right noun
                            if noun == "crumpled_note":
                                # plays a crumpling paper sound when player looks at note
                                pygame.mixer.music.load("walkway_note.mp3")
                                pygame.mixer.music.play(1)
                        # checks for right room
                        if Game.currentRoom.name == "Main hall":
                        # checks for right noun 
                            if noun == "weeping_door":
                                # plays crying sound when investigating weeping door
                                pygame.mixer.music.load("weeping_door.mp3")
                                pygame.mixer.music.play(1)
                                                                                                                  
                # the verb is: take
                elif (verb == "take"):
                    # plays sound if player adds something to their inventory
                    pygame.mixer.music.load("item.mp3")
                    pygame.mixer.music.play(1)
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid grabbable and is also not already in inventory
                    if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                        # get its index
                        i = Game.currentRoom.grabbables.index(noun)
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(Game.currentRoom.grabbables[i])
                        # set the response (success)
                        response = "You take {}.".format(noun)
                # the verb is: give 
                elif (verb == "give"):
                    # checks to see if player is in correct room
                    if Game.currentRoom.name == "An_unsettling_room":
                        # checks to see if player is giving the right item
                        if noun == "polaroid_picture":
                            # checks to see if the correct item is in the players inventory 
                            if "polaroid_picture" in Game.inventory:
                                # the mage gives the player a note that reveals the name of "butterfly girl"
                                # easter egg ('o')
                                response = "You give the mage the polaroid_picture.\n\nThe mage hands you back a note.\n\nIt reads:\n\n'Save Lumi'\n---------"
                                # plays a crumple paper sound 
                                pygame.mixer.music.load("mage_note.mp3")
                                pygame.mixer.music.play(1)
                
                                Game.inventory.append("note")
                                Game.inventory.remove("polaroid_picture")
                        
                            else:
                                response = "You don't have what she is looking for"
                        else:
                            response = "She doesn't want that." 
                    else:
                        response = "There's no one here who wants that."

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()

    # implements tab completion in the Entry widget
    def complete(self, event):
        # get user input and the last word of input
        words = Game.player_input.get().split()
        # continue only if there are words in the user's input
        if (len(words)):
            last_word = words[-1]
            # check if the last word of input is part of a valid verb/noun
            results = [x for x in Game.words if x.startswith(last_word)]

            # initially, there is no matching verb/noun
            match = None

            # is there only a single valid verb/noun?
            if (len(results) == 1):
                # the result is a match
                match = results[0]
            # are there multiple valid verbs/nouns?
            elif (len(results) > 1):
                # find the longest starting substring of all verbs/nouns
                for i in range(1, len(min(results, key=len)) + 1):
                    # get the current substring
                    match = results[0][:i]
                    # find all matches
                    matches = [x for x in results if x.startswith(match)]
                    # if there are less matches than verbs/nouns
                    if (len(matches) != len(results)):
                        # go back to the previous substring
                        match = match[:-1]
                        # stop checking
                        break
            # if a match exists, replace the user's input
            if (match):
                # clear user input
                Game.player_input.delete(0, END)
                # add all but the last (matched) verb/noun
                for word in words[:-1]:
                    Game.player_input.insert(END, "{} ".format(word))
                # add the match
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

        # prevents the tab key from highlighting the text in the Entry widget
        return "break"


###########################################################################################
# START THE GAME!!!
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Don't Look Behind You")


# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()

# all audio provided by pixabay

