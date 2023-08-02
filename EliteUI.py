class EliteUI:
    
    def __init__(self, maxopt=0):
        self.maxopt = maxopt
        if self.maxopt < 1:
            self.optnumb = 0
        else:
            self.optnumb = -1
        self.options = []
        for x in range(self.maxopt):
            self.options.append([x, "Value of option "+str(x)])
            continue
        return
        
    #catch error in try: except ValueError:
    def add_option(self, optID, optDesc):
        try:
            (self.options[optID])[1] = optDesc
            pass
        except ValueError:
            self.options.append([optID, optDesc])
            pass
        return self.options[optID]
    
    def DisPlaY(self):
        print("Please select from the following")
        #check if we loaded in options
        if self.optnumb < 0 and self.maxopt > 0:
            for x in range(self.maxopt):
                print(str((self.options[x])[0])+") \""+(self.options[x])[1]+"\"")
                continue
        #else will print options and get resp
        else:
            for x in range(self.optnumb): 
                print(str((self.options[x])[0])+") \""+(self.options[x])[1]+"\"")
                continue
            for x in range(self.maxopt):
                if x < self.optnumb:
                    continue
                print(str((self.options[x])[0])+") \""+(self.options[x])[1]+"\"")
                continue
        
        # read in argument 0 of 2d array self.options....
        # integer ID
        while True:
            id_str = raw_input('Enter your selection : ')
            id_int = int(id_str)
            for x in range(self.maxopt):
                if id_int == int((self.options[x])[0]):
                    return id_int
            print("Invalid selection!")
            continue
        return None
        
newGUI = EliteUI(3)
print("Got option + "+str(newGUI.DisPlaY()))