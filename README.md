# File Renamer Executable Guide

This guide explains how to use the `file_renamer.exe` application to batch rename files with optional prefixes, suffixes, and middle parts.

## Features
1. **Select Files to Rename**:
   - Click on the "Select Files" button.
   - In the file dialog that appears, select the files you want to rename and click "Open".
   - The selected files will be listed in the box below.

2. **Enter Prefix (Optional)**:
   - In the "Prefix" field, enter a prefix you want to add to the file names.
   - The prefix will automatically have an underscore `_` added after it.

3. **Enter Suffix (Optional)**:
   - In the "Suffix" field, enter a suffix you want to add to the file names.
   - The suffix will automatically have an underscore `_` added before it.

4. **Enter Middle Part (Optional)**:
   - In the "Replace middle with" field, enter the text you want to replace the middle part of the file names with.
   - This is optional and can be left blank if not needed.

5. **Keep Original File Name (Optional)**:
   - Check the "Keep original file name" box if you want to keep the original file names and just add the prefix and/or suffix.
   - **Note**: If this option is checked, you cannot enter a middle part. If you try to do so, an error message will appear.

6. **Rename Files**:
   - Click the "Rename Files" button to rename the selected files with the specified changes.
   - The renamed files will be listed in the box below, and a message will indicate that the files have been renamed.

## Example Scenarios

### Scenario 1: Adding a Prefix

- **Original File Name**: `example.png`
- **Prefix**: `Prefix_`
- **Result**: `Prefix_example.png`

### Scenario 2: Adding a Suffix

- **Original File Name**: `example.png`
- **Suffix**: `_Suffix`
- **Result**: `example_Suffix.png`

### Scenario 3: Replacing the Middle Part

- **Original File Name**: `example.png`
- **Middle Part**: `middle`
- **Result**: `middle.png`

### Scenario 4: Adding Prefix, Suffix, and Middle Part

- **Original File Name**: `example.png`
- **Prefix**: `Prefix_`
- **Middle Part**: `middle`
- **Suffix**: `_Suffix`
- **Result**: `Prefix_middle_Suffix.png`

### Scenario 5: Keeping Original Name with Prefix and Suffix

- **Original File Name**: `example.png`
- **Prefix**: `Prefix_`
- **Suffix**: `_Suffix`
- **Keep Original Name**: Checked
- **Result**: `Prefix_example_Suffix.png`

### Note

- If multiple files are selected, they will be automatically numbered to avoid conflicts:
  - `example_1.png`
  - `example_2.png`
  - `example_3.png`
