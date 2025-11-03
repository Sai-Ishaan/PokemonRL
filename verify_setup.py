### Verify all dependencies are installed correctly
## verify_setup.py

import sys
import importlib.metadata

def check_module(name, display_name=None):
    display_name = display_name or name
    
    try:
        mod = importlib.import_module(name)
        try:
            version = importlib.metadata.version(name)
        except:
            version = "installed"
        print(f"{display_name}: {version}")
        return True
    except ImportError:
            print(f"{display_name}: NOT INSTALLED!!")
            return False
        
def main():
    print("=" * 60)
    print("PokemonRL Training Environment - Installation Verification")
    print("=" * 60)
    
    print(f"\nPython Version: {sys.version.split()[0]}")
    print(f"Python Executable: {sys.executable}\n")
    
    modules = [
        ("poke_env", "poke-env"),
        ("numpy", "numpy"),
        ("gymnasium", "gymnasium"),
        ("stable_baselines3", "stable-baselines3"),
        ("torch", "torch"),
        ("pandas", "pandas"),
        ("matplotlib", "matplotlib"),
        ("tensorboard", "tensorboard"),
    ]
    
    results = []
    for mod_name, display_name in modules:
        results.append(check_module(mod_name, display_name))
    
    print("\n" + "="*60)
    success_count = sum(results)
    total_count = len(results)
    
    if success_count == total_count:
        print(f"Success: All {total_count} dependencies installed!!")
        print("\n Environment is ready for PokemonRL Training!!!")
    else:
        print(f" Warning!!! : {total_count - success_count} dependencies missing")
        
    print("=" * 60)
    return success_count == total_count

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success  else 1)
            