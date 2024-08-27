
import jenkins
import os
import subprocess
from Scripts.script import parse_pipeline_log, generate_random_filename
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

dir2 = 'new_logs'

# Create directories if they do not exist
os.makedirs(dir2, exist_ok=True)

# Define file paths
file_path_console = os.path.join(dir2, 'console_output.txt')

# Write console output to the second file
with open(file_path_console, 'w') as file_console:
    file_console.write(output_info)

# File path
file_path = 'new_logs/console_output.txt'

# Parse the log
pipeline_info, log_details = parse_pipeline_log(file_path)



# Example usage
filename = generate_random_filename('txt')

# Define directories for output files
dir1 = 'DataSet'
dir2 = 'ParsedLogs'
# Write the detailed output to a file
os.makedirs(dir1, exist_ok=True)
os.makedirs(dir2, exist_ok=True)

file_path_info = os.path.join(dir1, filename)
file_path_console = os.path.join(dir2, 'summ_log.txt')

# # Write last build info to the first file


with open(file_path_info, 'w') as output_file:
    for entry in log_details:
        output_file.write(entry)
   
with open(file_path_console, 'w') as output_file:
    for entry in log_details:
        output_file.write(entry)

# command = ['streamlit','run','frontend.py']
subprocess.run(["streamlit", "run", "frontend.py"])