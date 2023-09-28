# Description
This Python script is designed to perform data processing tasks on a CSV files named "*.csv". It utilizes the pandas library for data manipulation. The purpose of this script is to filter and reorganize the data from the input CSV file and then save the results in a new CSV file named "stc_csv.csv".
# Prerequisites
Before running this script, ensure you have the following prerequisites installed:
- Python: Make sure you have Python installed on your system. You can download it from Python's official website.
- pandas: This script relies on the pandas library, which is a popular data manipulation library in Python. You can install it using pip:
```
pip install pandas
```
# Usage
1. Place the script in the same directory as your "*.csv" file. If your CSV file has a different name or is located in a different directory, you can modify the script accordingly by changing the filename in the following line:
```
stc_csv = pd.read_csv("*.csv", encoding='cp1252' ,names=cal_name)
```
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:
```
python script.py
```
Replace "script.py" with the actual name of the Python script if it's different.
4. The script will perform the following tasks:
- Read the "stc.csv" file into a pandas DataFrame using the specified column names.
- Filter the DataFrame to keep only rows where the "Description" column equals "Current_Bill_Amount."
- Remove unnecessary columns ('group_name', 'FROM_DATE', 'Description', 'TO_DATE', 'NUMBER_OF_UNIT', 'UNIT', 'VOLUME', 'discount') from the DataFrame.
- Convert the "Phone_Number" column to integer type.
- Sort the DataFrame by the "Phone_Number" column in ascending order.
- Save the resulting DataFrame to a new CSV file named "*_YYYY_mm_dd.csv" in the same directory.
5. After the script completes, you can find the processed data in the "*_YYYY_mm_dd.csv" file in the same directory.
# Note
Make sure the input CSV file ("*_YYYY_mm_dd.csv") contains the necessary data and follows the expected format. Additionally, this script assumes that the "*.csv" file uses the 'cp1252' encoding; you may need to adjust the encoding if your file uses a different encoding.

Please ensure you have a backup of your original data before running this script, as it modifies and creates a new CSV file.
