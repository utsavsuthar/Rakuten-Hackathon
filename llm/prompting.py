from llama_index.llms.groq import Groq

def prompt(ex_2):

    llm_groq = Groq(model="llama3-70b-8192", api_key="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")

    ex_1 = '''
    We will be providing the cicd pipeline error logs in the 'Input'. You task is to provide four things including an error title,  detailed description of the error, solution of the error and the severity of the error. Some examples of 'Input' and
    'Analysis' are given. Like that complete for the other errors. 
    Input: [Pipeline] { (Declarative: Tool Install)
    Stage: Declarative: Tool Install - Status: SUCCESS
    [Pipeline] { (Git-Checkout)
    Stage: Git-Checkout - Status: SUCCESS
    [Pipeline] { (Compile)
    [INFO] BUILD SUCCESS
    Stage: Compile - Status: SUCCESS
    [Pipeline] { (Build)
    [INFO] BUILD SUCCESS
    Stage: Build - Status: SUCCESS
    [Pipeline] { (Test)
    [INFO] BUILD SUCCESS
    Stage: Test - Status: SUCCESS
    [Pipeline] { (Sonar-Analytics)
    Stage: Sonar-Analytics - Status: SUCCESS
    [Pipeline] { (Docker Build & Tag)
    Stage: Docker Build & Tag - Status: SUCCESS
    [Pipeline] { (Trivy Image Scan)
    Skipped Stage: Trivy Image Scan
    Stage: Trivy Image Scan - Status: SUCCESS
    [Pipeline] { (Docker Push Image)
    Skipped Stage: Docker Push Image
    Stage: Docker Push Image - Status: SUCCESS
    [Pipeline] { (Deploy)
    Skipped Stage: Deploy
    java.io.IOException: error=2, No such file or directory
        at java.base/java.lang.ProcessImpl.forkAndExec(Native Method)
        at java.base/java.lang.ProcessImpl.<init>(ProcessImpl.java:295)
        at java.base/java.lang.ProcessImpl.start(ProcessImpl.java:225)
        at java.base/java.lang.ProcessBuilder.start(ProcessBuilder.java:1126)
    Also:   org.jenkinsci.plugins.workflow.actions.ErrorAction$ErrorId: e5b5e541-4bb4-4b23-adbe-a6b00650d70a
    Caused: java.io.IOException: Cannot run program "docker": error=2, No such file or directory
        at java.base/java.lang.ProcessBuilder.start(ProcessBuilder.java:1170)
        at java.base/java.lang.ProcessBuilder.start(ProcessBuilder.java:1089)
        at hudson.Proc$LocalProc.<init>(Proc.java:252)
        at hudson.Proc$LocalProc.<init>(Proc.java:221)
        at hudson.Launcher$LocalLauncher.launch(Launcher.java:994)
        at hudson.Launcher$ProcStarter.start(Launcher.java:506)
        at hudson.Launcher$ProcStarter.join(Launcher.java:517)
        at PluginClassLoader for docker-commons//org.jenkinsci.plugins.docker.commons.impl.RegistryKeyMaterialFactory.materialize(RegistryKeyMaterialFactory.java:102)
        at PluginClassLoader for docker-workflow//org.jenkinsci.plugins.docker.workflow.AbstractEndpointStepExecution2.doStart(AbstractEndpointStepExecution2.java:53)
        at PluginClassLoader for workflow-step-api//org.jenkinsci.plugins.workflow.steps.GeneralNonBlockingStepExecution.lambda$run$0(GeneralNonBlockingStepExecution.java:77)
        at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:572)
        at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:317)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
        at java.base/java.lang.Thread.run(Thread.java:1583)
    Finished: FAILURE
    Stage: Deploy - Status: FAILURE
    Finished: FAILURE
    Analysis:
    File Missing:
    Detailed Description: The Jenkins CI/CD pipeline log provided shows that several stages of the pipeline were executed successfully, including stages like "Tool Install," "Git-Checkout," "Compile," "Build," "Test," "Sonar-Analytics," and "Docker Build & Tag." However, the pipeline encountered issues during the "Deploy" stage, leading to a failure.
    Primary Error: The main error occurred during the "Deploy" stage when Jenkins tried to run a process that required Docker.
    The specific error message is: java.io.IOException: Cannot run program "docker": error=2, No such file or directory.
    This error indicates that Jenkins attempted to execute the docker command, but the command was not found, meaning Docker is either not installed on the agent executing the pipeline, or the path to the Docker executable is not correctly set.
    Severity: High
    Possible Solutions: Check Docker Installation: Ensure that Docker is installed on the Jenkins agent or server where the pipeline is executed. You can check this by running docker --version on the command line of the Jenkins agent. If Docker is not installed, install it according to your system's package management guidelines.
    Set Docker Path: If Docker is installed but the error persists, it may be due to an incorrect or missing path to the Docker executable. Ensure that the path to the Docker binary is included in the system’s PATH environment variable.

    Input: [Pipeline] { (Declarative: Tool Install)
    Stage: Declarative: Tool Install - Status: SUCCESS
    [Pipeline] { (Git-Checkout)
    Stage: Git-Checkout - Status: SUCCESS
    [Pipeline] { (Compile)
    [INFO] BUILD SUCCESS
    Stage: Compile - Status: SUCCESS
    [Pipeline] { (Build)
    [INFO] BUILD SUCCESS
    Stage: Build - Status: SUCCESS
    [Pipeline] { (Test)
    [INFO] BUILD SUCCESS
    Stage: Test - Status: SUCCESS
    [Pipeline] { (Sonar-Analytics)
    21:42:28.195 ERROR Error during SonarScanner CLI execution
    java.lang.IllegalStateException: Failed to upload report: Error 500 on http://localhost:9000/api/ce/submit?projectKey=SIPCalculator&projectName=Blogging-app : {"errors":[{"msg":"An error has occurred. Please contact your administrator"}]}
        at org.sonar.scanner.report.ReportPublisher.upload(ReportPublisher.java:226)
        at org.sonar.scanner.report.ReportPublisher.execute(ReportPublisher.java:154)
        at org.sonar.scanner.scan.SpringProjectScanContainer.doAfterStart(SpringProjectScanContainer.java:376)
        at org.sonar.core.platform.SpringComponentContainer.startComponents(SpringComponentContainer.java:188)
        at org.sonar.core.platform.SpringComponentContainer.execute(SpringComponentContainer.java:167)
        at org.sonar.scanner.bootstrap.SpringGlobalContainer.doAfterStart(SpringGlobalContainer.java:137)
        at org.sonar.core.platform.SpringComponentContainer.startComponents(SpringComponentContainer.java:188)
        at org.sonar.core.platform.SpringComponentContainer.execute(SpringComponentContainer.java:167)
        at org.sonar.batch.bootstrapper.Batch.doExecute(Batch.java:72)
        at org.sonar.batch.bootstrapper.Batch.execute(Batch.java:66)
        at org.sonarsource.scanner.lib.internal.batch.BatchIsolatedLauncher.execute(BatchIsolatedLauncher.java:41)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.base/java.lang.reflect.Method.invoke(Method.java:568)
        at org.sonarsource.scanner.lib.internal.IsolatedLauncherProxy.invoke(IsolatedLauncherProxy.java:62)
        at jdk.proxy3/jdk.proxy3.$Proxy2.execute(Unknown Source)
        at org.sonarsource.scanner.lib.InProcessScannerEngineFacade.doAnalyze(InProcessScannerEngineFacade.java:39)
        at org.sonarsource.scanner.lib.Scann erEngineFacade.analyze(ScannerEngineFacade.java:61)
        at org.sonarsource.scanner.cli.Main.analyze(Main.java:77)
        at org.sonarsource.scanner.cli.Main.main(Main.java:63)
    Caused by: org.sonarqube.ws.client.HttpException: Error 500 on http://localhost:9000/api/ce/submit?projectKey=SIPCalculator&projectName=Blogging-app : {"errors":[{"msg":"An error has occurred. Please contact your administrator"}]}
        at org.sonarqube.ws.client.BaseResponse.failIfNotSuccessful(BaseResponse.java:36)
        at org.sonar.scanner.bootstrap.DefaultScannerWsClient.failIfUnauthorized(DefaultScannerWsClient.java:126)
        at org.sonar.scanner.bootstrap.DefaultScannerWsClient.call(DefaultScannerWsClient.java:89)
        at org.sonar.scanner.report.ReportPublisher.upload(ReportPublisher.java:224)
    21:42:28.197 ERROR 
    21:42:28.197 ERROR Re-run SonarScanner CLI using the -X switch to enable full debug logging.
    Stage: Sonar-Analytics - Status: SUCCESS
    [Pipeline] { (Deploy)
    Skipped Stage: Deploy
    ERROR: script returned exit code 1
    Finished: FAILURE
    Stage: Deploy - Status: FAILURE
    Finished: FAILURE
    Analysis: 
    SonarQube Internal Issue:
    Detailed Description: The provided Jenkins CI/CD pipeline logs show a sequence of events where various stages were executed. The issue arose during the "Sonar-Analytics" stage, leading to the eventual failure of the pipeline.
    Key Observations: Sonar-Analytics Stage Error:

    The error occurred during the "Sonar-Analytics" stage, specifically when the SonarScanner attempted to upload a report to the SonarQube server. The error response from the server included a message: {"errors":[{"msg":"An error has occurred. Please contact your administrator"}]}, which suggests that there is an internal issue on the SonarQube server side.
    Severity: Medium
    Possible Solution: Ensure Proper Configuration: Verify that the SonarQube server is properly configured, including settings related to memory allocation, database connections, and the number of worker threads.
    Upgrade or Reconfigure Resources: If the server is under heavy load, consider upgrading the hardware or adjusting the server’s configuration to better handle the load.

    Input: [Pipeline] { (Declarative: Tool Install)
    Stage: Declarative: Tool Install - Status: SUCCESS
    [Pipeline] { (Git-Checkout)
    Stage: Git-Checkout - Status: SUCCESS
    [Pipeline] { (Compile)
    [INFO] BUILD SUCCESS
    Stage: Compile - Status: SUCCESS
    [Pipeline] { (Build)
    [INFO] BUILD SUCCESS
    Stage: Build - Status: SUCCESS
    [Pipeline] { (Test)
    [INFO] BUILD SUCCESS
    Stage: Test - Status: SUCCESS
    [Pipeline] { (Sonar-Analytics)
    Stage: Sonar-Analytics - Status: SUCCESS
    [Pipeline] { (Deploy)
    Error: Unable to access jarfile your-jar-file-name.jar
    ERROR: script returned exit code 1
    Finished: FAILURE
    Stage: Deploy - Status: FAILURE
    Finished: FAILURE

    Analysis: 
    Jar File Not Found:
    Detailed Description: The provided Jenkins CI/CD pipeline logs show that the pipeline was successfully executed up until the "Deploy" stage, where it encountered a failure.
    Key Observations: This error indicates that the pipeline is trying to execute or access a JAR file named your-jar-file-name.jar, but Jenkins cannot find or access this file. This could be due to several reasons:
    The JAR file might not have been generated or might be located in a different directory than expected.
    The file path specified in the pipeline script might be incorrect.
    The file might have been deleted or moved during an earlier stage.
    Severity: Low
    Possible Solutions: Correct the File Path: If the JAR file is in a different directory, update the pipeline script to point to the correct path. For example, if the JAR file is located in a target/ directory, ensure the pipeline uses target/your-jar-file-name.jar instead of just your-jar-file-name.jar.
    Use Dynamic Path Resolution: Consider using environment variables or Jenkins workspace variables to dynamically reference the correct path to the JAR file, making the pipeline more robust.
    Check File Permissions:

    Verify Permissions: Ensure that the Jenkins agent has the necessary permissions to access the JAR file. If the file permissions are restrictive, Jenkins may be unable to read or execute the file.

    Input: [Pipeline] { (Declarative: Tool Install)
    Stage: Declarative: Tool Install - Status: SUCCESS
    [Pipeline] { (Git-Checkout)
    Stage: Git-Checkout - Status: SUCCESS
    [Pipeline] { (Compile)
    [INFO] BUILD SUCCESS
    Stage: Compile - Status: SUCCESS
    [Pipeline] { (Test)
    [INFO] BUILD SUCCESS
    Stage: Test - Status: SUCCESS
    [Pipeline] { (Sonar-Analytics)
    Stage: Sonar-Analytics - Status: SUCCESS
    [Pipeline] { (Build)
    [INFO] BUILD SUCCESS
    Stage: Build - Status: SUCCESS
    [Pipeline] { (Docker Build & Tag)
    Stage: Docker Build & Tag - Status: SUCCESS
    [Pipeline] { (Docker Push Image)
    Stage: Docker Push Image - Status: SUCCESS
    [Pipeline] { (Deploy)
    Finished: SUCCESS
    Stage: Deploy - Status: SUCCESS
    Analysis: 
    Success Run:
    Detailed Description: The provided Jenkins CI/CD pipeline logs indicate that the entire pipeline has executed successfully, with no errors reported.
    Severity: None
    Possible Solutions: No fixes are required
    '''


    response = llm_groq.complete(prompt = ex_1+"\n\nInput: " + ex_2 + "\n" + "Analysis: ")

    return response