# Voice-Recognition-Python-Backend

 - [Instalando ambiente virtual _python_](#instalando-ambiente-virtual-python)
 - [Instalando _pip_](#instalando-pip)
 - [Atualizando dependências do projeto](#atualizando-dependências-do-projeto)
 - [Criando e ativando ambiente virtual](#criando-e-ativando-ambiente-virtual)
 - [Atualizando dependências](#atualizando-dependências)

## Instalando dependências

### Instalando ambiente virtual _python_

_Linux_ (Debian/Ubuntu e derivados):
```bash
sudo apt update
sudo apt install python3-venv python3-pip -y
```
ou para uma versão específica:
```bash
sudo apt install python3.12-venv
```
O comando acima também instala o _pip_.

_macOS_:
```bash
brew install python
```

após isso, `python3 -m venv venv` já funciona.


_Windows_ (Usando _**winget**_):
```powershell
winget install Python.Python.3.12
```

depois, rode:
```powershell
python -m venv venv
```

### Instalando _pip_

_macOS_:
O _**Homebrew**_ já traz consigo o _pip_. Você pode confirmar com:
```bash
pip3 --version
```
caso não esteja instalado, instale com:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

_Windows_:
Caso o _Python_ tenha sido instalado pelo [**instalador oficial**](https://www.python.org/downloads/), o _pip_ já vem incluído. Se `pip --version` (sem o **3** do _macOS_) falhar, tente:

```powershell
python -m ensurepip --upgrade
```

ou:

```powershell
python -m pip install --upgrade pip
```

### Atualizando dependências do projeto

O arquivo `requirements.txt` permite concentrar todas as dependências utilizadas no projeto em um único local. Assim, é possível atualizar as dependências em abientes de trabalho (ou máquinas) diferentes.

#### Criando e ativando ambiente virtual

Crie o ambiente virtual `venv` com:

```bash
python3 -m venv venv
```

Ative-o com:

```bash
source venv/bin/activate
```
Em seguida, você verá `(venv)` antes da linha de _prompt_ de seu terminal, como na imagem:

![Texto alternativo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF4WsWEZ9aIQ2zzJz64Guf6cRCBki6Mb5fiQ&s)

Ao terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o comando `deactivate`.

#### Atualizando dependências

Para atualizar as dependências do projeto, simplesmente execute:

```bash
pip install -r requirements.txt
```

Caso precise instalar alguma outra dependência além das de _requirements.txt_, adicione àquelas já usadas no projeto com:

```
pip freeze > requirements.txt
```
