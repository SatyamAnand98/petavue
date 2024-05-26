# AI Engine for Excel and Google Sheet Data Manipulation

## Objective

Develop an AI engine capable of reading, analyzing, and updating data in an Excel or Google Sheet. The engine should be able to handle both structured and unstructured data, using OpenAI for processing unstructured data.

## Technical Specifications

-   The AI engine should be built using Python or NodeJS.
-   OpenAI should be leveraged for text-based data analysis and manipulation.
-   Appropriate libraries/APIs should be used for reading and writing to Excel or Google Sheets.

## Task Breakdown

### Data Generation

-   Structured Data (Priority 1): Generate a synthetic dataset containing structured data (e.g., numerical and categorical data) with at least 10,000 rows and 30+ columns. Save this data in an Excel sheet.
-   Unstructured Data (Priority 2): Generate a synthetic dataset containing unstructured data (e.g., text data) with at least 1,000 rows and 5 columns. If possible, use OpenAI to create realistic text entries. Save this data in another sheet within the same Excel file.

### Data Reading and Manipulation

-   Read data from the Excel or Google Sheet, which contains at least 10,000 rows and 30+ columns.
-   Perform basic mathematical operations (addition, subtraction, multiplication, and division) on numerical columns. Create new columns to store the results.
-   Calculate aggregations (sum, average, min, max, etc.) on numerical columns and produce a summary report.
-   Perform different types of joins (inner, left, right, etc.) with another dataset. Assume another dataset will be provided or generated.
-   Create a pivot table from the existing data and also perform the reverse operation to unpivot the table back to a normal dataset.
-   Perform date operations such as extracting the month, day, and year from date columns, and calculating the difference between two dates.
-   Create new columns based on existing structured data using formulas. All rows in the new columns should be updated accordingly.
-   Handle edge cases related to empty cells so that the formulas work seamlessly.
-   Create additional new columns by analyzing the unstructured data using OpenAI. The AI should understand the context or sentiment of the unstructured text and perform appropriate manipulations.

### API Development

-   Develop a RESTful API to trigger the AI engine's functions. The API should take the Sheet URL/File and user input, and perform operations such as searching the sheet, performing an operation, and updating the sheet. The API should be robust enough to handle large datasets without timing out and should provide meaningful error messages.

### Error Handling

-   Implement appropriate error handling for file read/write operations, OpenAI interactions, and data manipulations.

### Documentation

-   Provide a README file that contains instructions on setting up and running the application, along with explanations of the design and code choices.

## Progress Update

We strongly recommend sharing work-in-progress code by pushing it to your Git account as you make progress. This is how you would operate and work with the Petavue team if you take up this role, so it's always better for you and us to operate in the same fashion even during the assessment stage. You will be added to a WhatsApp group during the assignment period to minimize communication delays.
AI Engine for Excel and Google Sheet Data Manipulation Objective:
Develop an AI engine capable of reading, analyzing, and updating data in an Excel or Google Sheet. The sheet will contain both structured and unstructured data, and the engine should use OpenAI for processing unstructured data.

# Original Document:

Technical Specifications:
● The AI engine should be built using Python OR NodeJS.
● Leverage OpenAI for text-based data analysis and manipulation.
● Use appropriate libraries/APIs for reading and writing to Excel or Google Sheets.
Task Breakdown: Data Generation:
Structured Data(Priority 1): Generate a synthetic dataset containing structured data (e.g., numerical and categorical data) with at least 1,0000 rows and 30+ columns. Save this data in an Excel sheet.
Unstructured Data(Priority 2): Generate a synthetic dataset containing unstructured data (e.g., text data) with at least 1,000 rows and 5 columns. Use OpenAI to create realistic text entries if possible. Save this data in another sheet within the same Excel file.
Data Reading and Manipulation:
Read data from the Excel or Google Sheet which contains at least 10,000 rows and 30+ columns.
Basic Math Operations: Perform basic mathematical operations such as addition, subtraction, multiplication, and division on numerical columns. Create new columns to store the results.
Aggregations: Calculate aggregations like sum, average, min, max, etc., on numerical columns and produce a summary report.
Joining: Perform different types of joins (inner, left, right, etc.) with another dataset. Assume another dataset will be provided or generated.
Pivot and Unpivot: Create a pivot table from the existing data and also perform the

reverse operation to unpivot the table back to a normal dataset.
Date Operations: Perform operations like extracting the month, day, and year from date columns, and calculate the difference between two dates.
Create new columns based on existing structured data using formulas. All rows in the new columns should be updated accordingly.
Handle edge cases related to empty cells so that the formulas work seamlessly.
Create additional new columns by analyzing the unstructured data using OpenAI. The AI should understand the context or sentiment of the unstructured text and perform appropriate manipulations.
API Development:
Develop a RESTful API to trigger the AI engine's functions. This API should take the Sheet URL/File, User input and perform the operations like search something from the Sheet, Performing an operation and update the sheet etc. The API should be robust enough to handle large datasets without timing out and should provide meaningful error messages.
Error Handling:
Implement appropriate error handling for file read/write operations, OpenAI interactions, and data manipulations.
Documentation:
Provide a README file that contains instructions on setting up and running your application, along with explanations of the choices you made in your design and code.
Progress Update
We strongly recommend you to share work in progress code. Keep pushing to your git account as you make progress. This is how you would operate and work with the Petavue team if you take up this role, so it's always better for you and us to operate in the very same fashion even during the assessment stage.
You will be added to Whatsapp group during the assignment period to make the communication delay minimal.
