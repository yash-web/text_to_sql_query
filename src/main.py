import ollama 

oc =ollama.Client()

model="phi"
prompt="what is mcp"

resp=oc.generate(model=model,prompt=prompt)

print("Res",resp.response)

