# Compiling it yourself
So, you're a brave human (or bot, I don't really know) who is willing to compile Orange themselves. There are multiple reasons you might want to compile it yourself. Maybe you just added some changes and want to compile or maybe you just want to try it out to see how it works.

## Step 1: Cloning the repository
First, install Git from this link: https://git-scm.com/downloads. Then, clone the repository using this command:
```bash
git clone https://github.com/TechStudent11/Orange.git
```

Then:
```bash
cd Orange
```

## Virtual Environments (Optional)
So this step is optional, however it is recommended. Creating a virtual environment isolates the dependencies to one project.

### Windows
First you need to run:
```bash
pip install virtualenv
```
Next, to create it:
```bash
virtualenv venv
```

Then to activate it:
```
"venv/Scripts/activate"
```

### Linux/MacOS
Creating a virtual environment in Linux or MacOS comes included with Python. All  you have to run is:
```bash
python -m venv venv
```

Then to activate it:
```
source "venv/bin/activate"
```

## Step 2: Dependencies
To install all of the dependencies, make sure you are in the root directory. Then run:
```bash
pip install -r requirements.txt
```

## Step 3: Compiling
To compile Orange, you have to use the `auto-py-to-exe` library, which was installed using the command above.

So to run:
```bash
auto-py-to-exe -c pyinstaller.json
```

When the window opens up, click "Convert .PY to .EXE" and it should compile.

## Done!
You have now compiled Orange!
