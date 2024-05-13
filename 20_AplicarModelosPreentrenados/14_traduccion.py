#%% packages
from transformers import pipeline



#%% translation
pipe = pipeline("traduccion_de")
pipe("The capital of France is Paris.")
# %%
