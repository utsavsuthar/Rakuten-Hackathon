import jenkins

jenkins_url = 'http://localhost:8080'
username = 'sandhya'
password = '1168eca84e5494dfd6fe656d5674d1880d'
job_name = 'calculator'

server = jenkins.Jenkins(jenkins_url, username=username, password=password)

last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
console_output = server.get_build_console_output(job_name, last_build_number)
print(f'The last build ID for job \'{job_name}\' is {last_build_number}')
print(console_output)
