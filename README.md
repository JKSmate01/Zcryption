# Zcryption
Zcryption is a Python program designed to encrypt and decrypt files using password-protected zip archives. It utilizes various libraries and modules to perform these operations. Please follow the instructions below to use the program effectively.

# Prerequisites
Make sure you have the following libraries installed:

- pyzipper
- openpyxl
- shutil
- tqdm

You can install these libraries using the following commands:
```bash 
 pip install pyzipper
 pip install openpyxl
 pip install shutil
 pip install tqdm
```

# Usage
1. Clone or download the program files from the GitHub repository.
2. Open a terminal or command prompt and navigate to the program directory.
3. Run the program by executing the Zcryption.exe file.
4. The program will prompt you with three options:
 - - Encode (e): Encrypt files in the specified directory.
 - Decode (d): Decrypt files in the specified directory.
 - Delete All Data (delete): Delete all data in the list.
Choose the desired option by entering the corresponding command (e, d, or delete).

Depending on your selection, the program will perform the following actions:

Encode (e): Encrypt files in the specified directory and update the list.
Decode (d): Decrypt files in the specified directory using the passwords from the list.
Delete All Data (delete): Remove all data from the list.
For encryption, the program reads file information from an Excel file named list.xlsx located in the specified directory. The file should have the following columns:

Column A: File name
Column B: Description
Column C: Password
Column D: Destination file name (automatically updated by the program)
Column E: Indicator for extraction (automatically updated by the program)
The program creates password-protected zip archives for each file in the list, using the corresponding password and destination file name. It also updates the list with the encrypted file information.

For decryption, the program extracts files from the password-protected zip archives using the passwords from the list. If the extraction indicator is set to "x" for a file, it will be further extracted from the resulting zip archive.

Files that are not present in the list or do not have a corresponding password will not be processed.

The program saves any changes made to the list in the list.xlsx file.

Feel free to modify the program according to your specific requirements or extend its functionality as needed.
