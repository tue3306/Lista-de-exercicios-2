# Lista de Exercícios 2 

**Instruções:**  
Fazer a entrega dos arquivos `.py`, link do projeto no Google Colab ou link do GitHub na atividade do Moodle.

## Exercícios

### Exercício 1:
Crie uma classe base `Forma` com um método `desenhar()` que desenha uma forma qualquer utilizando a biblioteca `Turtle`. Em seguida, crie subclasses `Círculo` e `Quadrado` que herdam de `Forma` e sobrescrevem `desenhar()` para desenhar as formas específicas.

### Exercício 2:
Crie classes `Motor`, `Pneu`, `Veiculo`, onde `Veiculo` herda tanto de `Motor` quanto de `Pneu`. Ambas as classes base (`Motor` e `Pneu`) devem ter um método chamado `status()` que retorna uma string. A classe `Veiculo` deve também ter um método `status()` que chama os métodos `status()` das classes base. Implemente a herança de modo que a classe `Veiculo` resolva o método `status()` de maneira correta.

### Exercício 3:
Implemente uma classe `Ponto` com um construtor que aceita coordenadas `x` e `y` como atributos. Utilize o objeto ponto como parâmetro para o comando `goto()` da `Turtle`.

### Exercício 4:
Crie um sistema de simulação bancária onde diferentes tipos de contas compartilham algumas operações comuns, mas também têm regras específicas.  
Defina uma classe abstrata `ContaBancaria` com métodos abstratos para `depositar()`, `sacar()` e `calcular saldo()`.  
Crie duas subclasses concretas: `ContaCorrente` e `ContaPoupanca`.

- **ContaCorrente:** Deve permitir um saldo negativo até um certo limite (cheque especial).
- **ContaPoupanca:** Não deve permitir saldo negativo e deve calcular juros sobre o saldo atual.

Implemente métodos para exibir informações da conta.  
As contas devem ter atributos como número da conta, titular e saldo.  
A função `sacar()` de `ContaPoupanca` deve recusar a operação se o saldo ficar negativo.
