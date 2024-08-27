import re
import os
import csv
import uuid
def generate_random_filename(extension='txt'):
    return f"{uuid.uuid4().hex}.{extension}"

def parse_pipeline_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.readlines()

    output = []
    stages = []
    log_details = []
    in_exception = False

    # Regex patterns
    stage_start_pattern = re.compile(r'\[\s*Pipeline\s*\]\s*stage')
    stage_details_pattern = re.compile(r'\[\s*Pipeline\s*\]\s*\{\s*\((.*?)\)')

    error_pattern = re.compile(r'ERROR|Error:')
    exception_pattern = re.compile(r'(Exception:)',re.IGNORECASE)
    skipped_stage_pattern = re.compile(r'Stage "(.*?)" skipped due to earlier failure\(s\)')
    success_pattern = re.compile(r'BUILD SUCCESS|Finished: SUCCESS', re.IGNORECASE)
    failure_pattern = re.compile(r'BUILD FAILURE|Finished: FAILURE', re.IGNORECASE)

    for i, line in enumerate(log_data):
        # Handle exception blocks
        if 'omitted' in line:
            in_exception = False

        if in_exception:
            # Continue collecting lines as part of the exception stack trace
            log_details.append(line)

            # Check if we encounter a new error or success message
            if error_pattern.search(line) or success_pattern.search(line) or failure_pattern.search(line):
                in_exception = False  # Stop collecting on new message

        elif exception_pattern.search(line):
            log_details.append(line)
            in_exception = True  # Start collecting the exception stack trace
        elif error_pattern.search(line):
            log_details.append(line)
        elif success_pattern.search(line) or failure_pattern.search(line):
            log_details.append(line)

        # Check for stage start
        if stage_start_pattern.search(line):
            if i + 1 < len(log_data):  # Ensure there's a next line
                next_line = log_data[i + 1]
                # Check if the next line matches the stage details
                stage_match = stage_details_pattern.search(next_line)
                if stage_match:
                    stage_name = stage_match.group(1)
                    stages.append(stage_name)
                    if len(stages) > 1:
                        log_details.append(f"Stage: {stages[-2]} - Status: SUCCESS\n")
                        output.append(f"Stage: {stages[-2]} - Status: SUCCESS")
                    output.append(f"Stage: {stage_name} - Status: IN PROGRESS")   # Add stage start line
                    log_details.append(next_line)  # Add stage detail line
                    continue
 

        # Check for skipped stages
        skipped_stage_match = skipped_stage_pattern.search(line)
        if skipped_stage_match:
            log_details.append(f"Skipped Stage: {skipped_stage_match.group(1)}\n")
            output.append(f"Skipped Stage: {skipped_stage_match.group(1)}")
            # log_details.append(line)
            continue

        # Check for pipeline failure
        if failure_pattern.search(line):
            if stages:
                log_details.append(f"Stage: {stages[-1]} - Status: FAILURE\n")
                output[-1] = f"Stage: {stages[-1]} - Status: FAILURE"
            output.append("Pipeline Status: FAILURE")
            log_details.append(line)
            # break


    # Handle the last stage if it was not explicitly succeeded or failed
    if stages and ("Pipeline Status" not in output[-1]):
        last_stage_status = "SUCCESS" if success_pattern.search(log_data[-1]) else "FAILURE"
        output[-1] = f"Stage: {stages[-1]} - Status: {last_stage_status}"
        log_details.append(f"Stage: {stages[-1]} - Status: {last_stage_status}\n")

    return output, log_details












# Directory containing log files
# log_directory = 'logs'

# # Output CSV file path
# csv_output_file = 'parsed_pipeline_logs.csv'

# # Initialize a list to hold all rows
# csv_rows = []

# # Initialize a global index counter
# global_index = 1

# # Read all log files from the directory
# for log_file in os.listdir(log_directory):
#     log_file_path = os.path.join(log_directory, log_file)
    
#     # Skip non-log files (only process .txt files)
#     if not log_file.endswith('.txt'):
#         continue
    
#     # Parse the log file
#     _, log_details = parse_pipeline_log(log_file_path)
    
#     # Combine all log details into a single string
#     combined_log_details = ''.join(log_details).strip()
    
#     # Add a single row for the current file
#     csv_rows.append([global_index, combined_log_details])
    
#     # Increment the global index for the next file
#     global_index += 1

# # Write to CSV
# with open(csv_output_file, 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(['Index', 'Description'])  # Write header
#     csv_writer.writerows(csv_rows)

# print(f"Log details have been written to {csv_output_file}")