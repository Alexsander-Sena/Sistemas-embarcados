# Sistemas-embarcados

#### AQUISIÇÃO DE DADOS DE UM AVIÃO EM VOO PARA SER VISUALISADO POR UM OPERADOR NO SOLO ATRAVÉS DE UM HORIZONTE ARTIFICIAL

##### Este projeto tem como objetivo a implementação de recursos de aquisição de dados de uma aeronave em voo. Esses dados vão ser enviados e mostrados para um operador em solo.  

![Horizonte Artificial](https://github.com/Alexsander-Sena/Sistemas-embarcados/blob/main/horizonte%20artificial.png)

### Magnitudes aquisitadas:
  1. Velocidades CAS, TAS -> Pitot/Tomada de pressão Dinâmica e Estática
  2 .Altitude Pressão (ISA) -> Tomada de pressão estática
  3. VS (velocidade vertical) -> Tomada de variação de pressão estática 
  4. Medir atitude e direção de voo -> Giroscópio, Bússola (ver correção de bússola)
  6. Ground Speed (pelo GPS) (Secundário)

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
