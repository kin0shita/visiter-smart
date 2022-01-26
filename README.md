#　環境構築

## 環境の立ち上げ

### 仮想環境の作成
```
python3 -m venv [newenvname]
```

### macの場合
```
$ source [newenvname]/bin/activate
```

### windowsの場合
```
$ .\[newenvname]\Scripts\activate.bat
```

## パッケージのインストール

```
$ pip install -r requirements.txt
```

## secretkeyの生成

## local_settings.py を生成
```
touch menkaiProject/menkaiProject/local_settings.py 
```

### キーの生成
```
python menkaiProject/generate_secretkey_setting.py
```

