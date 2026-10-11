
class Paqueteria:
    def Costo_Envio(self, pesoPaquete: float, tipoEnvio: str) -> float:

       if pesoPaquete <= 0:
               raise ValueError("El peso del paquete debe ser mayor que cero")

       if tipoEnvio not in ("estandar", "expres"):
               raise ValueError("Tipo de envio no valido")

       Costobase = 50.00
       ExpresMultiplicativo = 2.00

       if pesoPaquete <= 5 :
           costoTotal = Costobase
       else:
            costoExtra = (pesoPaquete - 5) * 10
            costoTotal = Costobase + costoExtra

       if  tipoEnvio == "expres":
          costoTotal = costoTotal * ExpresMultiplicativo

       return costoTotal 
       