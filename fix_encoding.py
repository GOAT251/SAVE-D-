import os

def fix_file_encoding(filepath):
    try:
        # Read the file content
        with open(filepath, 'rb') as f:
            content = f.read()
        
        # Remove any null bytes
        content = content.replace(b'\x00', b'')
        
        # Write back with UTF-8 encoding
        with open(filepath, 'wb') as f:
            f.write(content)
        print(f"Successfully fixed encoding for {filepath}")
    except Exception as e:
        print(f"Error fixing {filepath}: {str(e)}")

# Fix the main files
fix_file_encoding('app.py')
fix_file_encoding(os.path.join('src', '__init__.py')) 