from impianto import ImpiantoSolare
def main() -> None:
    def registra_impianto(self,impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None:
        for i in impianti:
            if i.codice == impianto.codice:
                raise ValueError("Impianto gia presente")
        impianti.append(impianto)
        
    def cerca_impianto(self,impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare | None:
        for i in impianti:
            if i.codice.lower() == codice.lower():
                return i
        return None
    
    def riepilogo_impianti(self,nome_azienda: str, impianti: list[ImpiantoSolare]) -> None:
        for i in impianti:
            print f" {i} \n {i.modello} \n {i.stato} \n {i.potenza_pannelli()}"
            
    impianti: list(ImpiantoSolare) = []
    registra_impianto(impianti, ImpiantoSolare("BBB", "Aurora", "Bologna", 100, "in installazione" ))
    impianti_solari.append()


if __name__ == "__main__":
    main()
