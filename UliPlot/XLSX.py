#!/usr/bin/env python3
import openpyxl.utils.cell

def auto_adjust_xlsx_column_width(df, writer, sheet_name, margin=3, length_factor=1.0, index=True):
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
    writer_type = type(writer.book).__module__ # e.g. 'xlsxwriter.workbook' or 'openpyxl.workbook.workbook'
    is_openpyxl = writer_type.startswith("openpyxl")
    is_xlsxwriter = writer_type.startswith("xlsxwriter")
    if not is_openpyxl and not is_xlsxwriter:
        raise ValueError("Only openpyxl and xlsxwriter are supported as backends, not " + writer_type)
    sheet = writer.sheets[sheet_name]
    # Compute & set column width for each column
    for column_name in df.columns:
        # Convert the value of the columns to string and select the 
        column_length =  max(df[column_name].astype(str).map(len).max(), len(column_name))
        # Get index of column in XLSX
        # Column index is +1 if we also export the index column
        col_idx = df.columns.get_loc(column_name)
        if index:
            col_idx += 1
        # Set width of column to (column_length + margin)
        if is_openpyxl:
            sheet.column_dimensions[openpyxl.utils.cell.get_column_letter(col_idx + 1)].width = column_length * length_factor + margin
        else: # is_xlsxwriter
            sheet.set_column(col_idx, col_idx, column_length * length_factor + margin)
    # Compute column width of index column (if enabled)
    if index: # If the index column is being exported
        index_length =  max(df.index.astype(str).map(len).max(), len(df.index.name or ""))
        if is_openpyxl:
            sheet.column_dimensions["A"].width = index_length * length_factor + margin
        else: # is_xlsxwriter
            sheet.set_column(0, 0, index_length * length_factor + margin)
