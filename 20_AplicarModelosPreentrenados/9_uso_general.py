#%% packages
from transformers import pipeline

# %% proporciona la tarea
pipe = pipeline(task="text-classification")
# %% run pipe
pipe("Me gusta mucho.")
# %% modelo
pipe = pipeline(task="text-classification", 
                model="nlptown/bert-base-multilingual-uncased-sentiment")
# %% run pipe
# solo un string
pipe("Me gusta mucho.")

# %% consume a list
pipe(["Me gusta mucho.", 
      "Lo odio."])


# %%
