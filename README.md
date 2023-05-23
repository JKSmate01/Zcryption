# Zcryption
Zcryption is a Python program designed to **encrypt and decrypt** files using **password-protected zip archives**. Please follow the instructions below to use the program effectively.

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
1. **Download the zip from the releases tab.**
2. Run the program by executing the **Zcryption.exe** file.
3. The program will prompt you with three options:
   - **Encode (e): Encrypt files in the specified directory.**
   - **Decode (d): Decrypt files in the specified directory.**
   - **Delete All Data (delete): Delete all data in the list.**
4. Choose the desired option by entering the corresponding command **(e, d, or delete)**.
5. Depending on your selection, the program will perform the following actions:
   - **Encode (e): Encrypt files in the specified directory and update the list.**
   - **Decode (d): Decrypt files in the specified directory using the passwords from the list.**
   - **Delete All Data (delete): Remove all data from the list.**
- For encryption, the program reads file information from an Excel file named **list.xlsx** located in the specified directory. The file should have the following columns:
   - Column A: File name
   - Column B: Description
   - Column C: Password
   - Column D: Destination file name (automatically updated by the program)
   - Column E: Indicator for extraction (automatically updated by the program)

**DO NOT RENAME OR MODIFY THE 'list.xlsx' FILE!**

**FOR SAFETY DO NOT KEEP YOUR 'list.xlsx' FILE IN THE SAME FOLDER OR DIRECTORY. IF SOMEONE MANAGES TO STEAL THAT FILE THEY COULD DECRYPT ALL YOUR ZIP ARCHIVES!**

- The program creates **password-protected zip archives for each file** in the list, using the corresponding password and destination file name. It also updates the list with the encrypted file information.
- For **decryption**, the program **extracts files from the password-protected zip archives** **using** the passwords from **the list**.

Feel free to modify the program according to your specific requirements or extend its functionality as needed.

# Author
Zcryption is developed by Máté Jakus.
