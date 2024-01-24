# Maia Automize
Programa em Python3 com o módulo PyAutoGUI para automatizar suas tarefas 

# Como executar:
Após baixá-lo, crie um ambiente virtual e instale as dependencias,
No meu caso eu instalo com o seguinte comando: 

pip install -r requirement.txt

Depois edite o programa para fazer suas tarefas do pc e rode o comando:
python main.py


# Observações:
Depois de pronto seu programa, você pode transnformá-lo em um executável. 
Para isto use o módulo do python chamado de PyInstaller que você já instalou pelo arquivo requirement.txt.
Eu usei este comando para mim mesmo:

pyinstaller --noconsole --onefile --name="NomeDoSeuPrograma" main.py


Se você estiver no Windows ele criará um .exe, se você estiver no Linux ele criará um executável binário.
 
