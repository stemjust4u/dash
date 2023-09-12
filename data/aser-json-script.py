import json
import numpy as np 


example = [{
    'params': {'var1': 'value','var2': {'vvar1': 20,'vvar2': 3}},
    'model': 'path/to/file/model1.p',
    'graph_file': 'path/to/file/graph1.png',
    'assessment_accuracy': {},
    'question_accuracy': {}
    },
    {
    'params': {'var1': 'value','var2': {'vvar1': 5,'vvar2': 8}},
    'model': 'path/to/file/model2.p',
    'graph_file': 'path/to/file/graph2.png',
    'assessment_accuracy': {},
    'question_accuracy': {}
    }
]

for k in set('abcdefghijklmnop'):
    example[0]['question_accuracy'][k] = np.random.normal(20,3)
    example[1]['question_accuracy'][k] = np.random.normal(20,3)

for k in range(16):
    example[0]['assessment_accuracy'][k] = np.random.normal(5,8)
    example[1]['assessment_accuracy'][k] = np.random.normal(5,8)

#with open('/home/chawn1272/Desktop/aser_example_output.json', 'w') as outfile:
#    json.dump(example, outfile)

parm1 = example[0]['params']
model = example[0]['model']
graphfile = example[0]['graph_file']
for parm, item in example[0].items():
    if isinstance(item, dict):
        for key in item:
            print("{0}, {1}, {2}, {3}, {4}".format(parm1, model, graphfile, key, item[key]))