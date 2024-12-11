FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime
ENV DEBIAN_FRONTEND=noninteractive
ENV TARGET_COSY_MODEL_NAME=CosyVoice-300M-Instruct

WORKDIR /opt/CosyVoice

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get -y install git unzip git-lfs
RUN git lfs install
RUN git clone --recursive https://github.com/the-loki/CosyVoice.git
# here we use python==3.10 because we cannot find an image which have both python3.8 and torch2.0.1-cu118 installed
RUN cd CosyVoice && pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
RUN cd CosyVoice && python3 download_model.py
RUN cd pretrained_models/CosyVoice-ttsfrd/ && unzip resource.zip -d . &&  pip install ttsfrd-0.3.6-cp38-cp38-linux_x86_64.whl
RUN cd CosyVoice/runtime/python/grpc && python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. cosyvoice.proto