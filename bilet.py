import pdfplumber
import os
import file_formating as ff


PATH_TO_TICKETS = "tickets/"

#foramtuje daty na ładny format
def folder(date):
    return str( date[0:2]+date[3:5] )


class Bilet:
    def __init__( self  , path ):
        self.path              = path
        self.number            = path[6:15]
        self.raw               = self.extract()
        self.words             = self.raw.split(" ")
        self.new_name              = ""
        self.type = "MIESIECZNY"
        if "1,00\nBilet" in self.words:
            self.type = "DODATKOWY"
        
        if self.type == "DODATKOWY":
            self.miejsce           = self.words[65]
            self.wagon             = self.words[71]
            self.departure_station = self.words[24]
            self.departure_time    = self.words[23]
            self.arrival_station   = self.words[25]
            self.arrival_time      = self.words[28]
            self.date              = self.words[27]
        else:
            self.valid_from        = self.words[25]
            self.valid_to          = self.words[28][0:10]

    def setup(self):
        if self.type == "DODATKOWY":
            self.setup_dodatkowy()
        else:
            self.setup_glowny()
        
        #try:
        os.rename( self.path , self.new_name )
        #except:
            #print( "Plik o nazwie  "+self.new_name+"  z pliku  "+self.path+"  istnieje!")
    
    # dodRRMMDD-GODZ-MIEJSCE-WAGON
    def setup_dodatkowy(self):
        name = "dod_"
        name += "D-"+ self.date[3:5]+self.date[0:2] + "--"
        name += "T-"+self.departure_time[0:2] + self.departure_time[3:5] + "--"
        name += "M-"+self.miejsce + "-"
        name += self.wagon
        name += ".pdf"
        self.new_name = name


    # mies RRMMDD-RRMMDD
    def setup_glowny(self):
        name = "mie_od_" + folder(self.valid_from) + "-do_" + folder(self.valid_to) + ".pdf"
        self.new_name = name
        '''try:
            os.mkdir(name)
            print("Utworzono folder ",name)
        except:
            print("Folder już istnieje")'''


    # oddiela tekst z pliku pdf
    def extract( self ):
        pdf = pdfplumber.open( self.path )
        re = pdf.pages[0].extract_text()
        pdf.close()
        return re

    #debug only
    def debug( self ):
        print( self.path )
        print( self.raw )
        print( self.words )
        print( self.type )
        print( self.miejsce )
        print( self.wagon )
        print( self.date )
        print( self.arrival_time )
        print( self.departure_time )
        print( folder(self.date) ) 
        

# przelatuje folder i formatuje wszystkie pliki w nim zawarte
def rename_folder():
    for ticket in os.listdir( PATH_TO_TICKETS ):
        print("Plik: "+ ticket )
        if ticket.endswith(".pdf") and (ticket[0:5] == "bilet" or ticket[0:3]=="eic"):
            print("good")
            bilet = Bilet( PATH_TO_TICKETS + ticket )
           # bilet.debug()
            bilet.setup()
            print(ticket,"done")
    print("everything done!")

if __name__ == "__main__":
    rename_folder()

    