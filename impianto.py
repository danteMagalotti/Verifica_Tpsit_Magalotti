class ImpiantoSolare
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.località = località
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli = []
        
    def aggiungi_pannello(self, pannello : PannelloFotovoltaico) -> None:
        if pannello.potenza_kw > potenza_massima_kw:
            raise ValueError("Non puoi inserire un pannello con potenza maggiore della massima")
        for p in pannelli:
            if p.codice == pannello.codice:
                raise ValueError("Pannello gia presente")
            pannelli.append(pannello)
            
    def potenza_pannelli(self) -> float:
        potenza = 0
        for p in pannelli:
            potenza = potenza + p.potenza_kw
        return potenza
    
    def cerca_pannello(self, codice : str) -> PannelloFotovoltaico | None:
        for p in pannelli:
            if p.codice ==  codice:
                return p
        return None
                
    def rimuovi_pannello(self,codice:str) -> PannelloFotovoltaico | None:
        for p in pannelli:
            if p.codice ==  codice:
                pannelli.remove(p)
                return p
        return None
    def pannelli_sotto_potenza(self,potenza_massima: float) -> list[PannelloFotovoltaico]:
        return [p for p in pannelli if p <= potenza_massima]
    
        
        