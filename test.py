#from transformers import AutoModelForCausalLM
#from transformers import AutoTokenizer
import torch
import torchvision
#model_path=r"C:\\Users\\ken50\\OneDrive\\桌面\\GPTQ-for-LLaMa\\llama-7b\\"
#model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16)
#tokenizer = AutoTokenizer.from_pretrained(model_path, torch_dtype=torch.float16)

print(torchvision.__version__)
print(torch.version.cuda)

print(torch.cuda.is_available())