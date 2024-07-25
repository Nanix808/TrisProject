FROM ubuntu:jammy-20221130

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ARG DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_FRONTEND=noninteractive 

ARG INSTALL_DEV=false


WORKDIR /app


EXPOSE 8000


RUN apt update

RUN apt-get -y update
# RUN apt-get install build-essential -y
# RUN apt-get install zlib1g-dev -y
# RUN apt-get install build-essential -y
# RUN apt-get install zlib1g-dev -y
# RUN apt-get install libncurses5-dev -y
# RUN apt-get install libgdbm-dev -y
# RUN apt-get install libnss3-dev -y
# RUN apt-get install libreadline-dev -y
# RUN apt-get install libffi-dev -y
# RUN apt-get install libsqlite3-dev -y
# RUN apt-get install wget -y
# RUN apt-get install libbz2-dev -y
# RUN apt-get install libgl1-mesa-glx -y
# RUN apt-get install libpcap-dev -y
# RUN apt-get install libpq-dev -y

# RUN apt-get install libssl-dev -y
# RUN apt-get install cargo -y
# RUN apt-get install pkg-config -y

# RUN apt-get install libkrb5-dev -y
# RUN apt-get install gcc -y

# RUN apt-get install libzbar-dev -y
# RUN apt-get install libzbar0 -y

RUN apt-get install build-essential -y
RUN apt-get install libssl-dev -y
RUN apt-get install libffi-dev -y
RUN apt-get install cargo -y
RUN apt-get install pkg-config -y


RUN apt-get install ca-certificates curl


RUN apt-get install python3 python3-pip -y
RUN apt-get install -y python3-bcrypt -y
RUN apt-get install python3.10-dev -y

RUN python3 --version
# RUN python3.11 --version

RUN pip install --upgrade pip


COPY pyproject.toml poetry.lock ./
RUN python3 -m pip install poetry




# RUN poetry update
RUN poetry config virtualenvs.create false

# RUN poetry cache clear --all pypi
RUN poetry install --without dev --no-root

COPY . .




# WORKDIR /app/src


# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# ENTRYPOINT ["poetry", "run", "python3", "-m", "main"]





