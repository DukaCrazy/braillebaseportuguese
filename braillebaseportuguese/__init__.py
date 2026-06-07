from braillebase import BrailleBase

class BrailleBasePortuguese(BrailleBase):
    def __init__(self):

        """
        https://fisicaembraille.ufpr.br/alfabeto-braille/
        https://lepix.org/braillept/
        https://www.infoescola.com/portugues/braile/
        https://pt.wikipedia.org/wiki/Alfabeto_portugu%C3%AAs
        https://www.questoesestrategicas.com.br/resumos/ver/numeros-sinais-matematicos-unidades-monetarias-e-de-medidas
        https://www.deficienciavisual.pt/txt-grafiabrailleLP.htm
        """
        super().__init__()
        self.setting_braille_rules01("⠨", "⠐") #2026/05/18
        #letras min
        self.append_braille_letter("a", ["⠁"]) #2026/05/18
        self.append_braille_letter("b", ["⠃"]) #2026/05/18
        self.append_braille_letter("c", ["⠉"]) #2026/05/18
        self.append_braille_letter("d", ["⠙"]) #2026/05/18
        self.append_braille_letter("e", ["⠑"]) #2026/05/18
        self.append_braille_letter("f", ["⠋"]) #2026/05/18
        self.append_braille_letter("g", ["⠛"]) #2026/05/18
        self.append_braille_letter("h", ["⠓"]) #2026/05/18
        self.append_braille_letter("i", ["⠊"]) #2026/05/18
        self.append_braille_letter("j", ["⠚"]) #2026/05/18
        self.append_braille_letter("k", ["⠅"]) #2026/05/18
        self.append_braille_letter("l", ["⠇"]) #2026/05/18
        self.append_braille_letter("m", ["⠍"]) #2026/05/18
        self.append_braille_letter("n", ["⠝"]) #2026/05/18
        self.append_braille_letter("o", ["⠕"]) #2026/05/18
        self.append_braille_letter("p", ["⠏"]) #2026/05/18
        self.append_braille_letter("q", ["⠟"]) #2026/05/18
        self.append_braille_letter("r", ["⠗"]) #2026/05/18
        self.append_braille_letter("s", ["⠎"]) #2026/05/18
        self.append_braille_letter("t", ["⠞"]) #2026/05/18
        self.append_braille_letter("u", ["⠥"]) #2026/05/18
        self.append_braille_letter("v", ["⠧"]) #2026/05/18
        self.append_braille_letter("w", ["⠺"]) #2026/05/18
        self.append_braille_letter("x", ["⠭"]) #2026/05/18
        self.append_braille_letter("y", ["⠽"]) #2026/05/18
        self.append_braille_letter("z", ["⠵"]) #2026/05/18

        self.append_braille_letter("á", ["⠷"]) #2026/06/05
        self.append_braille_letter("ã", ["⠜"]) #2026/06/05
        self.append_braille_letter("â", ["⠡"]) #2026/06/05
        self.append_braille_letter("à", ["⠫"]) #2026/06/05
        self.append_braille_letter("é", ["⠿"]) #2026/06/05
        self.append_braille_letter("ê", ["⠣"]) #2026/06/05
        self.append_braille_letter("í", ["⠌"]) #2026/06/05
        self.append_braille_letter("ì", ["⠩"]) #2026/06/05
        self.append_braille_letter("ó", ["⠬"]) #2026/06/05
        self.append_braille_letter("ô", ["⠹"]) #2026/06/05
        self.append_braille_letter("õ", ["⠪"]) #2026/06/05
        self.append_braille_letter("ú", ["⠾"]) #2026/06/05
        self.append_braille_letter("ù", ["⠱"]) #2026/06/05
        self.append_braille_letter("ü", ["⠳"]) #2026/06/05

        self.append_braille_letter("ç", ["⠯"]) #2026/06/05
        self.append_braille_letter("ñ", ["⠻"]) #2026/06/05

       #letras maiusc
        self.append_special_braille_lettr_rules01("A", ["⠁"])
        self.append_special_braille_lettr_rules01("B", ["⠃"])
        self.append_special_braille_lettr_rules01("C", ["⠉"])
        self.append_special_braille_lettr_rules01("D", ["⠙"])
        self.append_special_braille_lettr_rules01("E", ["⠑"])
        self.append_special_braille_lettr_rules01("F", ["⠋"])
        self.append_special_braille_lettr_rules01("G", ["⠛"])
        self.append_special_braille_lettr_rules01("H", ["⠓"])
        self.append_special_braille_lettr_rules01("I", ["⠊"])
        self.append_special_braille_lettr_rules01("J", ["⠚"])
        self.append_special_braille_lettr_rules01("K", ["⠅"])
        self.append_special_braille_lettr_rules01("L", ["⠇"])
        self.append_special_braille_lettr_rules01("M", ["⠍"])
        self.append_special_braille_lettr_rules01("N", ["⠝"])
        self.append_special_braille_lettr_rules01("O", ["⠕"])
        self.append_special_braille_lettr_rules01("P", ["⠏"])
        self.append_special_braille_lettr_rules01("Q", ["⠟"])
        self.append_special_braille_lettr_rules01("R", ["⠗"])
        self.append_special_braille_lettr_rules01("S", ["⠎"])
        self.append_special_braille_lettr_rules01("T", ["⠞"])
        self.append_special_braille_lettr_rules01("U", ["⠥"])
        self.append_special_braille_lettr_rules01("V", ["⠧"])
        self.append_special_braille_lettr_rules01("W", ["⠺"])
        self.append_special_braille_lettr_rules01("X", ["⠭"])
        self.append_special_braille_lettr_rules01("Y", ["⠽"])
        self.append_special_braille_lettr_rules01("Z", ["⠵"])

        self.append_special_braille_lettr_rules01("Á", ["⠷"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ã", ["⠜"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Â", ["⠡"]) #2026/06/05
        self.append_special_braille_lettr_rules01("À", ["⠫"]) #2026/06/05
        self.append_special_braille_lettr_rules01("É", ["⠿"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ê", ["⠣"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Í", ["⠌"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ì", ["⠩"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ó", ["⠬"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ô", ["⠹"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Õ", ["⠪"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ú", ["⠾"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ù", ["⠱"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ü", ["⠳"]) #2026/06/05

        self.append_special_braille_lettr_rules01("Ç", ["⠯"]) #2026/06/05
        self.append_special_braille_lettr_rules01("Ñ", ["⠻"]) #2026/06/05

        #number
        self.append_braille_letter("⠼", ["⠼"]) #2026/06/05
        self.append_braille_letter("1", ["⠁"]) #2026/06/05
        self.append_braille_letter("2", ["⠃"]) #2026/06/05
        self.append_braille_letter("3", ["⠉"]) #2026/06/05
        self.append_braille_letter("4", ["⠙"]) #2026/06/05
        self.append_braille_letter("5", ["⠑"]) #2026/06/05
        self.append_braille_letter("6", ["⠋"]) #2026/06/05
        self.append_braille_letter("7", ["⠛"]) #2026/06/05
        self.append_braille_letter("8", ["⠓"]) #2026/06/05
        self.append_braille_letter("9", ["⠊"]) #2026/06/05
        self.append_braille_letter("0", ["⠚"]) #2026/06/05

        
        #math
        self.append_braille_letter("+", ["⠖"]) #2026/06/05
        self.append_braille_letter("-", ["⠤"]) #2026/06/05
        self.append_braille_letter("*", ["⠔"]) #2026/06/05
        self.append_braille_letter("×", ["⠦"]) #2026/06/05
        self.append_braille_letter("/", ["⠠"]) #2026/06/05
        self.append_braille_letter("÷", ["⠲"]) #2026/06/05
        self.append_braille_letter("=", ["⠶"]) #2026/06/05
        self.append_braille_letter("°", ["⠕"]) #2026/06/05
        self.append_braille_letter("%", ["⠸", "⠴"]) #2026/06/05
        self.append_braille_letter("√", ["⠫"]) #2026/06/05
        
        #Simbol
        self.append_braille_letter(".", ["⠄"]) #2026/06/05
        self.append_braille_letter(",", ["⠂"]) #2026/06/05
        self.append_braille_letter(";", ["⠆"]) #2026/06/05
        self.append_braille_letter(":", ["⠒"]) #2026/06/05
        self.append_braille_letter("?", ["⠢"]) #2026/06/05
        self.append_braille_letter("!", ["⠖"]) #2026/06/05

        self.append_braille_letter("(", ["⠣", "⠄"]) #2026/06/05
        self.append_braille_letter(")", ["⠠", "⠜"]) #2026/06/05
        self.append_braille_letter("<", ["⠪"]) #2026/06/05
        self.append_braille_letter(">", ["⠕"]) #2026/06/05
        self.append_braille_letter("[", ["⠷", "⠄"]) #2026/06/05
        self.append_braille_letter("]", ["⠠", "⠾"]) #2026/06/05
        self.append_braille_letter("\u201C", ["⠦"]) # “ #2026/06/05
        self.append_braille_letter("\u201D", ["⠴"]) # ” #2026/06/05
        #self.append_braille_letter("‘", ["⠄", "⠦"])


        #self.append_braille_letter("\u002F", ["⠌"])      # /
        #self.append_braille_letter("\u005C", ["⠸", "⠌"]) # \


        self.append_braille_letter("#", ["⠼"]) #2026/06/05
        self.append_braille_letter("|", ["⠸"]) #2026/06/05

        self.append_braille_letter("'", ["⠄"])
        self.append_braille_letter("@", ["⠱"]) #2026/06/05
        self.append_braille_letter("R$", ["⠨", "⠗", "⠌"]) #2026/06/05
        self.append_braille_letter("$", ["⠰"]) #2026/06/05
        self.append_braille_letter("€", ["⠈", "⠑"]) #2026/06/05 #2026/06/05
        self.append_braille_letter("£", ["⠈", "⠇"])

        self.append_braille_letter("_", ["⠨"]) #2026/06/05
        #jus
        self.append_braille_letter("ª", ["⠄", "⠘"]) #2026/06/05
        self.append_braille_letter("§", ["⠎", "⠎"]) #2026/06/05
        self.append_braille_letter("※", ["⠔"])
        self.append_braille_letter("’", ["⠳"]) #2026/06/05
        self.append_braille_letter("&", ["⠯"]) #2026/06/05
        self.append_braille_letter("^", ["⠈"]) #2026/06/05
        self.append_braille_letter("~", ["⠐"]) #2026/06/05

        self.append_braille_letter("...", ["⠄", "⠄", "⠄"])
        self.append_braille_letter("…", ["⠄", "⠄", "⠄"])
        self.append_braille_letter("———", ["⠤", "⠤", "⠤"])
        
        #self.append_special_braille_letter("I", ["⠠", "⠊"])
        #self.append_special_braille_letter("II", ["⠠", "⠊", "⠊"])
        #self.append_special_braille_letter("III", ["⠠", "⠊", "⠊", "⠊"])
        #self.append_special_braille_letter("IV", ["⠠", "⠊", "⠧"])
        #self.append_special_braille_letter("art.", ["⠼", "⠁"])


#TEST
#bb = BrailleBasePortuguese()
#print(bb.output_braille_txt("AAaAAAaaaAa 112233aA"))
