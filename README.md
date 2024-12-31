# rag

## Submodules management

To create a repository on GitHub that includes multiple forked repositories as primary folders alongside your own development folder, while allowing you to easily fetch updates from the original repositories, follow these steps:

### Step 1: **Add Forked Repositories as Git Submodules**
1. Inside the cloned repository folder, add each forked repository as a submodule:
   ```bash
   git submodule add git@github.com:DavidAmat/Hands-On-Large-Language-Models.git repos/Hands-On-Large-Language-Models
   git submodule add git@github.com:DavidAmat/LLMs-from-scratch.git repos/LLMs-from-scratch

   ```

2. Initialize and update the submodules:
   ```bash
   git submodule update --init --recursive
   ```

---

### Step 2: **Add Your Development Folder**
1. Create a new folder for your developments:
   ```bash
   mkdir david
   ```
2. Add your own Python scripts, modules, or other files here.

3. Stage and commit the changes:
   ```bash
   git add .
   git commit -m "Add forked repos and development folder"
   git push origin main
   ```


## Install virtual environments

### Repo: Gentle Introduction to RAG
Source: https://github.com/svpino/gentle-intro-to-rag

Install requirements:

```bash
pyenv install 3.10.14
pyenv local 3.10.14

# Notation: b_ -> book // hollm: hands on llm
conda create --name r_ragintro python=3.10.14
conda activate r_ragintro
# conda env update --file environment.yml
pip install -r requirements.txt
python -m ipykernel install --user --name "kr_hollm"
```
