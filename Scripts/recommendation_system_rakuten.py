
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt


import tensorflow as tf
import tensorflow_hub as hub

# Load the Universal Sentence Encoder model from TensorFlow Hub
# model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
# model = hub.load(model_url)


model = tf.saved_model.load("Scripts/encoder_model")

def embed(texts):
    return model(texts)

print("Universal Sentence Encoder model loaded successfully.")

df = pd.read_csv("Incidents/Incidents.csv")
df = df.fillna('')
# print(df.head())

# df = pd.concat([df1, df2,df3,df4,df5,df6], ignore_index=True)
# print(df.shape)
# df.head()

df = df[['Incident Number','Company Name','Problem Title','Incident Severity','Error Description','Solution']]
# df['Title_Description'] = df['Title'] + df['Description']
# df = df[['Name', 'City']]
print(df.head())

# df.to_csv('data.csv', index=True)


Description = df['Error Description']
# Description[0]

embeddings = embed(Description)
# embeddings.shape

pca = PCA(n_components=2)
pca_result = pca.fit_transform(embeddings)


plt.figure(figsize=(10, 8))
plt.scatter(pca_result[:, 0], pca_result[:, 1])
# plt.show()

nn = NearestNeighbors(n_neighbors=5)
nn.fit(embeddings)

# yt_url = "https://www.youtube.com/watch?v="
# def process(url):
#   return yt_url + url

def recommend(text):
    emd = embed([text])
    # idx = df[df['Title'] == title].index[0]
    neighbours = nn.kneighbors(emd, return_distance=False)[0]

    results = df['Problem Title'].iloc[neighbours].tolist()

    return results

# recommend('different types of mutual funds')

output = recommend('''Started by user Sandhya
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /Users/sandhyas/.jenkins/workspace/Calculator
[Pipeline] {
[Pipeline] tool
Unpacking https://repo1.maven.org/maven2/org/sonarsource/scanner/cli/sonar-scanner-cli/6.1.0.4477/sonar-scanner-cli-6.1.0.4477.zip to /Users/sandhyas/.jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonar-scanner on Jenkins
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Tool Install)
[Pipeline] tool
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Also:   org.jenkinsci.plugins.workflow.actions.ErrorAction$ErrorId: 8907d3fb-23fb-4ef7-8b14-d54f114f58ad
java.io.IOException: Unable to locate binary. A release might not exist for the selected combination. ID: jdk8u422-b05.1, Platform: MACOS, CPU: arm
	at PluginClassLoader for adoptopenjdk//io.jenkins.plugins.adoptopenjdk.AdoptOpenJDKInstaller.performInstallation(AdoptOpenJDKInstaller.java:117)
	at hudson.tools.InstallerTranslator.getToolHome(InstallerTranslator.java:70)
	at hudson.tools.ToolLocationNodeProperty.getToolHome(ToolLocationNodeProperty.java:109)
	at hudson.tools.ToolInstallation.translateFor(ToolInstallation.java:221)
	at hudson.model.JDK.forNode(JDK.java:150)
	at hudson.model.JDK.forNode(JDK.java:60)
	at PluginClassLoader for workflow-basic-steps//org.jenkinsci.plugins.workflow.steps.ToolStep$Execution.run(ToolStep.java:157)
	at PluginClassLoader for workflow-basic-steps//org.jenkinsci.plugins.workflow.steps.ToolStep$Execution.run(ToolStep.java:138)
	at PluginClassLoader for workflow-step-api//org.jenkinsci.plugins.workflow.steps.SynchronousNonBlockingStepExecution.lambda$start$0(SynchronousNonBlockingStepExecution.java:47)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:572)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:317)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
	at java.base/java.lang.Thread.run(Thread.java:1583)
Finished: FAILURE''')

print(output)