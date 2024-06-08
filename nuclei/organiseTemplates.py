import os
import yaml
import shutil
import argparse
import sys
import textwrap

def usage():
    print("Examples:")
    print(f"\n[+] Provide file with `-i` flag containing `id` to exclude, one per line: \n\t- {sys.argv[0]} -dir /home/nuclei-templates -i ids.txt")
    print(f"\n[+] If you don't provide a file, It will exclude templates set by default:\n\t- {sys.argv[0]} -dir /home/nuclei-templates\n")

def get_ids_from_file(file_path):
    with open(file_path, 'r') as f:
        ids = f.read().splitlines()
    return ids

def move_matching_files(directory, ids, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as yaml_file:
                    try:
                        content = yaml.safe_load(yaml_file)
                        if 'id' in content and content['id'] in ids:
                            shutil.move(file_path, os.path.join(output_dir, file))
                            print(f"Moved: {file_path}")
                    except yaml.YAMLError as exc:
                        print(f"Error parsing {file_path}: {exc}")

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='Separate Nuclei Templates files based on ID match.', epilog=textwrap.dedent(f"""Examples:
[+] Provide file with `-i` flag containing `id` to exclude, one per line: 
\t- {sys.argv[0]} -dir /home/nuclei-templates -i ids.txt
[+] If you don't provide a file, It will exclude templates set by default:
\t- {sys.argv[0]} -dir /home/nuclei-templates"""))
    
    
    parser.add_argument('-dir', required=True, help='Directory containing Nuclei Templates files')
    parser.add_argument('-i', required=False, help='File containing nuclei template IDs to exclude, Example: tech-detect, missing-csp, display-via-header')
    
    args = parser.parse_args()
    
    if args.i and args.dir:
        ids = get_ids_from_file(args.i)
        move_matching_files(args.dir, ids, 'separated')
    elif args.dir:
        ids = ['display-via-header', 'missing-csp', 'tech-detect', 'http-missing-security-headers']
        move_matching_files(args.dir, ids, 'separated')        
    else: 
        print("Incorreect use of flags!")
        sys.exit(1)

if __name__ == "__main__":
    main()
