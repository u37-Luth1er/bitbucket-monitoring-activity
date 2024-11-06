from openpyxl import Workbook
from datetime import datetime
from openpyxl import Workbook, load_workbook
import pytz
from email.message import EmailMessage
import json, random, sys, requests, smtplib
import argparse

class repo_created_monitoring:
    def __init__(self, token, created):
        self._token = token
        self.created = created
    def created_monitoring(self):
        secret = { 'Authorization': 'Basic {}'.format(self._token),
                'Accept' : 'application/json'}

        workspace = '' # your workspace here
        base_url = "https://api.bitbucket.org/2.0"
        repos_list = []
        url = f"{base_url}/repositories/{workspace}"
        while url:
            response = requests.get(url, headers = secret)
            response_data = json.loads(response.content)
            repos_list += response_data["values"]
            if "next" in response_data:
                url = response_data["next"]
                url = None
            else:
                url = None
        workbook = Workbook()
        sheet = workbook.active
        header = ["name", "description", "url","project","created", "last udpate"]
        sheet.append(header)
        data_corte = datetime.strptime(self.created, '%d/%m/%Y')
        data_corte = data_corte.replace(tzinfo=pytz.UTC)
        for repo in repos_list:
            created_on = datetime.strptime(repo["created_on"], '%Y-%m-%dT%H:%M:%S.%f%z')
            updated_on = datetime.strptime(repo["updated_on"], '%Y-%m-%dT%H:%M:%S.%f%z')
            created = created_on.strftime('%d/%m/%Y')
            updated = updated_on.strftime('%d/%m/%Y')
            if created_on > data_corte:
                row = [
                    repo["name"],
                    repo.get("description", ""),
                    repo["links"]["html"]["href"],
                    repo["project"]["key"],
                    created,
                    updated
                ]
                sheet.append(row)
        workbook.save(filename="repo-created-recently.xlsx")
