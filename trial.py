import google.generativeai as genai

genai.configure(api_key="AIzaSyAeG9w6uCOg_MsyaRM1_Y9IuOoNqOGFEGQ")

models = genai.list_models()
for model in models:
    print(model.name)
