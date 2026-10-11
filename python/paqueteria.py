class Paqueteria:
    def Costo_Envio(self, pesoPaquete: float, tipoEnvio: str) -> float:
        """
        Calcula el costo total de envio de un paquete segun su peso y tipo.
        """
        # Validacion: el peso debe ser positivo
        if pesoPaquete <= 0:
            raise ValueError("El peso del paquete debe ser mayor que cero")

        # Validacion: solo se aceptan dos tipos de envio
        if tipoEnvio not in ("estandar", "expres"):
            raise ValueError("Tipo de envio no valido")

        # Constantes de costo base y multiplicador
        Costobase = 50.00
        ExpresMultiplicativo = 2.00

        # Calculo del tarifa base segun el peso
        if pesoPaquete <= 5:
            costoTotal = Costobase
        else:
            # Si pesa mas de 5 kg se cobran 10 pesos por cada kg extra
            costoExtra = (pesoPaquete - 5) * 10
            costoTotal = Costobase + costoExtra

        # Si el envio es expres se duplica el costo total
        if tipoEnvio == "expres":
            costoTotal = costoTotal * ExpresMultiplicativo

        return costoTotal