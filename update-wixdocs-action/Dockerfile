FROM python:3.9

COPY . ./update-wixdocs-action
WORKDIR update-wixdocs-action
RUN pip3 install requests
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/update-wixdocs-action/entrypoint.sh"]