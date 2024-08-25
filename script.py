import re

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

        # Check for errors or exceptions
        # error_match = error_pattern.search(line)
        # if error_match:
        #     log_details.append(line)
        #     if stages:
        #         output[-1] = f"Stage: {stages[-1]} - Status: FAILURE"
        #     continue

        # Check for skipped stages
        skipped_stage_match = skipped_stage_pattern.search(line)
        if skipped_stage_match:
            log_details.append(f"Skipped Stage: {skipped_stage_match.group(1)}\n")
            output.append(f"Skipped Stage: {skipped_stage_match.group(1)}")
            # log_details.append(line)
            continue

        # Check for pipeline success
        # if success_pattern.search(line):
        #     if stages:
        #         log_details.append(f"Stage: {stages[-1]} - Status: SUCCESS\n")
        #         output[-1] = f"Stage: {stages[-1]} - Status: SUCCESS"
        #     # log_details.append("Pipeline Status: SUCCESS\n")
        #     output.append("Pipeline Status: SUCCESS")
            # log_details.append(line)
            

        # Check for pipeline failure
        if failure_pattern.search(line):
            if stages:
                log_details.append(f"Stage: {stages[-1]} - Status: FAILURE\n")
                output[-1] = f"Stage: {stages[-1]} - Status: FAILURE"
            output.append("Pipeline Status: FAILURE")
            log_details.append(line)
            # break

        # Add other log details as they appear in the file
        # log_details.append(line)

    # Handle the last stage if it was not explicitly succeeded or failed
    if stages and ("Pipeline Status" not in output[-1]):
        last_stage_status = "SUCCESS" if success_pattern.search(log_data[-1]) else "FAILURE"
        output[-1] = f"Stage: {stages[-1]} - Status: {last_stage_status}"
        log_details.append(f"Stage: {stages[-1]} - Status: {last_stage_status}\n")

    return output, log_details

# File path
file_path = 'logs/#31.txt'

# Parse the log
pipeline_info, log_details = parse_pipeline_log(file_path)

# # Print the summary results
# for entry in pipeline_info:
#     print(entry)

# Write the detailed output to a file
output_file_path = 'parsed_pipeline_log.txt'
with open(output_file_path, 'w') as output_file:
    for entry in log_details:
        output_file.write(entry)
    output_file.write("\nSummary:\n")
    for entry in pipeline_info:
        output_file.write(entry + '\n')
