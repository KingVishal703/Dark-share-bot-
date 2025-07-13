# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

FROM python:3.10-slim

RUN apt update && apt upgrade -y
RUN apt install git -y

COPY requirements.txt /requirements.txt

RUN pip install -U pip && pip install -U -r requirements.txt

WORKDIR /VJ-File-Store
COPY . /VJ-File-Store

CMD ["python", "bot.py"]
