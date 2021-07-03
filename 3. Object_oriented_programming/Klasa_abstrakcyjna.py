from abc import ABC, abstractmethod

class myclass(ABC):

    @abstractmethod # dekorator
    def wylicz_objetosc(self):
        pass
    
    def wyswietl_objetosc(self):
        print(f"obwod kola wynosi:  {self.wylicz_objetosc()}.")
    
class obj_pol_kolo(myclass):
    def wylicz_objetosc(self):

        x = 2*3.14*4
        return x
    

def main():
    kolo = obj_pol_kolo()
    kolo.wyswietl_objetosc()

if __name__ == "__main__":
    main()

# output
# =============================================================================
# obwod kola wynosi:  25.12.
# =============================================================================
