import click

# Setup commandline options
@click.command()
@click.argument('f_in',
            type=click.Path(exists=True))
@click.argument('f_out', 
            type=click.Path())
def main_entry(input_file, output_file):
    """
        WinevtJSON utility - used to convert Microsoft Windows system event logs into JSON format.
        
        \b
        F_IN = A Microsoft Windows system event log (.evtx) file exported from Event Viewer or Sysmon.

        \b
        F_OUT = Path to a file for output of data.
    """


if __name__ == '__main__':
    main_entry()
