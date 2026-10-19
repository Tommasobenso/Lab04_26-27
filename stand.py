

class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base
        self.disponibile = True     # inizializzo per vedere se è disponibile
        self.espositore = None      # inizializzo a None perchè per ora non ho espositore assegnato


    def calcola_prezzo(self):
        return self.prezzo_base

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"{self.codice} | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}")

    # metodo di confronto
    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()


# classe figlia
class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.numero_prese = numero_prese

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.numero_prese)

    def __str__(self):
        return (f"{super().__str__()} - Prese aggiuntive: {self.numero_prese}")


# altra classe figlia
class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        return (f"{super().__str__()} - Posizione: {self.posizione}")
