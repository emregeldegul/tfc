# TFC
Translate From The Clipboard (Simple Translate App From The Clipboard)

![TFC](images/tfc.png)

TFC listens to the clipboard and translates the copied words using Google Translate. It shows translations as notifications.

![TFC](images/tfcPicture.jpg)

# Setup
Download and install the project.

```bash
~$ git clone https://github.com/emregeldegul/tfc && cd tfc
~$ pip install -r requirements.txt
~$ python setup.py install
~$ sudo apt-get install xclip
```

That's it. You can now run the program from the terminal by writing `tfc`.

```bash
~$ tfc
~$ tfc -h
~$ tfc --dest en --src de
```
