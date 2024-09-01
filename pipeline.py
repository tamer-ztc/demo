from transformers.pipelines import SUPPORTED_TASKS
from pprint import pprint
from transformers import pipeline,QuestionAnsweringPipeline


pprint(SUPPORTED_TASKS.keys())
#for k,v in SUPPORTED_TASKS.items():
#    print(k,v)

pipe = pipeline("text-classification")
pipe(["very good!","very bad"])
