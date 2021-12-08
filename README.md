# Proyecto_Intru

## Interfaz Grafica

se uso pyqt5 y qt designer para crear la interfas y poder conectaros a los scrips creados
[Documentacionde Qt designer](https://doc.qt.io/) y [todas als clases](https://doc.qt.io/qt-5.15/classes.html).

[Descarga de qt designer](https://build-system.fman.io/qt-designer-download)


## Requerimientos para su descarga y correrlo

- **Tener instalado virtualenv y saber utilizarlo. aqui se encuentra la [guia de usuario](https://virtualenv.pypa.io/en/latest/user_guide.html)**

- **Despues del `git clone` entrar a la carpeta del proyecto y crear el entorno virtual con:**
```
virtualenv venv
```
- **Ahora debera haberse creado una carpeta llamada `venv`, ahora ejecutar el siguiente comando para entrar al entorno virtual**
    _En VS es un proceso diferente, por eso se recomienda hacerlo en el bash del GIT o en el CMD de windows directamente_
```
source venv/Scripts/activate
```
- **Ejemplo de como debera de verse**
```
(venv) 
Muerto@DESKTOP-8MA1RTD MINGW64 ~/Documents/VS/PracticaSenales (main)
$
```
- **esto se ejecuta el siguiente comando para instalar los modulos en el entorno virtual creado**
```
pip install -r requirements.txt
```

## Para salir den entorno virtual
- **Dentro de la misma carpeta del proyecto ejecutar**
```
deactivate
```
- **Ya no deveria de aparecer `(venv)`**

## Ejecutar el programa

**Para ello se necesita correr el `main.py` y se desplegara la interfaz grafica**
