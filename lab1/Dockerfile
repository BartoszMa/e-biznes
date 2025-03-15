FROM ubuntu:24.04

RUN apt -y update

RUN apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev wget zip \
    openjdk-17-jdk

RUN wget https://www.python.org/ftp/python/3.10.16/Python-3.10.16.tgz
RUN tar xvf Python-3.10.16.tgz

WORKDIR /Python-3.10.16
RUN ./configure --enable-optimizations --with-ensurepip=install
RUN make -j 8
RUN make altinstall
RUN rm -rf /Python-3.10.16.tgz

WORKDIR /
RUN wget https://services.gradle.org/distributions/gradle-8.13-bin.zip

RUN mkdir /opt/gradle
RUN unzip -d /opt/gradle gradle-8.13-bin.zip

ENV PATH=$PATH:/opt/gradle/gradle-8.13/bin

ENV JAVA_HOME=/usr
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /app
COPY hello_world /app/hello_world

WORKDIR /app/hello_world
RUN gradle build

CMD ["java", "-jar", "build/libs/hello_world.jar"]
