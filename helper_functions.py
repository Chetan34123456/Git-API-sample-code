
# imports
import requests

# vars
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCIsImtpZCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCJ9.eyJhdWQiOiJodHRwczovL2FwaS5mYWJyaWMubWljcm9zb2Z0LmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2ZmMzU1Mjg5LTcyMWUtNGRkNy1hNjYzLWFmZWM2MmFiOWQ1NC8iLCJpYXQiOjE3MTgyMTY4MzUsIm5iZiI6MTcxODIxNjgzNSwiZXhwIjoxNzE4MjIxNzEyLCJhY2N0IjowLCJhY3IiOiIxIiwiYWlvIjoiQVlRQWUvOFdBQUFBdDZrUmhTK2xLYUR3ZXAyMWFFaHMyZUw3d1JqdGZVMkl1VHhwVklDelN3MEhJQ0RaNGw2RXhtcFloemZ0WDRKemMzNnQvTkZhUGRJTSt2ZGZBaTRRUE1iZ1RmMEE5dWpoUjE2eGlyc1hOTXlPWDZYSTFubS85R3E0VkdjNWlTSU55MWxpcWZqV3pIWENvVFlUZlVNcjRERGVnRTc2aWFWaWpuaWF5L0lEQ2xVPSIsImFtciI6WyJmaWRvIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZGV2aWNlaWQiOiI4MjY2ZGQwNi1kNWU1LTRjNjYtOTlkZS1lMmMyOTM5Y2QxODgiLCJmYW1pbHlfbmFtZSI6Ikhpd2FsZSIsImdpdmVuX25hbWUiOiJDaGV0YW4iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMzYuMjI2LjI1NS4xOSIsIm5hbWUiOiJDaGV0YW4gU3VuaWwgSGl3YWxlIiwib2lkIjoiNDA0OGRiMTgtZTcxOS00MzFjLWJhNzgtNTJjNjQ4MjRlMjIzIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTM4MjAzODE4MjQtOTE4MzM4NTAyLTEwNDQyOTQ0NTItMTQyNjExIiwicHVpZCI6IjEwMDMyMDAyRkQ2MjQyMUYiLCJyaCI6IjAuQVZVQWlWSTFfeDV5MTAybVk2X3NZcXVkVkFrQUFBQUFBQUFBd0FBQUFBQUFBQUNJQU0wLiIsInNjcCI6IkFwcC5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkV3JpdGUuQWxsIENvbnRlbnQuQ3JlYXRlIERhc2hib2FyZC5SZWFkLkFsbCBEYXNoYm9hcmQuUmVhZFdyaXRlLkFsbCBEYXRhZmxvdy5SZWFkLkFsbCBEYXRhZmxvdy5SZWFkV3JpdGUuQWxsIERhdGFzZXQuUmVhZC5BbGwgRGF0YXNldC5SZWFkV3JpdGUuQWxsIEdhdGV3YXkuUmVhZC5BbGwgR2F0ZXdheS5SZWFkV3JpdGUuQWxsIEl0ZW0uRXhlY3V0ZS5BbGwgSXRlbS5SZWFkV3JpdGUuQWxsIEl0ZW0uUmVzaGFyZS5BbGwgT25lTGFrZS5SZWFkLkFsbCBPbmVMYWtlLlJlYWRXcml0ZS5BbGwgUGlwZWxpbmUuRGVwbG95IFBpcGVsaW5lLlJlYWQuQWxsIFBpcGVsaW5lLlJlYWRXcml0ZS5BbGwgUmVwb3J0LlJlYWRXcml0ZS5BbGwgUmVwcnQuUmVhZC5BbGwgU3RvcmFnZUFjY291bnQuUmVhZC5BbGwgU3RvcmFnZUFjY291bnQuUmVhZFdyaXRlLkFsbCBUZW5hbnQuUmVhZC5BbGwgVGVuYW50LlJlYWRXcml0ZS5BbGwgVXNlclN0YXRlLlJlYWRXcml0ZS5BbGwgV29ya3NwYWNlLkdpdENvbW1pdC5BbGwgV29ya3NwYWNlLkdpdFVwZGF0ZS5BbGwgV29ya3NwYWNlLlJlYWQuQWxsIFdvcmtzcGFjZS5SZWFkV3JpdGUuQWxsIiwic2lnbmluX3N0YXRlIjpbImR2Y19tbmdkIiwiZHZjX2NtcCIsImlua25vd25udHdrIl0sInN1YiI6Ikk5VG95NHNobDBRQ29jQ0FDQ2l5eGF5UndYQS1mcmQweGFOWDlVQktRUEUiLCJ0aWQiOiJmZjM1NTI4OS03MjFlLTRkZDctYTY2My1hZmVjNjJhYjlkNTQiLCJ1bmlxdWVfbmFtZSI6IkNoZXRhbi4xMDczMjEyOUBMVElNaW5kdHJlZS5jb20iLCJ1cG4iOiJDaGV0YW4uMTA3MzIxMjlATFRJTWluZHRyZWUuY29tIiwidXRpIjoiRllOU2tXZGxVa0s4cnpRbEk1dXFBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il19.GhxTsTKbXDZdKZSAdkrFO8Oo56mvXcdNDihxOeyhSTPOyOAHD3xNac4QcdkNUSd0_6-rbEaziX95z5Wxp2zhnIE9OESwQFZcpOHB5Cv6SlYuFyLifcsLl5pSADvGDwOEDtGsvKSmCIbN1XfghBKsnPbJW0P4teRm7Bf54Adl3Ulw38AzYtvTiYW5obshSTnW7AZJHUpLfBxmvmG573ZNsQzrI9g7xF0DFZe3HAb2XTt-EQ4Fr0fXdw3uZvk9YZmqOp7qw-YZixb8MiHZE7ZnC9yjJi08Pa2XcN3nd0aAdHc5RJ8SJlvOHmrE756hHqXO13SEazqgiA6fvBfDZ46VCA'
headers={'Authorization':f'Bearer {token}', 'Content-type': 'application/json', 'retry-after': '60'}


def listWorkspace(workspace):
    url = 'https://api.fabric.microsoft.com/v1/admin/workspaces'
    try: 
        workspaceList = requests.get(url, headers = headers).json()
        print(workspaceList)
        for i in workspaceList :
            if i['displayName'] == workspace:
                workspaceId = i['id']
                workspaceName = i['displayName']

                return workspaceId, workspaceName
            else :
                return f"No workspace found with Name {workspaceName}"
    except Exception as e :
            return f'Function returned with exception : {e}'