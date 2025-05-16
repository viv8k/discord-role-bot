# Pythonの公式イメージを使用
FROM python:3.11

# 作業ディレクトリを作成
WORKDIR /app

# ファイルをコピー
COPY . /app

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# Botを起動（bot.pyを使ってる前提）
CMD ["python", "bot.py"]
