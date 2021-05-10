import pdfplumber
import os
import file_formating as ff

#foramtuje daty na ładny format
def folder(date):
    return str( date[8:10] + date[3:5] + date[0:2] )


class Bilet:
    def __init__( self  , path ):
        self.path              = path
        self.number            = path[6:15]
        self.raw               = self.extract()
        self.words             = self.raw.split(" ")
        self.type              = self.words[1]
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
    
    # dodRRMMDD-GODZ-MIEJSCE-WAGON
    def setup_dodatkowy(self):
        name = "dod"
        name += folder(self.date) + "-"
        name += self.departure_time[0:2] + self.departure_time[3:5] + "-"
        name += self.miejsce + "-"
        name += self.wagon
        name += ".pdf"
        os.rename( self.path , name )


    # mies RRMMDD-RRMMDD
    def setup_glowny(self):
        name = "mie_od_" + folder(self.valid_from) + "-do_" + folder(self.valid_to) + ".pdf"
        os.rename( self.path , name)
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

# przelatuje folder i formatuje wszystkie pliki w nim zawarte
def rename_folder():
    for filename in os.listdir("tickets/"):
        typ = filename[0:5]
        if typ == "bilet" and filename.endswith(".pdf"):
            print(filename)
            bilet = Bilet(filename)
            bilet.setup()
            print(filename,"done")
    print("everything done!")

if __name__ == "__main__":
    rename_folder()

    