ARG BASE_IMAGE=paketobuildpacks/run-jammy-base


FROM $BASE_IMAGE
ARG HOME

LABEL maintainer="Swiss Data Science Center <info@datascience.ch>"

USER root
SHELL [ "/bin/bash", "-c", "-o", "pipefail" ]

# Install additional dependencies and nice-to-have packages
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    curl \
    git \
    gnupg \
    graphviz \
    jq \
    less \
    libsm6 \
    libxext-dev \
    libxrender1 \
    libyaml-0-2 \
    libyaml-dev \
    lmodern \
    musl-dev \
    nano \
    netcat \
    rclone \
    unzip \
    vim \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1 && \
    wget -q  https://github.com/justjanne/powerline-go/releases/download/v1.24/powerline-go-linux-"$(dpkg --print-architecture)" -O /usr/local/bin/powerline-shell && \
    chmod a+x /usr/local/bin/powerline-shell 

USER cnb
RUN mkdir $HOME/.jupyter_config
COPY jupyter_server_config.py jupyter_notebook_config.py $HOME/.jupyter_config/


# configure bash and shell prompt
ENV PATH=$HOME/.local/bin:$PATH
ENV SHELL=bash
COPY --chown=1000:100 bashrc profile /renku/
RUN cat "/renku/bashrc" >> "${HOME}/.bashrc"
RUN cat "/renku/profile" >> "${HOME}/.profile"

COPY entrypoint.sh /entrypoint.sh



