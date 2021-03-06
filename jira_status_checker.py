
from operator import truediv
from jira import JIRA
import os
import warnings
import sys

jira_id = sys.argv[1]
jira_base_url = os.environ.get("JIRA_BASE_URL")
username = os.environ.get("JIRA_USER_LOCAL")
apikey = os.environ.get("JIRA_TOKEN_LOCAL")

jira = JIRA(options = {'server':jira_base_url, 'verify':False}, basic_auth = (username, apikey))
singleIssue = jira.issue(jira_id)
jira_status = str(singleIssue.fields.status)
if jira_status in ["To Do", "Done"]:
  print("invalid")
elif jira_status in ["In Progress"]:
  print("valid")
else:
  print("Didn't find the JIRA status")
