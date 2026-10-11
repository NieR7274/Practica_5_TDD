
class Paqueteria:
    def Costo_Envio(self, pesoPaquete: float, tipoEnvio: str) -> float:

       if pesoPaquete <= 0:
               raise ValueError("El peso del paquete debe ser mayor que cero")

       if tipoEnvio not in ("estandar", "expres"):
               raise ValueError("Tipo de envio no valido")

       costoExtra = 0.0

       if pesoPaquete <= 5 and tipoEnvio == "estandar":
           return 50.00
       
       if pesoPaquete > 5 and tipoEnvio == "estandar":
                  costoExtra = (pesoPaquete - 5) * 10
                  return 50.00 + costoExtra
       
       if pesoPaquete <= 5 and tipoEnvio == "expres":
              return 100.00

       if pesoPaquete > 5 and tipoEnvio == "expres":
                         costoExtra = (pesoPaquete - 5) * 10
                         return (50.00 + costoExtra) * 2


