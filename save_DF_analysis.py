
def save_dataframe_analysis(df, output_file="data_analysis.txt"):
    """
    Saves key information about a DataFrame to a text file.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.
    output_file (str): The path to save the text file.

    Returns:
    str: The path to the saved text file.
    """
    try:
        with open(output_file, "w") as file:
            # Write head of the DataFrame
            file.write("HEAD of the DataFrame:\n")
            file.write(df.head().to_string())
            file.write("\n\n")

            # Write missing values
            file.write("MISSING VALUES:\n")
            file.write(df.isnull().sum().to_string())
            file.write("\n\n")

            # Write statistical summary
            file.write("DESCRIBE (Statistics):\n")
            file.write(df.describe().to_string())
            file.write("\n\n")

            # Write info about the DataFrame
            file.write("INFO:\n")
            df.info(buf=file)
            file.write("\n\n")

            # Write tail of the DataFrame
            file.write("TAIL of the DataFrame:\n")
            file.write(df.tail().to_string())

        print(f"Analysis saved to {output_file}")
        return output_file

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
