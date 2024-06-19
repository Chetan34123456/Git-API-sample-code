'''
---------------- Permissions ------------------
caller must have admin role

---------------- Scopes -----------------------
Workspace.ReadWrite.All
'''

#imports
import requests


# vars
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCIsImtpZCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCJ9.eyJhdWQiOiJodHRwczovL2FwaS5mYWJyaWMubWljcm9zb2Z0LmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2ZmMzU1Mjg5LTcyMWUtNGRkNy1hNjYzLWFmZWM2MmFiOWQ1NC8iLCJpYXQiOjE3MTg3MzQyOTMsIm5iZiI6MTcxODczNDI5MywiZXhwIjoxNzE4NzM5NjgwLCJhY2N0IjowLCJhY3IiOiIxIiwiYWlvIjoiQVpRQWEvOFhBQUFBVFlCeGFVSFg2bEs4MGEvUzFUak8rNlErKyswc0hxVDVONWRKdUNGSEMvOXoyL2w4TVp0L1lybU5rN1Y2TFUxT1BTbUVxRWtaeUxRekx0QmtYOFZTSmxWMDNOY1N0NEZTTjhJZHlkRzROMkI0VHpiUm1UTFBsU2tvUk85bnRJSU9ZUENYcDROaWN6T1EvUVlyRHhCalI1M3V3dlNjNkMxaEttdEpDRkJIdUYyeXRySjBrQzZ3TzV3dFhWbVQ2Nmh0IiwiYW1yIjpbInJzYSIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiODI2NmRkMDYtZDVlNS00YzY2LTk5ZGUtZTJjMjkzOWNkMTg4IiwiZmFtaWx5X25hbWUiOiJIaXdhbGUiLCJnaXZlbl9uYW1lIjoiQ2hldGFuIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTY1LjIyNS4xMjAuMjUxIiwibmFtZSI6IkNoZXRhbiBTdW5pbCBIaXdhbGUiLCJvaWQiOiI0MDQ4ZGIxOC1lNzE5LTQzMWMtYmE3OC01MmM2NDgyNGUyMjMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMzgyMDM4MTgyNC05MTgzMzg1MDItMTA0NDI5NDQ1Mi0xNDI2MTEiLCJwdWlkIjoiMTAwMzIwMDJGRDYyNDIxRiIsInJoIjoiMC5BVlVBaVZJMV94NXkxMDJtWTZfc1lxdWRWQWtBQUFBQUFBQUF3QUFBQUFBQUFBQ0lBTTAuIiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgSXRlbS5FeGVjdXRlLkFsbCBJdGVtLlJlYWRXcml0ZS5BbGwgSXRlbS5SZXNoYXJlLkFsbCBPbmVMYWtlLlJlYWQuQWxsIE9uZUxha2UuUmVhZFdyaXRlLkFsbCBQaXBlbGluZS5EZXBsb3kgUGlwZWxpbmUuUmVhZC5BbGwgUGlwZWxpbmUuUmVhZFdyaXRlLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBSZXBydC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuR2l0Q29tbWl0LkFsbCBXb3Jrc3BhY2UuR2l0VXBkYXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsiZHZjX21uZ2QiLCJkdmNfY21wIiwiaW5rbm93bm50d2siLCJrbXNpIl0sInN1YiI6Ikk5VG95NHNobDBRQ29jQ0FDQ2l5eGF5UndYQS1mcmQweGFOWDlVQktRUEUiLCJ0aWQiOiJmZjM1NTI4OS03MjFlLTRkZDctYTY2My1hZmVjNjJhYjlkNTQiLCJ1bmlxdWVfbmFtZSI6IkNoZXRhbi4xMDczMjEyOUBMVElNaW5kdHJlZS5jb20iLCJ1cG4iOiJDaGV0YW4uMTA3MzIxMjlATFRJTWluZHRyZWUuY29tIiwidXRpIjoiWlBwcFN4SDBLVUsyaEt6bjA1UmhBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19pZHJlbCI6IjEgMTYifQ.WbHvKIMcJ6txtyV9SWpZVsmP2H_WKFTbFpVylWSN3XsD2wvVxMk8PGHwtWBQQIzDEXscNbCDS4LPInakJkJaMJt67oq0vsupp2IxRtFJRqqaRcl4sjCObme8c9EedDeouthhaR9YSnD6fm9Med_htd0eAlMx8XuSI1nzMh2TheGBVIzm3X0N-jYSB7odaaZXOKvnOtkqLQDk__LkgcGu-MW6GyKXf8koXFTSphnu9suFIFyc8M7DpM7Apy7GK--X148WZOo-L0km07XRZ3_8bBnsKht2g_VQSVu5pAjmG1HaVC9ASEX0HbGWcpKLz6K-XE8k-TBY117HFIVRwdE40Q'
headers={'Authorization':f'Bearer {token}', 'Content-type': 'application/json', 'retry-after': '60'}


def connectToWorkspace(workspaceId : str):
    '''
    Only connects to Azure Devops Repo Branch to Fabric Workspace.
    Doesnt override or pull items from repo.
    Requires to sync items from Fabric Portal.
    
    params : str workspaceId -> workspace id of Fabric workspace
    '''
    url = f'https://api.fabric.microsoft.com/v1/workspaces/{workspaceId}/git/connect'

    config = {
            "gitProviderDetails": {
                "organizationName": "azuresunshine",
                "projectName": "CanvasSunshineProject",
                "gitProviderType": "AzureDevOps",
                "repositoryName": "Fabric_GITDemo",
                "branchName": "test_01",
                "directoryName": "test"
        }
    }

    response = requests.post(url=url, headers=headers, json=config)
    print(response.status_code)

    if response.status_code >= 400 :
        print(response.json()['errorCode'], response.json()['message'])

connectToWorkspace('9f06650a-4b74-42c4-bf0d-9cd7d5d6b140')
