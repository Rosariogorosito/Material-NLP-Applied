#%% packages
from transformers import pipeline

# %% reconocimiento entidades nombradas
pipe = pipeline(task="ner")
pipe("Apple Inc. fue fundada por Steve Jobs, Steve Wozniak y Ronald Wayne el 1 de abril de 1976, en Cupertino, California.")


# %%
