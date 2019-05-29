class Participant(object):
    """class defining a participant and info associated with them"""
    def __init__(self, name, discriminator, idstr, usrnum, wishlisturl='', preferences='', partnerid=''):
        self.name = name                   #string containing name of user
        self.discriminator = discriminator #string containing discriminant of user
        self.idstr = idstr                 #string containing id of user
        self.usrnum = usrnum               #int value referencing the instance's location in usr_list
        self.wishlisturl = wishlisturl             #string for user's wishlisturl
        self.preferences = preferences     #string for user's gift preferences
        self.partnerid = partnerid         #string for id of partner
    
    def wishlisturl_is_set(self):
        """returns whether the user has set an wishlisturl"""
        if (self.wishlisturl == "None") or (self.wishlisturl == ""):
            return False
        else:
            return True
    
    def pref_is_set(self):
        """returns whether the user has set gift preferences"""
        if (self.preferences == "None") or (self.preferences == ""):
            return False
        else:
            return True
