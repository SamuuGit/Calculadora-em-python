#  Calculadora Python

Bem-vindo ao meu projeto de calculadora em Python! Este software foi desenvolvido com foco em robustez lógica e uma interface de terminal fluida.

## Diferenciais e Tratamento de Erros

Diferente de calculadoras básicas, este programa antecipa limites matemáticos para garantir estabilidade:

* **Divisão:** Tratamento de erro para divisores nulos ($n/0$), retornando `Infinito` em vez de interromper a execução.
* **Raiz Quadrada:** Bloqueio de entrada de números negativos, restringindo as operações ao conjunto dos **Números Reais**.
* **Potenciação:** Proteção específica para base zero com expoente negativo, com feedback amigável ao usuário.

##  Interface e UX (User Experience)

O foco foi criar uma experiência que não parecesse um "script travado", mas sim um software real:

* **Fluxo de Navegação:** Uso estratégico de `time.sleep()` para cadência e `os.system()` para limpeza inteligente do console.
* **Formatação Inteligente (`f(n)`):** Função personalizada que trata a exibição numérica:
  - Remove o `.0` desnecessário de números inteiros.
  - Limita automaticamente números decimais a 2 casas decimais.

##  Estrutura de Dados e Controle

* **Histórico:** Implementação de uma lista dinâmica para armazenar e listar as operações realizadas durante a sessão.
* **Menu Moderno:** Utilização da estrutura `match case`, funcionalidade de controle de fluxo introduzida no **Python 3.10+**.

---
