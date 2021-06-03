import logging

import click

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

form = "%(asctime)s %(levelname)-8s %(funcName)-15s %(message)s"
logging.basicConfig(format=form,
                    datefmt="%H:%M:%S")

@click.group()
def cli():
    """This function is necessary for the click CLI to work."""

@cli.command()
@click.option('--camera', type=int, default=None, 
    help='The integer camera identifier. 0 if only one camera connected.')
@click.option('--video', default=None, 
        help='Path to the video file. Only used if'
        'the camera argument is not supplied')
@click.option('--detector_type',
    default='darknet', 
    type=click.Choice([
        'darknet',
        'xnor'], case_sensitive=False),
    help='The detector type to use.')
@click.option("--use_existing/--no-use_existing",
    is_flag=True,
    default=False,
    help="Whether or not to reload existing file info and object counts.")
<<<<<<< HEAD

=======
@click.option('--verbosity', '-v',
    default='INFO', 
    type=click.Choice([
        'CRITICAL',
        'ERROR',
        'WARNING',
        'INFO',
        'DEBUG',
        'NOTSET']),
    help='Logging verbosity level.')
>>>>>>> Lots of stuff
def go(
        camera: int,
        video: str,
        detector_type,
<<<<<<< HEAD
        use_existing: bool
    ):
    # need to use format with logger
    logger.info('Plotting all tickers {}'.format(TICKERS))
=======
        use_existing: bool,
        verbosity: str,
    ):
    # set verbosity. Do it jankily because life is too short.
    eval("logger.setLevel(logging.{})".format(verbosity)) #pylint: disable=eval-used

    # make sure not to use f-strings with logging
    logger.info('hey {}!'.format('you'))
>>>>>>> Lots of stuff

if __name__ == '__main__':
    cli()