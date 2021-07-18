try:
    import win32com.client
except ModuleNotFoundError:
    # Error handling
    pass

def _parse(args):
    input_file_name = args.get('--input-file-name', '')
    output_file_name = args.get('--output-file-name', '')
    return [input_file_name, output_file_name]

def _PPTtoPDF(input_file_name, output_file_name, formatType = 32):
    powerpoint = win32com.client.DispatchEx("Powerpoint.Application")
    powerpoint.Visible = True

    if output_file_name[-3:] != 'pdf':
        output_file_name = output_file_name + ".pdf"
    deck = powerpoint.Presentations.Open(input_file_name)
    deck.SaveAs(output_file_name, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

name = 'ppt-to-pdf'

def operator(df, args):
    return _PPTtoPDF(*_parse(args))

if __name__ == "__main__":
    import pathlib
    args = {
        '--input-file-name': str(pathlib.Path.cwd() / 'convert/tests/result.pptx'),
        '--output-file-name': str(pathlib.Path.cwd() / 'convert/tests/result.pdf'),
    }
    operator(None, args)