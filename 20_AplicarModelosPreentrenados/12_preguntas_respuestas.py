#%% packages
from transformers import pipeline



# %% Preguntas respuestas
pipe = pipeline("preguntas-respuestas")
pipe(context="Big Apple es un apodo para la Ciudad de Nueva York.", question="¿Qué es Big Apple?")

# %%
