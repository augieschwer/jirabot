from jira import JIRA

options = {
            'server': 'https://foo.atlassian.net'
}
jira = JIRA(options)

jira = JIRA(basic_auth=('admin', 'admin'))

props = jira.application_properties()

issues = jira.search_issues('assignee=admin')

from collections import Counter
top_three = Counter(
            [issue.fields.project.key for issue in issues]).most_common(3)
