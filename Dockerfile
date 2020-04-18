FROM  python
MAINTAINER shraddhasaini99@gmail.com
RUN mkdir /src
COPY . /src
CMD python3 /src/fizzbuzz.py
