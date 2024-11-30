FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y apt-transport-https \
       ca-certificates curl gnupg2 \
       software-properties-common
       
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN echo "deb [arch=amd64] https://download.docker.com/linux/debian bookworm stable" > /etc/apt/sources.list.d/docker.list

RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io

USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
