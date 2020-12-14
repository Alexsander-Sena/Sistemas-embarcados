# Sistemas Embarcados

#### On Board - Data Logger

##### Este projeto tem como objetivo a implementação de recursos para a aquisição de dados de uma aeronave em voo. Esses dados vão ser enviados e mostrados em um horizonte artificial para um operador em solo.  

![Horizonte Artificial](https://github.com/Alexsander-Sena/Sistemas-embarcados/blob/main/horizonte%20artificial.png)

### Dados aquisitadas:

  1. Ângulos de rolagem: Roll, Pitch e Yaw
  2. Velocidade
  3. Latitude 
  4. Longitude
  
### Arquitetura do projeto

  O projeto consistiu em elaborar um sistema embarcado capaz de coletar dados em voo e enviá-los para uma base em solo que fará o display em um horizonte artificial.Para isso, foram utilizados as seguintes instrumentações:
  
  1.Microcontrolador: STM32F103C8
  2.Acelerômetro/Giroscópio: comunicação I2C com módulo GY521
  3.GPS: comunicação UART com módulo UBLOX NEO 6M
  4.LoRa: comunicação UART com módulo E32-100-TTL
  5.Magnetômetro: leitura de dado analógico
  
  Em conjunto, foram desenvolvidos dois softwares:
  
  1.Software para microcontrolador: STM32IDE (linguagem C)
  2.Software para o display: Visual Code (Python)
  
 ![Arquitetura_projeto](https://github.com/Alexsander-Sena/Sistemas-embarcados/blob/main/Arquitetura_projeto.png)
 
 
 Por meio do módulo de acelerômetro e giroscópio foi possível obter dados de aceleração e velocidade angular nos eixos X, Y e Z. Esses dados, aliados com a bússola, permitiram calcular Roll, Pitch e Yaw.

Além disso, por meio do módulo de GPS, obtemos os dados de latitude, longitude e velocidade instantânea.

Esses dados são enviados por meio do transmissor LoRa, no seguinte formato:
roll;pitch;yaw;latitude;longitude;velocidade
Todos os dados são float, com pelo menos 2 casas decimais.

Um outro transmissor LoRa fica conectado ao computador, que recebe os dados e os exibe no programa desenvolvido em Python para o display no horizonte infinito em tempo real.
  
  


### Requisitos:
  1. Frequência de Aquisição: A freqûencia de aquisição dos dados deve ser bem alta, pois o piloto deve saber com precisão a situação real da aeronave para a     tomada de decisão. (10-100Hz)
  2. Mínimo Delay entre Aquisição e Amostra de Dados processados: Da mesma forma que a aquisição de dados deve ser alta, o tempo de processamento desses dados para mostrar para o piloto deve ser baixo. (máximo em 250 ms)
  3. Confiabilidade. Elemento crítico, componentes devem apresentar certificação aeronáutica para garantir baixa probabilidade de falha. A falha de um componente não deve atrapalhar o funcionamento dos outros nem de sistema em geral. Um sistema de backup pode ser cogitado.


### Testes


### Construído com


### Controle de versão


### Alunos

* Alexsander S. Sena
* Artur T. Diniz - 10308850
* Danilo H. Akiyama
* Guillhermo A. Krauch


### Instituição

* Escola de Engenharia de São Carlos 
* Universidade de São Paulo

### Docente responsável
* Glauco Augusto de Paula Caurin


![Emblema USP](https://github.com/Alexsander-Sena/Sistemas-embarcados/blob/b4b058cf1a0cc124654e30185625317d8727fa73/unnamed.png)
