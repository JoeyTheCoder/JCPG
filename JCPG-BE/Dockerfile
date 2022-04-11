FROM python:3

WORKDIR /home/joel/Desktop/CodingProjects/JCPG/JCPG-BE/app

ENV python = "/usr/lib/python3.8"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]
