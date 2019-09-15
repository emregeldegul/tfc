# TFC
Simple Translate App From Clipboard (Translate From Clipboard)

![TFC](images/tfc.png)

The TFC listens the clipboard and translates the copied words using yandex translate. And it shows as notification.

![TFC](images/tfcPicture.jpg)

# Setup
Firstly, take a yandex translate api key.

**Yandex Translate API:** https://tech.yandex.com/translate/doc/dg/concepts/about-docpage/

After take api key, create a config file as `.tfc.config.json` on **home** directory.

It should look like this:

```json
{
    "key": "YandexTranslateKey",
    "lang": "en-tr"
}
```
Ok. Now you can download and install.

```bash
~$ git clone https://github.com/emregeldegul/tfc && cd tfc
~$ pip install -r requirements.txt
~$ python setup.py install
```

That's all. Now you can run the program by write `tfc` from the terminal.

```bash
~$ tfc
```

# Project Idea
I learning English and I translate the words I don't know one by one. It's difficult.

Previously, Ömer Faruk Bayram wrote a similar project. But he deleted the project. So I wrote it again.
