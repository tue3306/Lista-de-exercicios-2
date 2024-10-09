# Exercício 2

class Motor:
    def status(self):
        return "Motor está funcionando."

class Pneu:
    def status(self):
        return "Pneus estão em bom estado."

class Veiculo(Motor, Pneu):
    def status(self):
        status_motor = Motor.status(self)  
        status_pneu = Pneu.status(self)   
        return f"Status do veículo:\n{status_motor}\n{status_pneu}"


veiculo = Veiculo()
print(veiculo.status())
