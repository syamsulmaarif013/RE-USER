# Using Python Slim-Buster
FROM spacebot14/spaceman:space
#
# Clone repo and prepare working directory
#
RUN git clone -b Kampang https://github.com/AngkasaBoy/Space-Bot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/syamsulmaarif013/RE-USER/Kampang/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
