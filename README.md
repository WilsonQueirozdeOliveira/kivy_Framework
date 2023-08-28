# kivy_Framework

learning from kivy documatation

kivy_pong_game

# pyinstaller

- git clone https://github.com/pyinstaller/pyinstaller
- cd pyinstaller
- cd bootloader
- python ./waf distclean all
- python ./waf all --target-arch=64bit #optional#
- python ./waf all #optional#
- cd ..
- pip install .

- run to compile in .exe : pyinstaller .\main.py --onefile --add-data="TheLab.kv;."