from braillebase import BrailleBase

class BrailleBasePortuguese(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠨", "⠐") #2026/05/18
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
        self.append_special_braille_letter_rules_uppercase("A", ["⠁"])
        self.append_special_braille_letter_rules_uppercase("B", ["⠃"])
        self.append_special_braille_letter_rules_uppercase("C", ["⠉"])
        self.append_special_braille_letter_rules_uppercase("D", ["⠙"])
        self.append_special_braille_letter_rules_uppercase("E", ["⠑"])
        self.append_special_braille_letter_rules_uppercase("F", ["⠋"])
        self.append_special_braille_letter_rules_uppercase("G", ["⠛"])
        self.append_special_braille_letter_rules_uppercase("H", ["⠓"])
        self.append_special_braille_letter_rules_uppercase("I", ["⠊"])
        self.append_special_braille_letter_rules_uppercase("J", ["⠚"])
        self.append_special_braille_letter_rules_uppercase("K", ["⠅"])
        self.append_special_braille_letter_rules_uppercase("L", ["⠇"])
        self.append_special_braille_letter_rules_uppercase("M", ["⠍"])
        self.append_special_braille_letter_rules_uppercase("N", ["⠝"])
        self.append_special_braille_letter_rules_uppercase("O", ["⠕"])
        self.append_special_braille_letter_rules_uppercase("P", ["⠏"])
        self.append_special_braille_letter_rules_uppercase("Q", ["⠟"])
        self.append_special_braille_letter_rules_uppercase("R", ["⠗"])
        self.append_special_braille_letter_rules_uppercase("S", ["⠎"])
        self.append_special_braille_letter_rules_uppercase("T", ["⠞"])
        self.append_special_braille_letter_rules_uppercase("U", ["⠥"])
        self.append_special_braille_letter_rules_uppercase("V", ["⠧"])
        self.append_special_braille_letter_rules_uppercase("W", ["⠺"])
        self.append_special_braille_letter_rules_uppercase("X", ["⠭"])
        self.append_special_braille_letter_rules_uppercase("Y", ["⠽"])
        self.append_special_braille_letter_rules_uppercase("Z", ["⠵"])

        self.append_special_braille_letter_rules_uppercase("Á", ["⠷"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ã", ["⠜"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Â", ["⠡"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("À", ["⠫"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("É", ["⠿"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ê", ["⠣"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Í", ["⠌"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ì", ["⠩"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ó", ["⠬"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ô", ["⠹"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Õ", ["⠪"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ú", ["⠾"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ù", ["⠱"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ü", ["⠳"]) #2026/06/05

        self.append_special_braille_letter_rules_uppercase("Ç", ["⠯"]) #2026/06/05
        self.append_special_braille_letter_rules_uppercase("Ñ", ["⠻"]) #2026/06/05

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
