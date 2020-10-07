from azureml.core import Workspace,Datastore,Dataset
from azureml.core.experiment import Experiment
from azureml.pipeline.core import Pipeline,PipelineData
from azureml.pipeline.steps import PythonScriptStep
ws= Workspace.from_config(path="./file-path/ws_config.json")
experiment = Experiment(workspace=ws, name='BrainStar')
def_blob_store = Datastore(ws, "workspaceblobstore")
compute_target = ws.compute_targets["BrainStar1"]
input_data=Dataset.get(ws,name="Absence data")
output_data1 = PipelineData("output_data1",datastore=def_blob_store,output_name="output_data1")
source_directory = './process'
step1 = PythonScriptStep(name="process_step",
                         script_name="process.py",
                         inputs=[input_data],
                         outputs=[output_data1],
                         compute_target=compute_target, 
                         source_directory=source_directory,
                         allow_reuse=True)

steps=step1
pipeline1 = Pipeline(workspace=ws, steps=steps)
pipeline1.validate()
pipeline_run1 = Experiment(ws, 'Hello_World1').submit(pipeline1, regenerate_outputs=False)

