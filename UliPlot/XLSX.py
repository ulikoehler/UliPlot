#!/usr/bin/env python3

def auto_adjust_xlsx_column_width(df, writer, sheet_name, margin=2, index=True):
    """
    Auto adjust column width to fit content in a XLSX exported from a pandas DataFrame.

    How to use:
    ```
    with pd.ExcelWriter(filename) as writer:
        df.to_excel(writer, sheet_name="MySheet")
        auto_adjust_column_width_index(df, writer, sheet_name="MySheet", margin=3)
    ```

    :param DataFrame df: The DataFrame used to export the XLSX.
    :param pd.ExcelWriter writer: The pandas exporter with engine="xlsxwriter"
    :param str sheet_name: The name of the sheet
    :param int margin: How many extra space (beyond the maximum size of the string)
    :param bool index: Whether the DataFrame's index is inserted as a separate column (if index=False in df.to_xlsx() set index=False here!)
    """
    for column_name in df.columns:
        # Convert the value of the columns to string and select the 
        column_length =  max(df[column_name].astype(str).map(len).max(), len(column_name))
        # Get index of column in XLSX
        # Column index is +1 if we also export the index column
        col_idx = df.columns.get_loc(column_name)
        if index:
            col_idx += 1
        # Set width of column to (column_length + margin)
        writer.sheets[sheet_name].set_column(col_idx, col_idx, column_length + margin)
    # Compute column width of index column (if enabled)
    if index: # If the index column is being exported
        index_length =  max(df.index.astype(str).map(len).max(), len(column))
        writer.sheets[sheet_name].set_column(0, 0, index_length + margin)
