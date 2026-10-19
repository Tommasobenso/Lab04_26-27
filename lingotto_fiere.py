from stand import Stand, StandPreseExtra, StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.stand = {}
        self.espositori = {}



    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        with open(file_path, "r", encoding="utf-8") as file:
            for riga in file:
                riga = riga.strip()
                if riga == "":
                    continue
                campi = riga.split(",")

                codice = campi[0]
                if codice.startswith("ST"):     # se è uno stand
                    superficie = float(campi[1])
                    padiglione = int(campi[2])
                    prezzo_base = float(campi[3])

                    if len(campi) == 4: # creo oggetto
                        stand = Stand(codice, superficie, padiglione, prezzo_base)
                    elif campi[4].isdigit():      # se stringa ha valore numerico
                        numero_prese = int(campi[4])
                        stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, numero_prese)
                    else:           # ultimo caso
                        posizione = campi[4]
                        stand = StandPremium(codice, superficie, padiglione, prezzo_base, posizione)

                    self.stand[codice] = stand  # aggiorno il dizionario

                elif codice.startswith("ES"):   # se è espositore
                    nome = campi[1]
                    cognome = campi[2]

                    espositore = Espositore(codice, nome, cognome)
                    self.espositori[codice] = espositore


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        # faccio i vari controlli: devono esistere lo stand, l'espositore, lo stand deve essere disponibile e l'espositore libero
        if codice_stand not in self.stand:
            raise Exception("Stand non presente.")
        if codice_espositore not in self.espositori:
            raise Exception("Espositore non presente.")

        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]

        if not stand.disponibile:
            raise Exception("Stand già assegnato.")
        for codice in self.stand:
            stand_attuale = self.stand[codice]
            if stand_attuale.espositore is espositore:
                raise Exception("L'espositore ha già uno stand assegnato.")

        # eseguo assegnazione
        stand.espositore = espositore
        stand.disponibile = False



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        # stand.espositore è il collegamento tra stand ed espositore
        for codice_espositore in self.espositori:   # percorro chiavi dizionario
            espositore = self.espositori[codice_espositore]

            stand_assegnato = None  # variabile per la ricerca
            for codice_stand in self.stand:     # esamino gli stand per l'espositore corrente
                stand = self.stand[codice_stand]
                if stand.espositore is espositore:
                    stand_assegnato = stand
                    break
            if stand_assegnato is None:
                print(f"{espositore} - Nessuno stand assegnato")
            else:
                print(f"{espositore} - Stand: {stand_assegnato.codice}")




    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stand.values())
