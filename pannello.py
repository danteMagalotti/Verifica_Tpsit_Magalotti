class PannelloFotovoltaico
    def __init__(self, codice: str, modello: str, potenza_kw: float) -> None:
        self.codice = codice
        self.modello = modello
        if potenza_kw <= 0:
            raise ValueError("Non è possibile inserire una potenza minore o uguale a 0")
        self.potenza_kw = potenza_kw