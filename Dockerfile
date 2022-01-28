FROM ubuntu:20.04

WORKDIR '/app'

# Install platform dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3.8 python3-pip curl zip

# Install Zagreus
RUN curl -L https://github.com/mariokaufmann/zagreus/releases/download/v0.0.4/zagreus-linux.zip > zagreus.zip
RUN unzip zagreus.zip
RUN rm -rf swagger-docs zagreus.zip

# Cleanup
RUN apt-get remove -y curl zip

# Copy application files to workdir
COPY template ./template
COPY shell.py .
COPY requirements.txt .
COPY run.sh .

# Install Python dependencies, remove requirements file
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

# Expose web port
EXPOSE 58179

# Start Zagreus shell
ENTRYPOINT [ "/bin/bash", "run.sh" ]