# quick‑reverse‑cli

A one‑file Python utility that echoes the reverse of the input string.

## Usage

```sh
# Reverse a string passed as an argument
python reverse.py "hello world"
# => dlrow olleh

# Pipe data into the tool
echo "stack overflow" | python reverse.py
# => wolfrevO kcats
```

## Why tiny?
- No dependencies, just the Python stdlib.
- Ideal for quick one‑liners, scripts, or CI pipelines.
- Perfect for instant scaffolding demos.

## Installation
Copy `reverse.py` to a directory in your `$PATH` and make it executable:
```sh
chmod +x reverse.py
mv reverse.py /usr/local/bin/reverse
```
Now you can run `reverse "text"` directly.

---
*Created by TopherBot*