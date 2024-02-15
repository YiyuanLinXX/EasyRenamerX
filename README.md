# EasyRenamerX

Author: [Yiyuan Lin](yl3663@cornell.edu)

EasyRenamerX is a simple but effective Python script designed to automate the renaming of files and folders within a specified directory. It replaces spaces with underscores and capitalizes titles, excluding prepositions, to ensure a clean, consistent naming convention.



## Features

- **Space to Underscore Conversion**: Automatically replaces spaces with underscores in file and folder names.
- **Selective Capitalization**: Capitalizes the first letter of each word except for prepositions, providing a more readable and standardized format.
- **Recursive Renaming**: Works through the specified directory, including all subdirectories and files, ensuring a comprehensive renaming process.
- **Customizable Directory Selection**: Allows users to specify the target directory or defaults to the directory where the script is located.



## Installation

To use EasyRenamerX, you need Python installed on your system. The script is compatible with Python 3.x versions. Clone or download this repository to your local machine to get started.

```bash
git clone https://github.com/YiyuanLinXX/EasyRenamerX.git
cd EasyRenamerX
```

No additional Python packages are required to run this script.



## Usage

To run EasyRenamerX, navigate to the script's directory in your terminal or command prompt, and execute the following command:

```bash
python EasyRenamerX.py --root_dir 'path/to/your/directory'
```

**NOTE: If you do not specify the `--root_dir` argument, the script will default to renaming files and folders in the script's current directory.**



## Limitations

- The script does not undo the renaming operation. Ensure you have backups or are sure about proceeding with the renaming.
- Customizing prepositions or additional naming rules in terminal or interactive interface is not supported in the current version, but you can modify the code with your specific rules.





## Contributing

Contributions to EasyRenamerX are welcome. Please feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue in the repository.