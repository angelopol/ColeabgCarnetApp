# App to make carnets for the Colegio de Abogados del Estado Carabobo members
## Old Project

- Maded with Python, OpenCV and Tkinter, use a MYSQL Database
- Fill the inputs with the DB members info
- Select photo from a local driver
- Save carnets in local DB for the next time
- Validate the members billings
- Make carnets without internet connection and save the data when the connection return

## Compile with PyInstaller

- python -m PyInstaller --noconsole --onefile --windowed --icon=assets/logo.ico --hidden-import babel.numbers home.py
- python -m PyInstaller --onefile --icon=assets/logo.ico OfflineUpdates.py