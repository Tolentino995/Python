# 🐍 Módulos en Python con PIP  

> 🚀 *Aprende a instalar, actualizar y gestionar paquetes en Python como un profesional con PIP.*  

PIP (*Python Package Installer*) es el gestor de paquetes oficial de Python. Nos permite descargar, actualizar y administrar librerías de terceros de forma sencilla.

--- 

## 🛠️ Comandos esenciales de PIP  


# 📌 1️⃣ Ver información de PIP y comprobar actualizaciones
```bash
pip  # Muestra los comandos disponibles y verifica si PIP necesita actualizarse

```
# 📦 2️⃣ Instalar paquetes con PIP
```bash
pip install requests  # 📥 Instala la librería "requests" y sus dependencias
pip install numpy pandas  # 🔄 Instala múltiples paquetes al mismo tiempo
```
# 📜 3️⃣ Listar paquetes instalados
```bash
pip list  # 📃 Muestra todos los paquetes instalados y sus versiones
```
# ❌ 4️⃣ Desinstalar paquetes
```bash
pip uninstall requests  # 🚮 Elimina la librería "requests"
pip uninstall numpy pandas  # 🔥 Desinstala múltiples paquetes a la vez
```
# 🎯 5️⃣ Instalar una versión específica de un paquete
```bash
pip install numpy==1.19.5  # ⏳ Instala la versión 1.19.5 de NumPy en lugar de la última
```
# ⬆️ 6️⃣ Actualizar un paquete a su última versión
```bash
pip install pandas --upgrade  # 📡 Descarga y actualiza el paquete a su versión más reciente
```
# 🔍 7️⃣ Ver paquetes desactualizados
```bash
pip list --outdated  # 📢 Muestra una lista de paquetes que necesitan actualización
```
# ℹ️ 8️⃣ Ver detalles de un paquete instalado
```bash
pip show requests  # 🔎 Muestra información detallada sobre el paquete
```
# 📄 9️⃣ Guardar lista de paquetes en un archivo de respaldo
```bash
pip freeze > requirements.txt  # 📂 Guarda todos los paquetes y versiones en un archivo .txt
```
# 🛠️ 🔟 Restaurar un entorno con los mismos paquetes
```bash
pip install -r requirements.txt  # 📌 Instala los paquetes desde un archivo de requerimientos
