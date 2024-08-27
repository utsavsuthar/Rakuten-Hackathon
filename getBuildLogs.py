# import jenkins

# jenkins_url = 'http://localhost:8080'
# username = 'sandhya'
# password = '1168eca84e5494dfd6fe656d5674d1880d'
# job_name = 'calculator'

# server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
# console_output = server.get_build_console_output(job_name, last_build_number)
# print(f'The last build ID for job \'{job_name}\' is {last_build_number}')
# print(console_output)


import jenkins
import os

# Jenkins server configuration
jenkins_url = 'http://localhost:8080'
username = 'sandhya'
password = '1168eca84e5494dfd6fe656d5674d1880d'
job_name = 'calculator'

# Initialize Jenkins server connection
server = jenkins.Jenkins(jenkins_url, username=username, password=password)

# Get last build number and console output
last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
output_info = server.get_build_console_output(job_name, last_build_number)

# Prepare output information
# output_info = f'The last build ID for job \'{job_name}\' is {last_build_number}\n'
# output_info = console_output

# Define directories for output files
dir1 = 'logs'
dir2 = 'new_logs'

# Create directories if they do not exist
os.makedirs(dir1, exist_ok=True)
os.makedirs(dir2, exist_ok=True)

# Define file paths
file_path_info = os.path.join(dir1, 'last_build_info.txt')
file_path_console = os.path.join(dir2, 'console_output.txt')

# Write last build info to the first file
with open(file_path_info, 'w') as file_info:
    file_info.write(output_info)

# Write console output to the second file
with open(file_path_console, 'w') as file_console:
    file_console.write(output_info)

# Print confirmation
print(f'Output written to {file_path_info} and {file_path_console}')
