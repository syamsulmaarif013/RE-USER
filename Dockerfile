# We're using Ubuntu 20.10
FROM spacebot14/angkasaboy:spaceman
#
# Clone repo and prepare working directory
#
RUN git clone -b Kampang https://github.com/AngkasaBoy/Space-Bot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/AngkasaBoy/Space-Bot/Kampang/requirements.txt

EXPOSE 80 433

#Finalization
CMD ["python3","-m","userbot"]
